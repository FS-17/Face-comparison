from Database import database
import argparse
import numpy as np
import face_recognition


# load the database
db = database()
all_faces = db.get_all()


def main(face_path):
    try:
        # Call the function to compare faces
        results = compare_faces(face_path)
        if results is None:
            print("No face found in the image")
            exit()
    except Exception as e:
        print("an error occurred")
        print(e)
        exit()

    text = ""
    # send the top 3 results
    for i in results:
        text = text + f"Result for {i[0]}: {i[1]:.2f}%\n\n"

    print(text)


def compare_faces(comparer_path):

    # Load the comparer image
    comparer_image = face_recognition.load_image_file(comparer_path)
    encoding = face_recognition.face_encodings(comparer_image)
    if encoding:
        comparer_encoding = encoding[0]
    else:
        return None

    # Initialize a list to store results
    results = []

    comparer_encoding = [comparer_encoding]

    # Compare the comparer encoding with each loaded encoding in the database
    for face in all_faces:
        loaded_encoding = np.array(face[1])
        face_distance = face_recognition.face_distance(
            comparer_encoding, loaded_encoding)
        comparison_percentage = (1 - face_distance[0]) * 100
        results.append((face[0], comparison_percentage))

    # Reorder the results by percentage
    results.sort(key=lambda x: x[1], reverse=True)

    # Get the top 3 results
    results = results[:3]

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", help="The path to the image")
    args = parser.parse_args()

    if args.image:
        face_path = args.image
    else:
        print("Please provide the path to the image")
        exit()

    main(face_path)
