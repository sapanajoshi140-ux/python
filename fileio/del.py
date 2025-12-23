import os

old_name = "file.txt"          # existing file name
new_name = "renamed_by_python.txt" # new file name

os.rename(old_name, new_name)

print("File renamed successfully!")
