#============================================================================//
# File ............: "setup.py"
# Author ..........: MESGUEN Frédéric
# Date ............: 27/03/19
#----------------------------------------------------------------------------//
#============================================================================//
from cx_Freeze import setup, Executable
import os
from tkinter.tix import *
 
os.environ['TCL_LIBRARY'] ="C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python37-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] ="C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python37-32\\tcl\\tk8.6"
os.environ['TK_LIBRARY'] ="C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python37-32\\tcl\\tix8.4.3"

setup(
    name = "Hubo",
    version = "0.1",
    description = "Programme de configuration HubO Lorawan",
    executables = [Executable("controller.py")]
)
