from cx_Freeze import setup, Executable
import os
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
base = None

executables = [Executable("Turtle_Race.py", base=base)]

packages = ["idna","random","turtle"]
options = {
    'build_exe': {
        'packages':packages,
        'include_files':[
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
         ],
    },
}

setup(
    name = "Turtle_Race",
    options = options,
    version = "1.0",
    description = 'Race between some Turtle Friends.',
    executables = executables
)
