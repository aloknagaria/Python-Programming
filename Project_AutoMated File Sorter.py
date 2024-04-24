import os, shutil
path = r"C:/Users/Dell/Desktop/Automated File Sorter/"
file_name = os.listdir(path)
# print(file_name)
folder_name = ['png files', 'csv files', 'txt files']
for i in range(0,3):
    if not os.path.exists(path + folder_name[i]):
        print(path + folder_name[i])
        os.makedirs(path+folder_name[i])

for file in file_name:
    if ".png" in file and not os.path.exists(path + "png files/"+file):
        shutil.move(path + file, path + "png files/" + file)
    else:
        print("invalid input")