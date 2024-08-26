import os
import re
import sys

def to_kebab_case(s):
    # Remove any characters that aren't alphanumeric or spaces
    s = re.sub(r'[^\w\s-]', '', s)
    # Replace spaces and underscores with hyphens
    s = re.sub(r'[\s_]+', '-', s)
    # Convert to lowercase
    return s.lower()

def rename_to_kebab_case(path):
    for root, dirs, files in os.walk(path, topdown=False):
        # Rename files
        for name in files:
            old_path = os.path.join(root, name)
            new_name = to_kebab_case(os.path.splitext(name)[0]) + os.path.splitext(name)[1]
            new_path = os.path.join(root, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed file: {old_path} -> {new_path}")

        # Rename directories
        for name in dirs:
            old_path = os.path.join(root, name)
            new_name = to_kebab_case(name)
            new_path = os.path.join(root, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed directory: {old_path} -> {new_path}")

    # Rename the starting directory
    parent_dir = os.path.dirname(path)
    new_name = to_kebab_case(os.path.basename(path))
    new_path = os.path.join(parent_dir, new_name)
    os.rename(path, new_path)
    print(f"Renamed starting directory: {path} -> {new_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory")
        sys.exit(1)

    rename_to_kebab_case(directory)
    print("Renaming process completed.")
