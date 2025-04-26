import os
import shutil

source = '/mnt/c/Users/samlo/Downloads'

destination = '/mnt/c/Users/samlo/OneDrive/Desktop/files'

dir_list = os.listdir(source)
folder_paths = {}
for file in dir_list:
    reverse_file = file[::-1]
    result = ''
    j = 0
    for char in reverse_file:
        if char != '.' and j < 6 and char.isalpha():
            result += char
        elif j > 6:
            break    
        elif char == '.' and j < 6 and len(result) > 1:
            if result[::-1] not in folder_paths:
                folder_paths[result[::-1]] = [f'{source}/{file}']
            else:
                folder_paths[result[::-1]].append(f'{source}/{file}')    
            break  
        j += 1    

for k,v in folder_paths.items():
    for files in v:
        if os.path.exists(f'{destination}/{k}-folder'):
            current = f'{destination}/{k}-folder'
            shutil.move(files, current)
        else:
            full_path = os.path.join(destination, f'{k}-folder')    
            os.makedirs(full_path, exist_ok=True)
            current = f'{destination}/{k}-folder'
            shutil.move(files, current)

