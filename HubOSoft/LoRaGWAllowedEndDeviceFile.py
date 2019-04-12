#============================================================================//
# File ............: "LoRaGWAllowedEndDevFile.py"
# Author ..........: MESGUEN F
# Date ............: 04/03/19
#----------------------------------------------------------------------------//
# Description : To create a list of End Device allowed
#         
#============================================================================//
from Files_Functions import *
import IHM
from LoRaLinkFile import EMPTY_JSON_DICT_LINK_FILE, DEFAULT_LINK_FILE_NAME, JSON_LINK_START_NAME
from CONSTANTS import EMPTY_JSON_DICT_ALLOWEDENDEVICE_FILE

# CONSTANTS
JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME = "LoRa_GW_Allowed_End_Dev_File"
JSON_GW_ALLOWED_END_DEVICE_TAB_NAME = "End_Device_Objects"
EMPTY_JSON_NAME_GW_ALLOWEDENDDEVICE = "P_010_0000.json"

    
# Get the provisionning file and the provisionning file version
def get_AllowedEndDevice_File(server_directory):
    prov_file = sFGetCompleteFilenameDirectory(server_directory, "p_010" )
    print("\nFound provisionning file : ", prov_file )
      
    #If no config file then create the name of a empty config file
    if(prov_file == "ERROR"):
        prov_file = server_directory + EMPTY_JSON_NAME_GW_ALLOWEDENDDEVICE
        dict_in_json(server_directory, EMPTY_JSON_NAME_GW_ALLOWEDENDDEVICE, EMPTY_JSON_DICT_ALLOWEDENDEVICE_FILE)
    print( "\nFound provisionning file : ", prov_file )    
    return prov_file

# Get the Allowed EndDevice file version
def get_AllowedEndDevice_File_version(prov_file, server_directory):
    version = int( prov_file[(len(server_directory)+6):(len(server_directory)+10)] )
    print( "Version :", version )
    return version

# Get the list of end-devices
def get_list_EndDevice(prov_file):
    end_dev_list =  []
    with open(prov_file, 'r') as jsonfile:
        # Read the content of the json file
        json_content = jsonfile.read()
    # Load the json as a json object 
    parsed_json = json.loads(json_content, object_pairs_hook=OrderedDict)
    # Get the tab containing the device objects
    devices_tabs_json = parsed_json[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_ALLOWED_END_DEVICE_TAB_NAME]
    # Get the list of end-devices
    for device_object in devices_tabs_json:
        end_dev_list.append(device_object["End_Device_ID"]["DevEUI"])
    # Read  the list of end-devices
    for end_dev in end_dev_list:
        print(json.dumps(end_dev, indent=4))
    
    return parsed_json
   
#Get all entry and Prepare the json object 
def get_all_entry_and_create_JSON_GW_AllowedEndDevice_File(isOTAA):
    
    Dev_EUI = IHM.variable_ENDDeviceIDDevEUI_entry.get()
    Dev_Addr = IHM.variable_ENDDeviceIDDevAddr_entry.get()
    
    Asso_type = IHM.ASSOSInfosActivationMode_entry.get()
    Class = IHM.variable_ASSOSInfosClass_entry.get()   
    
    if( isOTAA ):
    # OTAA managed
        App_EUI = IHM.variable_OTAFieldsAppEUI_entry.get() 
        AppKey = IHM.variable_OTAFieldsAppKey_entry.get()    
        print("DevEUI :", Dev_EUI)
        print("DevAddr :", Dev_Addr)
        print("Asso_Infos :", Asso_type)
        print("Class :", Class)
        print("AppEUI :", App_EUI)
        print("AppKey :", AppKey)
    else:
    # ABP managed
        Nwk_S_Key = IHM.variable_ABPFieldsNwkSKey_entry.get()  
        App_S_Key = IHM.variable_ABPFieldsAppSKey_entry.get()   
        print("DevEUI :", Dev_EUI)
        print("DevAddr :", Dev_Addr)
        print("Asso_Infos :", Asso_type)
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
    parsed_json[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_ALLOWED_END_DEVICE_TAB_NAME].append(new_json_object)
        
# Create the name of the new provisionning file
def create_name_AllowedEndDevice_File_Name(version, server_directory):
    new_prov_file = "p_010_" + (str(version+1).zfill(4)) + ".json"
    new_prov_file = (server_directory  + new_prov_file )
    return new_prov_file

#Write the new json object and delete the old file
def write_newJSON_delete_oldJSON_updateLinkFile_GW_Allowed(new_prov_file,new_json_object,prov_file,server_directory):
    with open(new_prov_file, 'w') as resultjsonfile:
        # Print the json object in a file
        json.dump(new_json_object, resultjsonfile, indent=4)
             
    # Delete the old file
    os.remove(prov_file)
    print( "\nProvisionning file updated : ", new_prov_file )
     
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
    vFUpdateLinkFile(server_directory, link_file_name_directory, prov_file[-15:], new_prov_file[-15:] )
          
    print( "Link file updated : ", server_directory + link_file_name )
