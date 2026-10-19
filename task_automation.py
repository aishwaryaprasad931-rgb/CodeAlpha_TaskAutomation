import os
import shutil


def move_jpg_files(source_folder, destination_folder):
    # Check whether the source folder exists
    if not os.path.isdir(source_folder):
        print(f"Error: Source folder not found: {source_folder}")
        return

    # Prevent moving files into the source folder itself
    source_path = os.path.abspath(source_folder)
    destination_path = os.path.abspath(destination_folder)

    if source_path == destination_path:
        print("Error: Source and destination folders must be different.")
        return

    # Create the destination folder if necessary
    os.makedirs(destination_path, exist_ok=True)

    moved_count = 0
    skipped_count = 0

    # Examine files in the source folder
    for filename in os.listdir(source_path):
        file_path = os.path.join(source_path, filename)

        # Select JPG files only; ignore subdirectories
        if os.path.isfile(file_path) and filename.lower().endswith(".jpg"):
            target_path = os.path.join(destination_path, filename)

            # Avoid overwriting an existing file
            if os.path.exists(target_path):
                print(f"Skipped (already exists): {filename}")
                skipped_count += 1
                continue

            try:
                shutil.move(file_path, target_path)
                print(f"Moved: {filename}")
                moved_count += 1
            except OSError as error:
                print(f"Could not move {filename}: {error}")

    print("\n--- Task Automation Report ---")
    print(f"JPG files moved: {moved_count}")
    print(f"Files skipped: {skipped_count}")
    print("Automation completed.")


if __name__ == "__main__":
    source = input("Enter the source folder path: ").strip().strip('"')
    destination = input("Enter the destination folder path: ").strip().strip('"')

    move_jpg_files(source, destination)