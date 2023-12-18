
# Python File Organizer Tutorial

## Overview
In this project, you will develop a Python script to automatically organize files in a directory based on their file extensions (e.g, .mp4, .pdf). This project is an excellent way to practice the skills taught in earlier lessons. This project will help you understand file handling and directory/folder management. Before beginning the project lets go over an some important modules you're going to need, [os](../../module-library/os.md) and [shutil]()
## Requirements

- A zip file containing various file types (`.pdf`, `.mp4`, `.mp3`, `.csv`, etc.).

## Instructions

1. **Unzipping the File**: 
   - Start by unzipping the provided zip file. This will extract various files which we will organize using the Python script.

2. **Creating Necessary Folders**:
   - Create a .py file inside the unzipped folder. This will be your working directory.

3. **File Categories and Organization**:
   - The script organizes files into the following categories based on their file extensions:
     - `Documents`: Includes `.pdf`, `.doc`, `.docx`, `.txt` files.
     - `Images`: Includes `.jpg`, `.jpeg`, `.png`, `.gif` files.
     - `Music`: Includes `.mp3`, `.wav`, `.aac` files.
     - `Videos`: Includes `.mp4`, `.mov`, `.avi` files.
     - `Spreadsheets`: Includes `.xls`, `.xlsx`, `.csv` files.
   - For each category, a corresponding folder will be created where the files will be moved.

4. **Script Setup**:
   - Copy the provided boilerplate code into a new Python file in your working directory.
   - In the script, set the `directory` variable to the path of your working directory.

5. **Running the Script**:
   - Run the script. It will automatically create folders for each category and move the files into their respective folders.

6. **Completion**:
   - Once the script finishes running, your files will be organized into their respective folders.
   - Check the folders to verify that all files have been moved correctly.

## Boilerplate Code
```python
import os
import shutil

# Define the directory to organize
directory = '[Your Directory Path Here]'

# Define the file type categories and their corresponding extensions
file_types = {
    'Documents': ['.pdf', '.doc', '.docx', '.txt'],
    # Add other categories here as needed
}

# Add the remaining part of the provided script here
```

Remember to replace `[Your Directory Path Here]` with the actual path to your working directory.

Good Luck 😃