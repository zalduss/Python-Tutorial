# OS Module
The os library allows you to interact with the file system, including creating, renaming, moving, and deleting files and directories.

- os: operating system

## How to use os?
To use the os library, first import it at the top of your .py file.

```python
import os 
# rest of your code
```

## 1. File and Directory Management
Interact with the file system for operations like creating, renaming, moving, and deleting files and directories.

### Examples:
1. **Navigating the File System**:
   ```python
   import os
   cwd = os.getcwd() # cwd is 'Current Working Directory'
   print("Current Directory:", cwd)
   os.chdir('/path/to/new/directory') #chdir is 
   ```

   - cwd: current working directory
   - chdir: change current working directory

<br>

2. **Listing Directory Contents**:
   ```python
   entries = os.listdir('.')
   print(entries) 
   ```
   - `listdir`: list the files and folders in the specified directory
   - The `.` indicates to list files in the current working directory
   - Note. If your confused about the term directory, think of it has a folder instead

<br>

3. **Creating Directories**:
   ```python
   os.mkdir('new_directory')
   os.makedirs('nested/directory/structure')
   ```
   - `mkdir`: makes directory (folder)
   - `makedirs`: makes directory (folders/folder) at the specified path
<br>

4. **Renaming Files and Directories**:
   ```python
   os.rename('old_name', 'new_name')
   ```
   - `rename`: renames a file

<br>

5. **Deleting Files and Directories**:
   ```python
   os.remove('file_to_delete.txt')
   os.rmdir('empty_directory')
   ```

   - `remove`: deletes fil
   - `rmdir`: deletes directory (folder)


## 2. File Path Manipulation
Manipulate file paths, crucial for writing OS-agnostic code.

### Examples:
1. **Joining Paths**:
   ```python
   full_path = os.path.join('directory', 'subdirectory', 'file.txt')
   ```
   - `join` is used to concatenate various parts of a file path.
   - In `os.path.join('directory', 'subdirectory', 'file.txt')`, the method joins the strings 'directory', 'subdirectory', and 'file.txt' into a single path. The result is a path string like 'directory/subdirectory/file.txt' (or 'directory\subdirectory\file.txt' on Windows).

2. **Splitting Paths**:
   ```python
   path, filename = os.path.split('/path/to/file.txt')
   ```
   - `split` function splits a path into two parts: the directory path and the file name. It's useful for separating the file name from its directory path.
   - In `path, filename = os.path.split('/path/to/file.txt')`, the path '/path/to/file.txt' is split into '/path/to' (path) and 'file.txt' (filename).

   <br>

3. **Checking Path Validity**:
   ```python
   exists = os.path.exists('/path/to/check')
   is_file = os.path.isfile('/path/to/check')
   is_dir = os.path.isdir('/path/to/check')
   ```
   - `os.path.exists`: Checks if the path exists. It returns True if the path exists, whether it's a file or a directory.
   - `os.path.isfile`: Checks if the path is a file. Returns True only if the given path is a file.
   - `os.path.isdir`: Checks if the path is a directory. Returns True only if the given path is a directory.

<br>

4. **Splitting the Extension**:
   ```python
   root, ext = os.path.splitext('file.txt')
   ```
   - `splittext`: Splits a path into two parts: the path without the file extension and the file extension itself. This is useful when you need to work with file extensions, like filtering files by type or changing the extension.
   - In `root, ext = os.path.splitext('file.txt')`, the file name 'file.txt' is split into 'file' (root) and '.txt' (ext), where 'file' is the name of the file and '.txt' is the extension.


