import os
import shutil
from config import WORKDIR

class FileManager:
    def __init__(self, workdir):
        self.workdir = workdir
        self.current_dir = workdir

    def execute_command(self, command):
        args = command.split()
        command_name = args[0]

        if command_name == "cd":
            self.change_directory(args[1])
        elif command_name == "ls":
            self.list_files()
        elif command_name == "mkdir":
            self.create_directory(args[1])
        elif command_name == "touch":
            self.create_file(args[1])
        elif command_name == "rm":
            self.remove(args[1])
        elif command_name == "cat":
            self.read_file(args[1])
        elif command_name == "cp":
            self.copy(args[1], args[2])
        elif command_name == "mv":
            self.move(args[1], args[2])
        elif command_name == "rename":
            self.rename(args[1], args[2])
        else:
            print(f"Неизвестная команда: {command_name}")

    def change_directory(self, new_dir):
        new_path = os.path.join(self.current_dir, new_dir)
        if os.path.exists(new_path) and os.path.isdir(new_path):
            self.current_dir = new_path
        else:
            raise ValueError("Директория не найдена")

    def list_files(self):
        for entry in os.listdir(self.current_dir):
            print(entry)

    def create_directory(self, dirname):
        path = os.path.join(self.current_dir, dirname)
        os.makedirs(path, exist_ok=True)

    def create_file(self, filename):
        path = os.path.join(self.current_dir, filename)
        open(path, 'a').close()

    def remove(self, path):
        path = os.path.join(self.current_dir, path)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)

    def read_file(self, filename):
        path = os.path.join(self.current_dir, filename)
        with open(path, 'r') as f:
            print(f.read())

    def copy(self, source, destination):
        source = os.path.join(self.current_dir, source)
        destination = os.path.join(self.current_dir, destination)
        if os.path.isdir(source):
            shutil.copytree(source, destination)
        else:
            shutil.copy2(source, destination)

    def move(self, source, destination):
        source = os.path.join(self.current_dir, source)
        destination = os.path.join(self.current_dir, destination)
        shutil.move(source, destination)

    def rename(self, old_name, new_name):
        old_path = os.path.join(self.current_dir, old_name)
        new_path = os.path.join(self.current_dir, new_name)
        os.rename(old_path, new_path)