# import os

# # This is a Python script that demonstrates how to use the os module

# # os.mkdir('nidal')  # Create a new directory named 'new_directory'
# # print(os.listdir('nidal'))  # List all files and directories in the current directory
# os.getcwd()  # Get the current working directory

# os.rename("nidal", "nidakhan")





# .

# 🧠 os Module: Overview
# ✅ To use it:
# python
# Copy
# Edit
# import os
# 🔹 Common os Module Functions
# 1. Get Current Working Directory
# python
# Copy
# Edit
# print(os.getcwd())  # shows where your Python script is running
# 2. List Files in a Directory
# python
# Copy
# Edit
# print(os.listdir())  # lists files and folders in current directory
# print(os.listdir('/path/to/dir'))  # specify directory
# 3. Create a Folder
# python
# Copy
# Edit
# os.mkdir("new_folder")
# 4. Create Nested Folders
# python
# Copy
# Edit
# os.makedirs("parent/child/grandchild")
# 5. Rename a File or Folder
# python
# Copy
# Edit
# os.rename("old_name.txt", "new_name.txt")
# 6. Remove Files and Folders
# python
# Copy
# Edit
# os.remove("file.txt")       # remove a file
# os.rmdir("empty_folder")    # remove an empty folder
# os.removedirs("a/b/c")      # remove nested empty folders
# 7. Check if File or Folder Exists
# python
# Copy
# Edit
# os.path.exists("file.txt")
# 8. Join Paths
# python
# Copy
# Edit
# path = os.path.join("folder", "file.txt")
# print(path)  # folder/file.txt
# 🧪 Example: Working with Files and Directories
# python
# Copy
# Edit
# import os

# # Get current directory
# print("Current directory:", os.getcwd())

# # Create a new folder
# if not os.path.exists("test_folder"):
#     os.mkdir("test_folder")
#     print("Folder created!")

# # Rename it
# os.rename("test_folder", "my_folder")

# # List all files
# print("Files in directory:", os.listdir())

# # Remove folder
# os.rmdir("my_folder")
# print("Folder removed!")
# ✅ When to Use the os Module
# Creating or navigating folders in a script.

# Automating file handling.

# Building CLI tools or scripts that need file system access.

# Managing environment variables (os.environ).

