import folders_and_files_functions as ff
from commit_version import *
from datetime import datetime
import os
import shutil
import json


class Repository:
    def __init__(self, current):
        self.current_path = current
        self.dictionary = {}


    def wit_init(self):
        try:
            if os.path.exists(self.current_path + '\.wit'):
                print("Repository already exist.")
            else:
                ff.create_folder(self.current_path + '\.wit')
                ff.create_folder(self.current_path + '\.wit\stage')
                ff.create_folder(self.current_path + '\.wit\commit')
                print("Repository created successfully.")
        except Exception as e:
            return str(e)


    def wit_add(self, file_name):
        destination_directory = self.current_path + '\.wit\stage'  # ניתוב קבוע לתיקייה היעד
        try:
            # בודק אם הקובץ קיים
            if os.path.isfile(file_name):
                destination_path = os.path.join(destination_directory, file_name)
                shutil.copy(file_name, destination_path)
                print("File uped to stage.")
            else:
                print("File does not exist.")
        except Exception as e:
            return str(e)


    def wit_commit(self, message):
        source_directory = self.current_path + '\.wit\stage'
        target_directory = self.current_path + '\.wit\commit'
        try:
            if ff.is_empty_folder(source_directory):
                print("Not have files to commit.")
                return
            # טוען נתונים קיימים מקובץ JSON אם קיים
            if os.path.exists(self.current_path + '\.wit\commit_data.json'):
                with open(self.current_path + '\.wit\commit_data.json', 'r') as json_file:
                    self.dictionary = json.load(json_file)
            else:
                self.dictionary = {}
            if not ff.is_empty_folder(source_directory):
                version_object = CommitVersion(str(hash(message)), datetime.now(), message)
                # יצירת התיקיה החדשה עם השם שניתן
                new_directory = os.path.join(target_directory, version_object.hash_code)
                if not os.path.exists(new_directory):
                    os.makedirs(new_directory)  # ,exist_ok=True)
                # מעבר על כל הקבצים בתיקיה המקורית
                for file_name in os.listdir(source_directory):
                    source_file = os.path.join(source_directory, file_name)
                    # בודק אם זה קובץ ולא תיקיה
                    if os.path.isfile(source_file):
                        target_file = os.path.join(new_directory, file_name)
                        shutil.move(source_file, target_file)  # מעביר את הקובץ
                # הוספת האובייקט למילון
                self.dictionary[version_object.hash_code] = {
                    'hash_code': version_object.hash_code,
                    'date': str(version_object.date),  # המרת התאריך
                    'message': version_object.message
                }
                # שמירת הנתונים לקובץ JSON
                with open(self.current_path + '\.wit\commit_data.json', 'w') as json_file:
                    json.dump(self.dictionary, json_file, ensure_ascii=False, indent=4)
                print("Committed successfully.")
        except Exception as e:
            return str(e)


    def wit_log(self):
        try:
            if not self.dictionary:
                print("No commits found.")
                return
            for hash_code, version_info in self.dictionary.items():
                print("Hash: {}, Date: {}, Message: {}".format(hash_code, version_info['date'], version_info['message']))
        except Exception as e:
            return str(e)

    def wit_status(self):
        try:
            if ff.is_empty_folder(self.current_path + '\.wit\stage'):
                print("There are no committed changes.")
            else:
                print("There are changes that have not been committed.")
        except Exception as e:
            return str(e)


    def wit_checkout(self, commit_id):
        target_directory = os.path.join(self.current_path, '.wit', 'commit', commit_id)
        try:
            # טוען נתונים קיימים מקובץ JSON אם קיים
            if os.path.exists(self.current_path + '\.wit\commit_data.json'):
                with open(self.current_path + '\.wit\commit_data.json', 'r') as json_file:
                    self.dictionary = json.load(json_file)
            else:
                print("No commit data found.")
                return
            if commit_id not in self.dictionary:
                print("Commit ID does not exist.")
                return
            # נוודא שהתיקיה קיימת
            if not os.path.exists(target_directory):
                print("The specified commit does not exist.")
                return
            # ניקוי תיקיית העבודה הנוכחית
            for file_name in os.listdir(self.current_path):
                file_path = os.path.join(self.current_path, file_name)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            # העתקת הקבצים מהתיקיה של ה-commit לגרסה הנוכחית
            for file_name in os.listdir(target_directory):
                source_file = os.path.join(target_directory, file_name)
                target_file = os.path.join(self.current_path, file_name)
                shutil.copy(source_file, target_file)
            print("Checked out to commit {} successfully.".format(commit_id))
        except Exception as e:
            return str(e)



# rep = Repository(os.getcwd())
# rep.wit_init()
# rep.wit_add("hhh.txt")
# rep.wit_commit("bbb")
# rep.wit_log()
# rep.wit_status()
# rep.wit_checkout("-1512785904")