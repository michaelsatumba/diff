import os

folder1 = '/Users/michaelsatumba/Desktop/13195-dev'
folder2 = '/Users/michaelsatumba/Desktop/13195'

files1 = set(os.listdir(folder1))
files2 = set(os.listdir(folder2))

missing_in_folder1 = files2 - files1
missing_in_folder2 = files1 - files2

print("Files missing in", folder1, ":", missing_in_folder1)
print("Files missing in", folder2, ":", missing_in_folder2)
