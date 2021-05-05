# rdworks_hack
Automaticly approving RDWorks dialogs when uploading a file to the laser cut machine.

#### [optional] Create python environment
	python -m venv env
	.\env\Scripts\Activate.ps1

#### Install python packages
	pip install pywinauto auto-py-to-exe

#### Convert script to executable
	pyinstaller --noconfirm --onedir --windowed C:\rdworks_hack\rdworks_hack.py
	# or auto-py-to-exe
	auto-py-to-exe
	settings -> import conf -> auto_py_to_exe.json
	click on convert py to exe

#### [optional] Set to run as admin (for makelab's PC that seems to run RDWorks as admin..)
	right click on -> C:\rdworks_hack\output\rdworks_hack\rdworks_hack.exe -> Properties -> run_as_administrator

#### auto start program
	create a shortcut of rdworks_hack.vbs in %AppData%\Microsoft\Windows\Start Menu\Programs\Startup

## Enjoy!
A.E.TECH
