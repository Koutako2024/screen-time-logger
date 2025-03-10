# Start Developping
1. `git clone git@github.com:Koutako2024/screen-time-logger.git`
2. `.\.venv\Scripts\Activate.ps1`
3. `pip install -r requirements.txt`

# Build
1. `pyinstaller -w -F --clean --hidden-import plyer.platforms.win.notification rest_window.py`
2. `pyinstaller -w --clean --hidden-import plyer.platforms.win.notification main.py`
3. move rest_window.exe, main.exe, and _internal directory to .