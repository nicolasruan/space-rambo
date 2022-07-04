import cx_Freeze

import os
os.environ['TCL_LIBRARY'] = "C:\\Program Files (x86)\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Program Files (x86)\\Python35-32\\tcl\\tk8.6"

executables  = [cx_Freeze.Executable("GAME.py")]
cx_Freeze.setup(
    name = "Space Rambo",
    options = {"build_exe": {"packages":["pygame", "numpy", "main", "constants","ui"], "include_files":["reload.wav", "gong.wav", "gunshot.wav", "explosion.wav", "enemy_dead.wav", "laugh.wav", "throw_bomb.wav", "soundtrack.wav"]}},
    description = "Space Rambo",
     executables = executables,
    version="22.99"
               )
