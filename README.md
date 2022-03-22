# nameChanger
A project of an app used to change many file names at once.  

Existing features:
-Changing file names in a specific path, to base name with number (counting from zero/one, and brackets around the number selectable),  
-Changing file extensions in a specific path,  
-Config file with settings such as: file renaming/extension changer mode, brackets mode, counting mode,  
-Can handle "file already exist" error*  
  
  
List of planned features:  
-Renaming a list of files, with a name + number/letter. Sorting by date of creation, size, alfabetical.  
-Changing extensions of files.  
-Renaming part of a file's name.  
-Working on files in a specified folder, selected files in specific location, files drag and dropped to the app (creating a new folder in a specified location)  
-Also supporting working on folder names.  


*If a some of the files already uses basename+number syntax, standard os.rename method faced this error. My resolution is putting colliding files in a temporary directory.
