import shutil 

# copy file.txt to destination 
shutil.copy('C:\\User\\Name\\file.txt', 'C:\\User\\Name\\destination')

# copy and rename file.txt to destination 
shutil.copy('C:\\User\\Name\\file.txt', 'C:\\User\\Name\\destination\\spam.txt')

# copy folder and its contents 
shutil.copytree('C:\\User\\Name\\original_folder', 'C:\\User\\Name\\original_folder_backup')

# move file 
shutil.move('C:\\User\\Name\\destination\\file.txt', 'C:\\User\\Name\\new_destination\\file.txt')

# rename file without moving it 
shutil.move('C:\\User\\Name\\destination\\file.txt', 'C:\\User\\Name\\destination\\new_name.txt')

# delete file 
os.unlink('file.txt')

# delete directory - directory has to be empty
os.rmdir('C:\\User\Marco\\folder_name')

# delete directory and everything inside of it
shutil.rmtree('C:\\User\Marco\\folder_name')