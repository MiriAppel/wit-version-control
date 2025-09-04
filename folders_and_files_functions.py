import os

# יצירת תיקייה חדשה במיקום שנבחר
def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

# בדיקה האם תיקייה ריקה
def is_empty_folder(path):
    dir = os.listdir(path)
    if len(dir) == 0:
        return True
    return False
