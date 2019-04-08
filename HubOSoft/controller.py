#============================================================================//
# File ............: "Controller.py"
# Author ..........: Frédéric MESGUEN
# Date ............: 04/03/19
#----------------------------------------------------------------------------//
# Description :
#         
#============================================================================//
# import LoRaEndDeviceConfigFile
# import LoRaGWAllowedEndDeviceFile
# import LoRaGWConfigurationFile
from collections import OrderedDict
import json
import os
from IHM import *
import IHM


boolLoopEvenement = False

if __name__ == '__main__':
           
    while(boolLoopEvenement == False):
        mainWindow.mainloop()
        server_config_directory = get_dir_name_config()
        server_data_directory = get_dir_name_data()
        
        
        print("Affichage du controller")
        print("Le dossier pour la configuration est  le suivant : " + server_config_directory)
        print("Le dossier de reception des données est  le suivant : " + server_data_directory)
        
        
        boolLoopEvenement = True