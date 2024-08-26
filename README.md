# Kebab Case File Renamer

This script recursively renames files and directories to kebab case format, providing a consistent and clean file naming structure.

## Why Use This Script?

File organization is crucial for efficient workflows, especially when dealing with downloaded courses, projects, or any collection of files from various sources. This script addresses several common issues:

1. **Inconsistent Naming**: Downloaded files often come with inconsistent naming conventions, making navigation and organization difficult.
2. **Special Characters**: Files may contain spaces, underscores, or other special characters that can cause issues in command-line operations or scripts.
3. **Case Sensitivity**: Mixed case filenames can lead to confusion and potential conflicts in case-sensitive file systems.
4. **Improved Readability**: Kebab case (e.g., "my-file-name.txt") offers a clean, consistent, and easily readable format.
5. **Command-Line Friendly**: Kebab case names are easy to type and use in command-line operations without requiring quotes or escapes.

By converting all file and directory names to kebab case, this script helps create a uniform, Linux-friendly file structure that's easier to navigate, manage, and use in various development and organizational contexts.

## Usage
```
python kebab_case_renamer.py <directory_path>
```

## Features
- Converts file and directory names to kebab case
- Handles special characters and spaces
- Renames the starting directory as well
- Preserves file extensions
- Recursively processes all subdirectories

## Requirements
- Python 3.x

## Caution
Always backup your files before running this script, as the renaming process is irreversible.

## Example
Before:
```
My Project/
├── 01-Introduction to Topic.pdf
├── Chapter 2_Main Concepts.docx
└── FINAL NOTES.txt
```

After:
```
my-project/
├── 01-introduction-to-topic.pdf
├── chapter-2-main-concepts.docx
└── final-notes.txt
```

This script is particularly useful for organizing educational materials, project files, or any collection of documents where consistent naming would improve workflow and file management.
