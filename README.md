# CRO_Roadbook_QT

The repo is about developing a GUI for digital roads.

## QT Designer
With the QT Designer Software https://build-system.fman.io/qt-designer-download it is easy to develop a GUI for any needs.
Just download latest version and start a new project.

### Convert .ui to .py with anaconda prompt
1. Open anaconda prompt
2. Change to current folder with: cd C:\Users\ll_stsekeid\Desktop\CRO_Roadbook_QT
3. Insert: pyuic5 -x qtdesigner.ui -o qtdesigner.py
4. In your directory there is a new file qtdesigner.py
5. Execute qtdesigner.py in Spyder
![firstGUI](/img/firstGUI.jpeg)

### First Photo on GUI
1. Take the existing label and choose a image in the row pixmap
2. For example hochschulekempten.jpeg
3. Current GUI
![photo](/img/firstPhotoGUI.jpeg)


### Add second window
1. Create new OtherWindow.py file
2. Create a main_window.py file to manage the two windows
3. Execute the main_window.py to see the current firstGUI
![photo](/img/MainWindow.JPG)
![photo](/img/OtherWindow.JPG)


### Add third window
1. Create new A7S_window.py file
2. define new class in main_window.py file
3. Execute the main_window.py to see the current firstGUI
![photo](/img/ManagingThreeWindows.JPG)


### Include HTML Map
1. Updating A7_window.py file
2. Execute the main_window.py to see the current firstGUI
![photo](/img/IncludeHTML.JPG)
