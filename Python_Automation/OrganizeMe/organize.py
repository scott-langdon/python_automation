import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png'],
    "PHOTOSHOP": ['.svg']
}

''' 
Note: This function returns a category based off the file suffix
'''
def pickDirectory(value): 
    for category, suffixes in SUBDIRECTORIES.items(): # Loops through all items in the dict
        for suffix in suffixes: 
            if suffix == value: 
                return category
    return 'MISC'
# print(pickDirectory('.pdf'))

''' 
Note: This function collects all the files in the directory and then files them in their proper folders ... it will not move a file to another dir if it is incorrect, that is the next thing it needs...
'''
def organizeDirectory():
    for item in os.scandir(): # collects all the files in the directory
        if item.is_dir(): # if item is the directory it skips it 
            continue
        filePath = Path(item) 
        filetype = filePath.suffix.lower()
        directory = pickDirectory(filetype)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True: # if dir not exist, then creat new dir w/ name
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath)) # moves file in the correct dir
        
organizeDirectory()