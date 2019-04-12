#============================================================================//
# File ............: "LoRaLinkFile.py"
# Author ..........: MESGUEN F
# Date ............: 04/03/19
#----------------------------------------------------------------------------//
#============================================================================//
from cx_Freeze import setup, Executable

setup(
    name = "Hubo",
    version = "0.1",
    description = "Programme de configuration HubO Lorawan",
    executables = [Executable("controller.py")]
)