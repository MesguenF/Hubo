#============================================================================//
# File ............: "setup.py"
# Author ..........: MESGUEN Frédéric
# Date ............: 27/03/19
#----------------------------------------------------------------------------//
#============================================================================//
from cx_Freeze import setup, Executable
import os

 
os.environ['TCL_LIBRARY'] ="C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python37-32\\DLLs\\tcl86t.dll"
os.environ['TK_LIBRARY'] ="C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python37-32\\DLLs\\tk86t.dll"

setup(
    name = "Hubo",
    version = "0.1",
    description = "Programme de configuration HubO Lorawan",
    executables = [Executable("controller.py")]
)
