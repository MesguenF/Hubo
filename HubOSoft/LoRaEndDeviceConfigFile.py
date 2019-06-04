#============================================================================//
# File ............: "LoRaEndDevConfigFile.py"
# Author ..........: MESGUEN Frederic
# Date ............: 04/03/19
#----------------------------------------------------------------------------//
# Description : To create a configuration of a End Device
#         
#============================================================================//
from collections import OrderedDict
import json
import os
import sys
import Files_Functions
from Files_Functions import *
from IHM import *
import IHM
from CONSTANTS import EMPTY_JSON_DICT_END_DEVICE_CONFIG_FILE


# CONSTANTS
JSON_PROV_OBJ_NAME = "LoRa_GW_Allowed_End_Dev_File"
JSON_GW_ALLOWED_END_DEVICE_TAB_NAME = "End_Device_Objects"
JSON_END_DEV_CONF_OBJ_NAME = "LoRa_End_Device_Config_File"
JSON_END_DEV_CONF_TAB_NAME = "Configuration_Frames"

EMPTY_JSON_NAME_END_DEVICE_CONFIGURATION = "c_0000_0000000000000000.json" #c_0000_70B3D5E75E004910

#Variable for DevEUI End Device
DevEUI=""

#To return DevEUI of End Device
def get_DevEUI_End_Device():
    return DevEUI 

# Get the GW configuration file and configuration file version
def get_EndDevice_config_file(server_directory, DevEUI):
    conf_file = sFGetCompleteFilenameDirectory(server_directory,"c_010")
               
    #If no config file then create the name of a empty config file
    if(conf_file == "ERROR"):
        conf_file = server_directory + EMPTY_JSON_NAME_GW_CONFIGURATION
        dict_in_json(server_directory, EMPTY_JSON_NAME_GW_CONFIGURATION, EMPTY_JSON_DICT_CONFIG_FILE)
         
    return conf_file

# Get the list of end-devices
# def get_list_EndDevice(prov_file):
#     end_dev_list = []
#     with open(prov_file, 'r') as jsonfile:
#         # Read the content of the json file
#         json_content = jsonfile.read()
#       
#     # Load the json as a json object 
#     parsed_json = json.loads(json_content, object_pairs_hook=OrderedDict)
#            
#     # Get the tab containing the device objects
#     devices_tabs_json = parsed_json[JSON_PROV_OBJ_NAME][JSON_GW_ALLOWED_END_DEVICE_TAB_NAME]
#            
#     # Get the list of end-devices
#     for device_object in devices_tabs_json:
#         end_dev_list.append(device_object["End_Device_ID"]["DevEUI"])
#      
#       
#     # Read  the list of end-devices
#     print( "\nEnd-devices found in provisionning file :" )
#     for end_dev in end_dev_list:
#         print(json.dumps(end_dev, indent=4))
#              
#     return parsed_json
    
