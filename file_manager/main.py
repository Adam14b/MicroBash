import os
from commands import FileManager
from config import WORKDIR

def main():
    fm = FileManager(WORKDIR)

    while True:
        command = input(f"{fm.current_dir}> ").strip()
        if command == "exit":
            break

        try:
            fm.execute_command(command)
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()