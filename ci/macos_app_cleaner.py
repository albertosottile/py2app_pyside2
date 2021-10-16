import os
import zipfile

PATH = 'dist/Test.app/Contents/Resources/lib'

zin = zipfile.ZipFile(f'{PATH}/python39.zip', 'r')
tbd = [path for path in zin.namelist() if 'PySide2/Qt/' in path]

zout = zipfile.ZipFile(f'{PATH}/python39_new.zip', 'w', zipfile.ZIP_DEFLATED)

for item in zin.namelist():
    buffer = zin.read(item)
    if item not in tbd:
        zout.writestr(item, buffer)

zout.close()
zin.close()

os.remove(f'{PATH}/python39.zip')
os.rename(f'{PATH}/python39_new.zip', f'{PATH}/python39.zip')
