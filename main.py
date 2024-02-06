import os
import subprocess
import ctypes

temp_dirs = [
    r'C:\Windows\Temp',
    os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Temp')
]

for del_dir in temp_dirs:
    pObj = subprocess.Popen('del /S /Q /F "%s\\*.*"' % del_dir, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    rTup = pObj.communicate()
    rCod = pObj.returncode
    if rCod == 0:
        print(f"Cleaned {del_dir}")
    else:
        print(f"Couldn't clean {del_dir}")

try:
    ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 1)
    print("Recycle bin cleared.")
except Exception as e:
    print(f"Error clearing recycle bin: {e}")