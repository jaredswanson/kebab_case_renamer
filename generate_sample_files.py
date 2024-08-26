import os
import random

def create_sample_files(base_path):
    # Sample file names with various formats
    file_names = [
        "01-Introduction to Programming.pdf",
        "Lesson 2_ Data Structures.txt",
        "Chapter 3 - Algorithms and Complexity.docx",
        "04 ADVANCED TOPICS.mp4",
        "Final Project_Guidelines.xlsx",
        "Appendix A - Additional Resources.html",
        "Quiz 1 Answers (Do Not Open).pdf",
        "Lecture Notes - Week 5.md",
        "LAB_EXERCISE_6.py",
        "Group Project Ideas & Guidelines.pptx"
    ]

    # Sample directory names
    dir_names = [
        "01-Course Materials",
        "Week 2_Assignments",
        "BONUS CONTENT",
        "Extra Credit Opportunities",
        "Required_Reading_List",
        "student resources",
        "Project Files (Final)",
        "Archived Lectures - Spring 2023",
        "Discussion_Forum_Topics",
        "Quiz & Exam Prep"
    ]

    def create_files(path, depth=0):
        if depth > 3:  # Limit directory depth
            return

        # Create some files in this directory
        for _ in range(random.randint(1, 5)):
            file_name = random.choice(file_names)
            with open(os.path.join(path, file_name), 'w') as f:
                f.write(f"This is a sample file: {file_name}")

        # Create some subdirectories
        for _ in range(random.randint(1, 3)):
            dir_name = random.choice(dir_names)
            new_dir = os.path.join(path, dir_name)
            os.makedirs(new_dir, exist_ok=True)
            create_files(new_dir, depth + 1)

    # Create the base directory
    os.makedirs(base_path, exist_ok=True)
    create_files(base_path)

    print(f"Sample files and directories created in: {base_path}")

if __name__ == "__main__":
    base_directory = "sample_course_files"
    create_sample_files(base_directory)
