# nameChanger

Author: WojciechSzade  

A project of an app used to change many file names at once.  

Existing features:  
-Changing file names in a specific path, to base name with number (counting from zero/one, and brackets around the number selectable), sorted by date of creation/size/alphabetical/alphabetical by file extension/reversed of any,  
-Changing file extensions in a specific path,  
-Config file with settings such as: file renaming/extension changer mode, brackets mode, counting mode and more,  
-Can handle "file already exist" error*,  
-Changing extensions of files,  
-Selecting directory to work on by dialog window.
  
List of planned features:  
-Renaming part of a file's name.  
-Working on files in a specified folder, selected files in specific location, files drag and dropped to the app (creating a new folder in a specified location)  
-Also supporting working on folder names.  
-GUI for the whole program


*If a some of the files already uses basename+number syntax, standard os.rename method faced this error. My resolution is putting colliding files in a temporary directory.
