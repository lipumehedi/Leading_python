
import argparse
import shutil
from pathlib import Path


def organize_folder(folder, dry_run=False):
    folder = Path(folder).expanduser().resolve()

    if not folder.is_dir():
        raise ValueError("The specified folder does not exist.")

    categories = {
        ".pdf": "PDF",
        ".doc": "Documents",
        ".docx": "Documents",
        ".txt": "Documents",
        ".jpg": "Images",
        ".jpeg": "Images",
        ".png": "Images",
        ".gif": "Images",
        ".mp3": "Audio",
        ".wav": "Audio",
        ".mp4": "Videos",
        ".mov": "Videos",
        ".zip": "Archives",
        ".csv": "Spreadsheets",
        ".xlsx": "Spreadsheets",
    }

    files = [
        path for path in folder.iterdir()
        if path.is_file() and path.name != Path(__file__).name
    ]

    moved = 0

    for file_path in files:
        category = categories.get(file_path.suffix.lower(), "Others")
        destination_dir = folder / category
        destination = destination_dir / file_path.name

        if destination.exists():
            print(f"Skipped (destination exists): {file_path.name}")
            continue

        if dry_run:
            print(f"Would move: {file_path.name} -> {category}/")
        else:
            destination_dir.mkdir(exist_ok=True)
            shutil.move(str(file_path), str(destination))
            print(f"Moved: {file_path.name} -> {category}/")

        moved += 1

    print(f"\n{'Would organize' if dry_run else 'Organized'}: {moved} file(s)")


def main():
    parser = argparse.ArgumentParser(description="Organize files by extension.")
    parser.add_argument("folder", help="Folder to organize")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without moving files",
    )
    args = parser.parse_args()

    try:
        organize_folder(args.folder, args.dry_run)
    except (ValueError, OSError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
