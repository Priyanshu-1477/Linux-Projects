#!/usr/bin/env python3
import os
import sys

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def list_directory(path):
    try:
        entries = os.listdir(path)
        entries.sort()
        print(f"\nContents of: {path}\n")
        for index, entry in enumerate(entries):
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                print(f"[{index}] 📁 {entry}/")
            else:
                print(f"[{index}] 📄 {entry}")
        return entries
    except Exception as e:
        print(f"Error: {e}")
        return []

def open_file(path):
    print(f"\n--- Preview of {os.path.basename(path)} ---")
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for i, line in enumerate(file):
                print(line.rstrip())
                if i == 19:
                    print("... [file preview limited to 20 lines] ...")
                    break
    except Exception as e:
        print(f"Cannot open file: {e}")

def file_explorer():
    current_path = os.getcwd()

    while True:
        clear_screen()
        entries = list_directory(current_path)

        print("\nOptions:")
        print("[c] Change directory")
        print("[o] Open file")
        print("[u] Go up one directory")
        print("[q] Quit")

        choice = input("\nEnter your choice: ").strip()

        if choice == 'q':
            break
        elif choice == 'c':
            sub = input("Enter folder index or name: ")
            try:
                idx = int(sub)
                folder = entries[idx]
            except:
                folder = sub
            new_path = os.path.join(current_path, folder)
            if os.path.isdir(new_path):
                current_path = new_path
            else:
                input("Not a valid directory. Press Enter to continue.")
        elif choice == 'u':
            current_path = os.path.dirname(current_path)
        elif choice == 'o':
            sub = input("Enter file index or name: ")
            try:
                idx = int(sub)
                file = entries[idx]
            except:
                file = sub
            file_path = os.path.join(current_path, file)
            if os.path.isfile(file_path):
                clear_screen()
                open_file(file_path)
                input("\nPress Enter to return.")
            else:
                input("Not a valid file. Press Enter to continue.")
        else:
            input("Invalid option. Press Enter to try again.")

if __name__ == '__main__':
    file_explorer()
