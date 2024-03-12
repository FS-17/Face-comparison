# Face comparison project

## Description

This project uses face recognition to identify face in image. It includes scripts to load images into a database and compare faces in a given image with the faces in the database.

it can compare 1 to many faces and return the name of the person in the image.

## Installation

1. Clone this repository.
```bash
git clone https://github.com/FS-17/Face-comparison.git
```

2. Install the required Python packages by running 
```bash
pip install -r requirements.txt
```

3. Add faces to faces folder and run the loadimages.py script to load the images into the database.

4. Run the main.py script to compare faces in an image with the faces in the database.
```bash
python main.py --image <path_to_image>
```

note: `loadimages.py` run it only when you add new faces to the faces folder.
## Usage

1. Load images into the database by running `python loadimages.py --folder <path_to_folder>`. Replace `<path_to_folder>` with the path to the folder that contains the images you want to load.

2. Compare faces in an image with the faces in the database by running `python main.py --image <path_to_image>`. Replace `<path_to_image>` with the path to the image you want to compare.

## Contributing

Contributions are welcome. Please submit a pull request.

