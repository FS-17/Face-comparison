import face_recognition
import os
from Database import database
import argparse

target_folder = "faces"  # the folder that contains the images


def load_images():
    # Create a database connection
    db = database()
    db.reset()

    try:
        target_files = os.listdir(target_folder)
    except FileNotFoundError:
        print(f"Folder {target_folder} not found")
        exit()

    # loop through the files in the folder
    for target_file in target_files:
        # check if the file is an image
        if not is_image(target_file):
            continue

        # load the image and get the encoding
        target_path = os.path.join(target_folder, target_file)
        target_image = face_recognition.load_image_file(target_path)
        encoding = face_recognition.face_encodings(target_image)

        if encoding:
            encoding = encoding[0].tolist()
            db.cursor.execute(
                "INSERT INTO faces (name, encoding) VALUES (?, ?)", (target_file, str(encoding)))
            db.conn.commit()
        else:
            continue

    # close the database connection
    del db

    print("Images loaded successfully")


def is_image(file):
    file = file.lower()
    return file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--folder", help="The path to the folder")
    args = parser.parse_args()

    if args.folder:
        target_folder = args.folder

    load_images()
