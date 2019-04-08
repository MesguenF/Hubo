#============================================================================//
# File ............: "LoRaEndDevConfigFile.py"
# Author ..........: Frédéric MESGUEN
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
import IHM
from Files_Functions import *
from IHM import *

# CONSTANTS
JSON_PROV_OBJ_NAME = "LoRa_GW_Allowed_End_Dev_File"
JSON_PROV_TAB_NAME = "End_Device_Objects"
JSON_END_DEV_CONF_OBJ_NAME = "LoRa_End_Device_Config_File"
JSON_END_DEV_CONF_TAB_NAME = "Configuration_Frames"
link_file_name = "corresp_file.json"
    
# Get the provisionning file
def get_prov_file(server_directory):
    prov_file = sFGetCompleteFilenameDirectory(server_directory , "p_" )
    print("\nFound provisionning file : ", prov_file)
    return prov_file
            
# Get the list of end-devices
def get_list_EndDevice(prov_file):
    end_dev_list = []
    with open(prov_file, 'r') as jsonfile:
        # Read the content of the json file
        json_content = jsonfile.read()
    
    # Load the json as a json object 
    parsed_json = json.loads(json_content, object_pairs_hook=OrderedDict)
         
    # Get the tab containing the device objects
    devices_tabs_json = parsed_json[JSON_PROV_OBJ_NAME][JSON_PROV_TAB_NAME]
         
    # Get the list of end-devices
    for device_object in devices_tabs_json:
        end_dev_list.append(device_object["End_Device_ID"]["DevEUI"])
    
    # Read  the list of end-devices
    for end_dev in end_dev_list:
        print(json.dumps(end_dev, indent=4))
            
    return parsed_json
    print( "\nEnd-devices found in provisionning file :" )
    print( "------------------------------------------" )
    
    
# ####Select a end-device
# print("DevEUI of the end-device to send frame(s) to ? (8 bytes)")
# Dev_EUI = ""   #IHM.variable_ENDDeviceIDDevEUI_entry
#       
# # While loop to get all the payloads that the user wants to sent
# ucFrameNb = 0
# bKeepLooping = True
# pSFramesToSend = []
# while( ( ucFrameNb < 5 ) and bKeepLooping ):
#     # Get the payload
#     print("\nPayload to send to end-Device", Dev_EUI, "?")
#     SPayload = IHM.variable_MACInfoFrmPayload_entry
#           
#     # Get the FPort
#     print("\nFPort to used ?")
#     SFPort = IHM.variable_MACInfoFPort_entry
#           
#     # Save inside the list
#     pSFramesToSend.append( {"FPort":int(SFPort), "FrmPayload":SPayload} )
#           
#     # Increment the counter
#     ucFrameNb = ucFrameNb + 1
#           
#     # Ask the user if he wants to send another frame (if less than 5 frames saved)
#     if( ucFrameNb < 5 ):
#         print("\nDo you want to send another frame ? (Y/N)")
#         SAnswer = input("\n>> ")
#         if( (SAnswer[0] == 'N') or (SAnswer[0] == 'n') ):
#             bKeepLooping = False
#                   
# # Look if there is a existing configuration file for this end-device
# config_file = sFGetEndDevConfigFilename(IHM.DIR_NAME_CONFIG, Dev_EUI)
#   
# if( config_file != "" ):
#     # A configuration file is already existing for this end_device, get the version
#     print( "\nFound configuration file : ", config_file )
#     version = int( config_file[(len(IHM.DIR_NAME_CONFIG)+1+2):(len(IHM.DIR_NAME_CONFIG)+1+6)] )
#     print( "Version :", version )
#       
#     # Delete the found configuration file
#     os.remove(config_file)
#           
# else:
#     version = 0
#       
# # Create the JSON object that will allow to set the file
# new_json_object = OrderedDict()
# new_json_object[JSON_END_DEV_CONF_OBJ_NAME] = OrderedDict()
# new_json_object[JSON_END_DEV_CONF_OBJ_NAME]["Version"] = IHM.VersionLoRaEndDeviceConfigFile_entry
# new_json_object[JSON_END_DEV_CONF_OBJ_NAME]["End_Device_ID"] = OrderedDict()
# new_json_object[JSON_END_DEV_CONF_OBJ_NAME]["End_Device_ID"]["DevEUI"] = Dev_EUI
# new_json_object[JSON_END_DEV_CONF_OBJ_NAME][JSON_END_DEV_CONF_TAB_NAME] = []
#       
# for frame in pSFramesToSend:
#     tmp_json_object = OrderedDict()
#     tmp_json_object["MAC_Info"] = OrderedDict()
#     tmp_json_object["MAC_Info"]["FPort"] = frame["FPort"]
#     tmp_json_object["MAC_Info"]["FrmPayload"] = frame["FrmPayload"]
#     new_json_object[JSON_END_DEV_CONF_OBJ_NAME][JSON_END_DEV_CONF_TAB_NAME].append(tmp_json_object)
#   
# new_json_object[JSON_END_DEV_CONF_OBJ_NAME]["Alarm_Info"] = OrderedDict()
# new_json_object[JSON_END_DEV_CONF_OBJ_NAME]["Alarm_Info"]["Is_Alarm"] = IHM.variable_ALARMINFOIsAlarm_entry
# new_json_object[JSON_END_DEV_CONF_OBJ_NAME]["Alarm_Info"]["Reg_Ex"] = IHM.variable_ALARMINFORegEx_entry
# new_json_object[JSON_END_DEV_CONF_OBJ_NAME]["Alarm_Info"]["Act_On_Alarm"] = IHM.variable_ALARMINFOActOnAlarm_entry
#       
# # Create the name of the new configuration file
# new_config_file = "c_" + (str(version+1).zfill(4)) + "_" + Dev_EUI + ".json"
# new_config_file = ( IHM.DIR_NAME_CONFIG + "\\" + new_config_file )
#       
# with open(new_config_file, 'w') as resultjsonfile:
#     # Print the json object in a file
#     json.dump(new_json_object, resultjsonfile, indent=4)
#       
# print( "\nConfiguration file updated : ", new_config_file )
#       
# # # Add the filename in the corresponding file
# # if( config_file != ""):
# #     vFUpdateLinkFile( IHM.DIR_NAME_CONFIG, link_file_name, config_file[-28:], new_config_file[-28:] )
# # else:
# #     vFUpdateLinkFile( IHM.DIR_NAME_CONFIG, link_file_name, new_config_file[-28:], new_config_file[-28:] )
# #       
# # print( "Link file updated : ", IHM.DIR_NAME_CONFIG + "\\" + link_file_name )
#     
#     