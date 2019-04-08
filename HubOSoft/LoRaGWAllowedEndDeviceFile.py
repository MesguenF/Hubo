#============================================================================//
# File ............: "LoRaGWAllowedEndDevFile.py"
# Author ..........: Frédéric MESGUEN
# Date ............: 04/03/19
#----------------------------------------------------------------------------//
# Description : To create a list of End Device allowed
#         
#============================================================================//
from collections import OrderedDict
import json
import os
import sys    
from Files_Functions import *
import Files_Functions
import IHM
from IHM import *

# CONSTANTS
JSON_GW_CONF_OBJ_NAME = "LoRa_GW_Allowed_End_Dev_File"
JSON_PROV_TAB_NAME = "End_Device_Objects"
link_file_name = "corresp_file.json"
    
# Get the provisionning file and the provisionning file version
def get_AllowedEndDevice_File(directory):
    conf_file = sFGetCompleteFilenameDirectory(directory, "p_" )
    print( "\nFound provisionning file : ", conf_file )
    return conf_file

# Get the Allowed EndDevice file version
def get_AllowedEndDevice_File_version(conf_file, directory):
    version = int( conf_file[(len(directory)+1+6):(len(directory)+1+10)] )
    print( "Version :", version )
    return version

# Get the list of end-devices
def get_list_EndDevice(conf_file):
    end_dev_list =  []
    with open(conf_file, 'r') as jsonfile:
        # Read the content of the json file
        json_content = jsonfile.read()
    # Load the json as a json object 
    parsed_json = json.loads(json_content, object_pairs_hook=OrderedDict)
    # Get the tab containing the device objects
    devices_tabs_json = parsed_json[JSON_GW_CONF_OBJ_NAME][JSON_PROV_TAB_NAME]
    # Get the list of end-devices
    for device_object in devices_tabs_json:
        end_dev_list.append(device_object["End_Device_ID"]["DevEUI"])
    # Read  the list of end-devices
    for end_dev in end_dev_list:
        print(json.dumps(end_dev, indent=4))
    
    return parsed_json
   
#Get all entry and Prepare the json object 
def get_all_entry_and_create_JSON():
    Dev_EUI = IHM.variable_ENDDeviceIDDevEUI_entry
    Dev_Addr = IHM.variable_ENDDeviceIDDevAddr_entry
    Class = IHM.variable_ASSOSInfosClass_entry 
    Asso_type = IHM.ASSOSInfosActivationMode_entry
  
    #####################################################
    if (IHM.variable_OTA_Checkbutton.get() == 1) :
        print(IHM.variable_OTA_Checkbutton.get())
        isOTAA = True
    else:
        print(IHM.variable_OTA_Checkbutton.get())
        isOTAA = False
    #####################################################
    
    if( isOTAA ):
    # OTAA managed
        App_EUI = IHM.variable_OTAFieldsAppEUI_entry  
        AppKey = IHM.variable_OTAFieldsAppKey_entry    
        print("DevEUI :", Dev_EUI)
        print("DevAddr :", Dev_Addr)
        print("Class :", Class)
        print("AppEUI :", App_EUI)
        print("AppKey :", AppKey)
    else:
    # ABP managed
        Nwk_S_Key = IHM.variable_ABPFieldsNwkSKey_entry  
        App_S_Key = IHM.variable_ABPFieldsAppSKey_entry   
        print("DevEUI :", Dev_EUI)
        print("DevAddr :", Dev_Addr)
        print("Class :", Class)
        print("NwkSKey :", Nwk_S_Key)
        print("AppSKey :", App_S_Key)
        
    #Prepare the json object
    new_json_object = OrderedDict()
        
    new_json_object["End_Device_ID"] = OrderedDict()
    new_json_object["End_Device_ID"]["DevEUI"] = Dev_EUI
    new_json_object["End_Device_ID"]["DevAddr"] = Dev_Addr
        
    new_json_object["Asso_Infos"] = OrderedDict()
        
    if(isOTAA):
        new_json_object["Asso_Infos"]["Activation_Mode"] = "OTA"
    else:
        new_json_object["Asso_Infos"]["Activation_Mode"] = "ABP"
        
    new_json_object["Asso_Infos"]["Class"] = Class
        
    if(isOTAA):
        # Create the sub-object for OTAA uniquely
        new_json_object["OTA_Fields"] = OrderedDict()
        new_json_object["OTA_Fields"]["AppEUI"] = App_EUI
        new_json_object["OTA_Fields"]["AppKey"] = AppKey
    else:
        # Create the sub-object for ABP uniquely
        new_json_object["ABP_Fields"] = OrderedDict()
        new_json_object["ABP_Fields"]["NwkSKey"] = Nwk_S_Key
        new_json_object["ABP_Fields"]["AppSKey"] = App_S_Key
    
    return new_json_object
        
# Add the json object
def add_json_object(parsed_json, new_json_object):
    parsed_json[JSON_GW_CONF_OBJ_NAME][JSON_PROV_TAB_NAME].append(new_json_object)
        
# Create the name of the new provisionning file
def create_name_AllowedEndDevice_File_Name(version, server_directory):
    new_prov_file = "p_010_" + (str(version+1).zfill(4)) + ".json"
    new_prov_file = (server_directory  + "\\" + new_prov_file )
    return new_prov_file

#Write the new json object and delete the old file
def write_newJSON_delete_oldJSON_updateLinkFile(new_prov_file,parsed_json,conf_file,server_directory):
    with open(new_prov_file, 'w') as resultjsonfile:
        # Print the json object in a file
        json.dump(parsed_json, resultjsonfile, indent=4)
            
    # Delete the old file
    os.remove(conf_file)
        
    print( "\nProvisionning file updated : ", new_prov_file )
        
#     # Add the filename in the corresponding file
#     vFUpdateLinkFile(server_directory, link_file_name, conf_file[-15:], new_prov_file[-15:] )
#         
#     print( "Link file updated : ", server_directory + "\\" + link_file_name )
    
###############################################