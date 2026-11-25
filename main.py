import shutil
from pathlib import Path


FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx", ".md"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".webm"],
    "Audio": [".mp3", ".wav", ".ogg", ".m4a", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp"]
}


def get_category(file_path):
    extension = file_path.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def get_unique_path(destination):
    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = f"{destination.stem}_{counter}{destination.suffix}"
        new_path = destination.parent / new_name

        if not new_path.exists():
            return new_path

        counter += 1


def organize_files(folder_path):
    folder = Path(folder_path).expanduser()

    if not folder.exists() or not folder.is_dir():
        print("Error: The specified folder does not exist.")
        return

    folder = folder.resolve()
    current_script = Path(__file__).resolve()
    moved_count = 0

    print("\nStarting file organization...\n")

    for file in list(folder.iterdir()):
        if not file.is_file():
            continue

        if file.name.startswith(".") or file.resolve() == current_script:
            continue

        category = get_category(file)
        destination_folder = folder / category
        destination_folder.mkdir(exist_ok=True)

        destination = get_unique_path(destination_folder / file.name)

        try:
            shutil.move(str(file), str(destination))
            print(f"Moved: {file.name} -> {category}/")
            moved_count += 1
        except OSError as error:
            print(f"Could not move {file.name}: {error}")

    print(f"\nOrganization completed! {moved_count} file(s) moved.")


if __name__ == "__main__":
    print("=" * 40)
    print("       PYTHON FILE ORGANIZER")
    print("=" * 40)

    folder_path = input("\nEnter the folder path to organize: ")
    organize_files(folder_path)
