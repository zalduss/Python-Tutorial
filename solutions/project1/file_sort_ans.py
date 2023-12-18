import os
import shutil

# Define the directory to organize
directory = '/Users/zald/Documents/Projects/tutorial_python/file_sorter'

# Define the file type categories and their corresponding extensions
file_types = {
    'Documents': ['.pdf', '.doc', '.docx', '.txt'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Spreadsheets': ['.xls', '.xlsx', '.csv']
}

# Create folders for each category if they don't exist
for category in file_types.keys():
    folder_path = os.path.join(directory, category)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def get_category(file_extension):
    for category, extensions in file_types.items():
        if file_extension in extensions:
            return category
    return 'Others'

# Organize the files
for filename in os.listdir(directory):
    if filename.startswith('.') or os.path.isdir(os.path.join(directory, filename)):
        continue  # Skip hidden files and directories

    # Skip the script itself
    if filename == os.path.basename(__file__):
        continue

    _, file_extension = os.path.splitext(filename)
    file_extension = file_extension.lower()

    category = get_category(file_extension)
    source_path = os.path.join(directory, filename)
    destination_path = os.path.join(directory, category, filename)

    shutil.move(source_path, destination_path)

print("Files organized successfully.")
