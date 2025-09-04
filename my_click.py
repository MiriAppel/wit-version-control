import click
from repository import Repository

class Cli:

    def __init__(self, current):
        self.repository = Repository(current)
        print(self.repository)

    def create_cli(self):

        @click.group()
        def cli():
            """Management user interface repository"""
            pass

        @cli.command()
        def init():
            try:
                self.repository.wit_init()
            except Exception as e:
                click.echo("Error {}".format(e))

        @cli.command()
        @click.argument("file_name")
        def add(file_name):
            try:
                self.repository.wit_add(file_name)
            except Exception as e:
                click.echo("Error {}".format(e))

        @cli.command()
        @click.argument("message")
        def commit(message):
            try:
                self.repository.wit_commit(message)
            except Exception as e:
                click.echo("Error {}".format(e))

        @cli.command()
        def log():
            try:
                self.repository.wit_log()
            except Exception as e:
                click.echo("Error {}".format(e))

        @cli.command()
        def status():
            try:
                self.repository.wit_status()
            except Exception as e:
                click.echo("Error {}".format(e))

        @cli.command()
        @click.argument("commit_hash")
        def checkout(commit_hash):
            try:
                self.repository.wit_checkout(commit_hash)
            except Exception as e:
                click.echo("Error {}".format(e))

        return cli
