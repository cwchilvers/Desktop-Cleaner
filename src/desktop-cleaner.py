import os, shutil

desktop = os.path.expanduser('~/Desktop')
destination = os.path.expanduser('~/Documents/Desktop Cleaner')

# Dictionary of file extensions
extensions = {
    'image': ['ai', 'apng', 'avif', 'avifs', 'bmp', 'gif', 'heic', 'heif', 'ico', 'jfif', 'jfif-tbnl', 'jfi', 'jpe', 'jpeg', 'jpg', 'jif', 'png', 'psd', 'raw', 'svg', 'tiff', 'tif', 'webp', 'webp', 'h264', 'h265', 'mkv', 'webm'],
    'video': ['3g2', '3gp', 'avi', 'flv', 'f4a', 'f4b', 'f4p', 'f4v', 'm2v', 'm4v', 'mkv', 'mng', 'mov', 'mp2', 'mp4', 'mpg', 'mpe', 'mpeg', 'mpv', 'mxf', 'nsv', 'ogg', 'qt', 'roq', 'svi', 'swf', 'vob', 'webm', 'wmv'],
    'audio': ['aac', 'aif', 'aifc', 'aiff', 'ape', 'au', 'flac', 'm4a', 'mac', 'mid', 'midi', 'mka', 'mp3', 'oga', 'ogg', 'opus', 'ra', 'rm', 'snd', 'wav', 'wma', 'm4b', 'alac', 'aiff'],
    'document': ['csv', 'doc', 'docx', 'key', 'log', 'msg', 'numbers', 'odp', 'ods', 'odt', 'pages', 'pdf', 'ppt', 'pptx', 'rtf', 'txt', 'wps', 'wpd', 'xlr', 'xls', 'xlsx', 'xml', 'odt', 'tex', 'texinfo', 'md', 'json', 'yaml'],
    'executable': ['apk', 'app', 'bat', 'com', 'exe', 'gadget', 'jar', 'msi', 'wsf', 'vbs', 'vb', 'appimage'],
    'archive': ['7z', 'ace', 'arj', 'bz2', 'cab', 'deb', 'dmg', 'gz', 'hqx', 'iso', 'lzh', 'pkg', 'rar', 'rpm', 'sea', 'sit', 'sitx', 'tar', 'uue', 'zip', 'zipx', 'z', 'gzip', 'bzip2', 'lzma', 'xz', 'tar.gz', 'tar.bz2', 'tar.xz', 'tar.lzma', 'tar.z']
}

# Create destination folder if it doesn't exist
if not os.path.exists(destination):
    os.makedirs(destination)

try:
    # Move desktop files & folders to destination folder
    for item in os.listdir(desktop):
        source = os.path.join(desktop, item)
        if os.path.isfile(source):
            extension = item.split('.')[-1].lower()
            if extension in extensions['image']:
                destination_folder = os.path.join(destination, 'Images')
            elif extension in extensions['video']:
                destination_folder = os.path.join(destination, 'Videos')
            elif extension in extensions['audio']:
                destination_folder = os.path.join(destination, 'Audio')
            elif extension in extensions['document']:
                destination_folder = os.path.join(destination, 'Documents')
            elif extension in extensions['executable']:
                destination_folder = os.path.join(destination, 'Executables')
            elif extension in extensions['archive']:
                destination_folder = os.path.join(destination, 'Archives')
            else:
                destination_folder = os.path.join(destination, 'Other')
        else:
            destination_folder = os.path.join(destination, 'Folders')

        os.makedirs(destination_folder, exist_ok=True)
        shutil.move(source, os.path.join(destination_folder, item))
        print("Moved", item, "successfully")

    print("Cleaned up desktop successfully. Files are now located in", destination)

except Exception as e:
    print("An error occurred during the cleaning process:", str(e))

# Pause until user presses enter
input("Press enter to exit")