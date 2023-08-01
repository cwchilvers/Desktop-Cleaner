import ..config.extensions as extensions

def organize():
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

        return jsonify({'status': 'success', 'message': 'Desktop cleaned up successfully. Files are now located in ' + destination})

    except Exception as e:
        return jsonify({'status': 'error', 'message': 'An error occurred during the cleaning process: ' + str(e)})