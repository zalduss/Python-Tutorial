
# Python os Library Tutorial

## Introduction
The `os` library in Python provides a way to use operating system dependent functionalities. It's essential for file and directory operations, process management, and working with environment variables. This tutorial offers an in-depth exploration of key features with examples.

## 1. File and Directory Management
Interact with the file system for operations like creating, renaming, moving, and deleting files and directories.

### Examples:
1. **Navigating the File System**:
   ```python
   import os
   cwd = os.getcwd()
   print("Current Directory:", cwd)
   os.chdir('/path/to/new/directory')
   ```

2. **Listing Directory Contents**:
   ```python
   entries = os.listdir('.')
   print(entries)
   ```

3. **Creating Directories**:
   ```python
   os.mkdir('new_directory')
   os.makedirs('nested/directory/structure')
   ```

4. **Renaming Files and Directories**:
   ```python
   os.rename('old_name', 'new_name')
   ```

5. **Deleting Files and Directories**:
   ```python
   os.remove('file_to_delete.txt')
   os.rmdir('empty_directory')
   import shutil
   shutil.rmtree('directory_to_delete')
   ```

## 2. Environment Variables
Work with key-value pairs that can affect the behavior of running processes.

### Examples:
1. **Accessing an Environment Variable**:
   ```python
   user = os.environ.get('USER')
   print(user)
   ```

2. **Setting Environment Variables**:
   ```python
   os.environ['NEW_VAR'] = 'value'
   ```

3. **Modifying the PATH Variable**:
   ```python
   os.environ['PATH'] += os.pathsep + '/path/to/directory'
   ```

4. **Enumerating All Environment Variables**:
   ```python
   for key, value in os.environ.items():
       print(key, '=', value)
   ```

5. **Using Environment Variables in Script**:
   ```python
   debug_mode = os.environ.get('DEBUG_MODE', False)
   ```

## 3. File Path Manipulation
Manipulate file paths, crucial for writing OS-agnostic code.

### Examples:
1. **Joining Paths**:
   ```python
   full_path = os.path.join('directory', 'subdirectory', 'file.txt')
   ```

2. **Splitting Paths**:
   ```python
   path, filename = os.path.split('/path/to/file.txt')
   ```

3. **Checking Path Validity**:
   ```python
   exists = os.path.exists('/path/to/check')
   is_file = os.path.isfile('/path/to/check')
   is_dir = os.path.isdir('/path/to/check')
   ```

4. **Getting Absolute Path**:
   ```python
   absolute_path = os.path.abspath('relative/path')
   ```

5. **Splitting the Extension**:
   ```python
   root, ext = os.path.splitext('file.txt')
   ```

## 4. Process Management
Start and manage processes, and get information about them.

### Examples:
1. **Starting a New Process**:
   ```python
   os.system('python script.py')
   ```

2. **Getting the Current Process ID**:
   ```python
   pid = os.getpid()
   ```

3. **Getting the Parent Process ID**:
   ```python
   ppid = os.getppid()
   ```

4. **Creating a Child Process**:
   ```python
   # Unix/Linux only
   pid = os.fork()
   ```

## Conclusion
The `os` library is a fundamental part of Python programming, especially when dealing with file and directory operations, process management, and environment variables. The examples provided here give a glimpse into its capabilities and use cases.

