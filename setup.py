import os
import config
import shutil

os.system('pyinstaller project.py')
path = config.PROGRAMPATH
os.chdir(path)
os.system(f'MOVE /Y {config.PROGRAMPATH}\dist\project\*.* {config.PROGRAMPATH}')
shutil.move(f'{path}/dist/project/certifi', f'{path}', copy_function = shutil.copytree)
shutil.move(f'{path}/dist/project/Include', f'{path}', copy_function = shutil.copytree)
shutil.move(f'{path}/dist/project/lib2to3', f'{path}', copy_function = shutil.copytree)
shutil.move(f'{path}/dist/project/tcl', f'{path}', copy_function = shutil.copytree)
shutil.move(f'{path}/dist/project/tk', f'{path}', copy_function = shutil.copytree)
shutil.move(f'{path}/dist/project/wrapt', f'{path}', copy_function = shutil.copytree)
shutil.rmtree(f'{path}/dist')
shutil.rmtree(f'{path}/build')
shutil.rmtree(f'{path}/__pycache__')

