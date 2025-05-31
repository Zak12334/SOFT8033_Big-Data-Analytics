import os

path = "D:/G Downlaods/A02/FileStore/tables/my_dataset_1"

print("Path exists:", os.path.exists(path))

if os.path.exists(path):
    print("Files inside:")
    for file in os.listdir(path):
        print(file)