####Add a end-device    
# def get_all_entry_and_create_JSON_GW_EndDeviceConfigFile():
#     print("DevEUI of the end-device to add ? (8 bytes)")
#     Dev_EUI = IHM.variable_ENDDeviceIDDevEUI_entry
#     # While loop to get all the payloads that the user wants to sent
#     ucFrameNb = 0
#     bKeepLooping = True
#     pSFramesToSend = []
#     while( ( ucFrameNb < 5 ) and bKeepLooping ):
#         # Get the payload
#         print("\nPayload to send to end-Device", Dev_EUI, "?")
#         SPayload = IHM.variable_MACInfoFrmPayload_entry
#         
#         # Get the FPort
#         print("\nFPort to used ?")
#         SFPort = IHM.variable_MACInfoFPort_entry
#         # Save inside the list
#         pSFramesToSend.append( {"FPort":int(SFPort), "FrmPayload":SPayload} )
#         
#         # Increment the counter
#         ucFrameNb = ucFrameNb + 1
#         
#         # Ask the user if he wants to send another frame (if less than 5 frames saved)
#         if( ucFrameNb < 5 ):
#             print("\nDo you want to send another frame ? (Y/N)")
#             SAnswer = input("\n>> ")
#             if( (SAnswer[0] == 'N') or (SAnswer[0] == 'n') ):
#                 bKeepLooping = False

       
####Add a end-device    
def get_all_entry_and_create_JSON_GW_EndDeviceConfigFile(server_directory):
      
    
    DevEUI = IHM.variable_ENDDeviceIDDevEUI_entry.get()
    # Create the JSON object that will allow to set the file
    new_json_object = OrderedDict()
    new_json_object[JSON_END_DEV_CONF_OBJ_NAME] = OrderedDict()
    new_json_object[JSON_END_DEV_CONF_OBJ_NAME]["Version"] = IHM.VersionLoRaEndDeviceConfigFile_entry.get()
    
    new_json_object[JSON_END_DEV_CONF_OBJ_NAME]["End_Device_ID"] = OrderedDict()
    new_json_object[JSON_END_DEV_CONF_OBJ_NAME]["End_Device_ID"]["DevEUI"] = DevEUI
               
    new_json_object[JSON_END_DEV_CONF_OBJ_NAME]["MAC_Info"] = OrderedDict()
    new_json_object[JSON_END_DEV_CONF_OBJ_NAME]["MAC_Info"]["FPort"] = IHM.variable_MACInfoFPort_entry.get()
    new_json_object[JSON_END_DEV_CONF_OBJ_NAME]["MAC_Info"]["FrmPayload"] = IHM.variable_MACInfoFrmPayload_entry.get()
    
    new_json_object[JSON_END_DEV_CONF_OBJ_NAME]["Alarm_Info"] = OrderedDict()
    new_json_object[JSON_END_DEV_CONF_OBJ_NAME]["Alarm_Info"]["Is_Alarm"] = IHM.variable_ALARMINFOIsAlarm_entry.get()
    new_json_object[JSON_END_DEV_CONF_OBJ_NAME]["Alarm_Info"]["Reg_Ex"] = IHM.variable_ALARMINFORegEx_entry.get()
    new_json_object[JSON_END_DEV_CONF_OBJ_NAME]["Alarm_Info"]["Act_On_Alarm"] = IHM.variable_ALARMINFOActOnAlarm_entry.get()
    
    #return new_json_object
    
    # Look if there is a existing configuration file for this end-device
    config_file = sFGetEndDevConfigFilename(server_directory, DevEUI)

    if( config_file != "" ):
        # A configuration file is already existing for this end_device, get the version
        print( "\nFound configuration file : ", config_file )
        version = int( config_file[(len(server_directory)+2):(len(server_directory)+6)] )
        print( "Version :", version )
    
        # Delete the found configuration file
        os.remove(config_file)
        
    else:
        version = 0
    
    new_config_file = "c_" + (str(version+1).zfill(4)) + "_" + get_DevEUI_End_Device() + ".json"
    new_config_file = ( server_directory + new_config_file )
    
    
    with open(new_config_file, 'w') as resultjsonfile:
        # Print the json object in a file
        json.dump(new_json_object, resultjsonfile, indent=4)
        
    print( "\nConfiguration file updated : ", new_config_file )
    
    #Delete the old file
    os.remove(config_file)
    
    # To test if a link_file exist
    link_file_name_directory = sFGetCompleteFilenameDirectory(server_directory,JSON_LINK_START_NAME)       
    
     #If no link file then create a empty link file json and name of a empty default link file
    if(link_file_name_directory == "ERROR"):
        print("Pas de fichier LINK FILE dans le dossier , CREATION D'UN LINK FILE")
        link_file_name =  JSON_LINK_START_NAME + DEFAULT_LINK_FILE_NAME + '.json'
        link_file_name_directory = server_directory + link_file_name
        data_dict = EMPTY_JSON_DICT_LINK_FILE
        dict_in_json(server_directory, link_file_name, data_dict)
    
    # Add the filename in the corresponding file
    vFUpdateLinkFile(server_directory, link_file_name_directory, config_file[-28:], new_config_file[-28:] )
           
    print( "Link file updated : ", server_directory + link_file_name )

# Create the name of the new configuration file
def create_name_EndDeviceConfig_File_Name(version, server_directory):
    new_config_file = "c_" + (str(version+1).zfill(4)) + "_" + get_DevEUI_End_Device() + ".json"
    new_config_file = ( server_directory + new_config_file )
    return new_config_file

#Write the new json object and delete the old file
def write_newJSON_delete_oldJSON_updateLinkFile_EndDeviceConf(new_config_file,new_json_object,conf_file,server_directory):
    with open(new_config_file, 'w') as resultjsonfile:
        # Print the json object in a file
        json.dump(new_json_object, resultjsonfile, indent=4)
        
    print( "\nConfiguration file updated : ", new_config_file )
    
    #Delete the old file
    os.remove(conf_file)
    
    # To test if a link_file exist
    link_file_name_directory = sFGetCompleteFilenameDirectory(server_directory,JSON_LINK_START_NAME)       
    
     #If no link file then create a empty link file json and name of a empty default link file
    if(link_file_name_directory == "ERROR"):
        print("Pas de fichier LINK FILE dans le dossier , CREATION D'UN LINK FILE")
        link_file_name =  JSON_LINK_START_NAME + DEFAULT_LINK_FILE_NAME + '.json'
        link_file_name_directory = server_directory + link_file_name
        data_dict = EMPTY_JSON_DICT_LINK_FILE
        dict_in_json(server_directory, link_file_name, data_dict)
    
    # Add the filename in the corresponding file
    vFUpdateLinkFile(server_directory, link_file_name_directory, config_file[-28:], new_config_file[-28:] )
           
    print( "Link file updated : ", server_directory + link_file_name )
# Look if there is a existing configuration file for this end-device
def test_if_existing_config_file(server_directory):
    config_file = sFGetEndDevConfigFilename(server_directory, get_DevEUI_End_Device())
    
    if( config_file != "" ):
         # A configuration file is already existing for this end_device, get the version
        print( "\nFound configuration file : ", config_file )
        # Delete the found configuration file
        os.remove(config_file)
    else:
        conf_file = server_directory + EMPTY_JSON_NAME_END_DEVICE_CONFIGURATION
        dict_in_json(server_directory, EMPTY_JSON_NAME_END_DEVICE_CONFIGURATION, EMPTY_JSON_DICT_END_DEVICE_CONFIG_FILE)
            
    return config_file 
   
# Get the version of config_file 
def get_Version_Config_File(config_file, server_directory):
    version = int( config_file[(len(server_directory)+2):(len(server_directory)+6)] )
    return version