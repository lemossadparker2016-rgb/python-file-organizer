# Python File Organizer

A simple Python tool that automatically organizes files into folders based on their file extensions. Keep your directories clean and organized with just one command.

## Features

- Automatically sorts files by type.
- Organizes images, documents, videos, audio files, archives, and source code.
- Creates category folders automatically.
- Handles duplicate filenames without overwriting existing files.
- Supports unknown file types through an Others folder.
- Uses Python's built-in libraries.
- No external dependencies required.

## Requirements

- Python 3.8 or higher.

## How to Use

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the following command:

```bash
python main.py
```

4. Enter the path of the folder you want to organize.
5. The program will automatically sort the files into their respective folders.

**Note:** Files are moved, not copied. Make sure you have a backup before organizing important files.

## Example Output

```text
========================================
       PYTHON FILE ORGANIZER
========================================

Enter the folder path to organize: /home/user/Downloads

Starting file organization...

Moved: photo.jpg -> Images/
Moved: report.pdf -> Documents/
Moved: presentation.pptx -> Documents/
Moved: video.mp4 -> Videos/
Moved: music.mp3 -> Audio/
Moved: project.zip -> Archives/

Organization completed! 6 file(s) moved.
```

## Project Structure

```text
python-file-organizer/
│
├── main.py
├── README.md
│
└── Images/
    ├── photo.jpg
    └── picture.png
```

## Technologies Used

- Python
- pathlib
- shutil

## License

This project is open-source and available under the MIT License.
