import os
import shutil


# Reference
# os — This module provides a portable way of using operating system dependent functionality
# https://docs.python.org/3/library/os.html
# shutil - The shutil module offers a number of high-level operations on files and collections of files.
# https://docs.python.org/3/library/shutil.html


def create_folder():
    print("Enter Folder name:")
    name = input()
    folder = os.getcwd() + "/" + name  # getcwd - Return a string representing the current working directory.
    if not os.path.exists(folder):  # Return True if path refers to an existing path
        os.makedirs(folder, 0o777)   # makedirs - creates folder
        print("Folder Created")
    else:
        print("Folder already exists")


def change_extension():
    print("Enter old Extension:")
    old_extension = input()
    print("Enter new Extension:")
    new_extension = input()
    folder = os.getcwd()                    # getcwd - Return a string representing the current working directory.
    for filename in os.listdir(folder):
        in_file_name = os.path.join(folder, filename) # os.path.join('home', 'abc', 'work') -> home/abc/work
        if not os.path.isfile(in_file_name):
            continue
        os.path.splitext(filename)
        new_name = in_file_name.replace(old_extension, new_extension)
        os.rename(in_file_name, new_name)
    print("Modifying Extension Complete")


def create_copy():
    print("Enter file Name with Extension")
    file_name = input()
    if os.path.isfile(file_name):
        shutil.copy2(file_name, '(copy)' + file_name)
        print("Copy Created")
    else:
        print("No such file")


def delete_file():
    print("Enter file Name with Extension")
    file_name = input()
    if os.path.isfile(file_name):
        os.remove(file_name)
        print("File Removed!")
    else:
        print("No such File")


def delete_folder():
    print("Enter folder")
    filename = input()
    if os.path.exists(filename):
        shutil.rmtree(filename, ignore_errors=True)  # Delete an entire directory tree; path must point to a directory
        print("Folder Deleted")
    else:
        print("No Such Folder")


def move_file():
    print("Enter filename:")
    filename = input()
    if os.path.exists(filename):
        print("Enter sub folder:")
        folder = input()
        if os.path.exists(folder):
            os.rename(filename, folder + '/' + filename)
            print("File moved")
        else:
            print("Folder doesnt exist. Would you like to create folder (yes/no)")
            f = input()
            if f == 'yes':
                os.makedirs(folder, 0o777)
                os.rename(filename, folder + '/' + filename)
                print("File moved")
            elif f == 'no':
                print("Folder not created")
            else:
                print("invalid input")
    else:
        print("No such file")


def move_ext():
    print("Enter Extension:")
    ext = input()
    print("Enter sub folder:")
    folder = input()
    flag = 0
    if not os.path.exists(folder):
        print("Folder doesnt exist. Would you like to create folder (yes/no)")
        f = input()
        if f == 'yes':
            os.makedirs(folder, 0o777)
        elif f == 'no':
            print("Folder not created")
        else:
            print("invalid input")
    if os.path.exists(folder):
        for filename in os.listdir(os.getcwd()):
            if ext in filename:
                os.rename(filename, folder + '/' + filename)
                flag = 1
    if flag == 0:
        print("No files moved")
    else:
        print("Moving of files complete")


print("\n         EASY  FILE  HANDLER           ")
print("          By Pritish Gupta            ")
print(" ------------------------------------")
while True:
    print("\n1.Change Extension")
    print("2.Create a folder")
    print("3.Create copy of a file")
    print("4.Delete file")
    print("5.Delete folder")
    print("6.Move specific file to sub folder")
    print("7.Move according to extension")
    print("0.Exit")
    cmd = input()
    if cmd == '1':
        change_extension()
    elif cmd == '2':
        create_folder()
    elif cmd == '3':
        create_copy()
    elif cmd == '4':
        delete_file()
    elif cmd == '5':
        delete_folder()
    elif cmd == '6':
        move_file()
    elif cmd == '7':
        move_ext()
    elif cmd == '0':
        break
    else:
        print("Invalid command.")
