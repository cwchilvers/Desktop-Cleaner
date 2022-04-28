import os, shutil

desktop = os.path.expanduser(os.sep.join(['~', 'Desktop']))
destination = os.path.expanduser(os.sep.join(['~', 'Documents\Sorted Files\\']))

for file in os.listdir(desktop):
    for letter in file:
        if letter == ".":
            extension = os.path.splitext(file)
            extension = extension[1].replace(".", "")
            extension_directory = destination + extension
            if not os.path.exists(extension_directory):
                os.makedirs(extension_directory)
            shutil.move(desktop + "\\" + file, extension_directory + "\\" + file)
            print("Moved " + file)

input()


