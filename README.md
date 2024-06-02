# Sunday's Craziness
Experimental Pygame rhythm game. Also added so you can fix my terrible code.
Note: The game is in it's alpha and not working properly.

## How to compile
So normally you don't because python is an interpreter-based language, but
there is a way to compile the code to exe and this file will show how.

1. For python you have to install the version 3.12.3 which is the newest if I am correct.

2a. For windows you can go to the microsoft store and download python 3.12 and it should work with this if not use the method for other platforms.

2b. For other platforms go to the python site (https://www.python.org/downloads). The site should detect your os. If the newest version isn't 3.12.3 or at least any of the python 3.12 versions then hover over on the downloads tab and under the download latest version button you should see a text saying "View the full list of downloads" and click on it. Choose the 3.12.3 version and install it.

3. Click on the downloaded file in the file manager for whatever os you have and go through the download process. I recommend adding python to PATH.

4. Open any terminal you have on your os like Command Prompt on Windows and start downloading all the libraries:

Macos:
python3 -m ensurepip
python3 -m pip install pygame 2.5.2
python3 -m pip install pygame_gui 0.6.10
python3 -m pip install psutil 5.9.8
python3 -m pip install pyinstaller 6.6.0

Windows:
pip install pygame 2.5.2
pip install pygame_gui 0.6.10
pip install psutil 5.9.8
pip install pyinstaller 6.6.0

Linux:
Will update it later

5. Open your os terminal with the games directory and type:
pyinstaller --onefile (the file you chose because there is no main yet).py

If you understood everything and you've done it right, you can be happy with the partly compiled code!
