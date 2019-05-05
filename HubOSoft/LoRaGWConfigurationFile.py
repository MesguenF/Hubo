#============================================================================//
# File ............: "LoRaGWConfigurationFile.py"
# Author ..........: MESGUEN F
# Date ............: 04/03/19
#----------------------------------------------------------------------------//
# Description : This is the script to create a LoRa_GW_Configuration_File
#         
#============================================================================//
from Files_Functions import *
import IHM
from CONSTANTS import EMPTY_JSON_DICT_CONFIG_FILE
from LoRaLinkFile import EMPTY_JSON_DICT_LINK_FILE, DEFAULT_LINK_FILE_NAME, JSON_LINK_START_NAME

# CONSTANTS
JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME = "LoRa_GW_Configuration_File"
JSON_GW_CONF_TAB_NAME_LAN = "Lan"
JSON_GW_CONF_TAB_NAME_WWAN = "Wwan"
JSON_GW_CONF_TAB_NAME_TIME = "Time"
JSON_GW_CONF_TAB_NAME_SERVICE = "Service"
JSON_GW_CONF_TAB_NAME_DEBUG = "Debug"

EMPTY_JSON_NAME_GW_CONFIGURATION = "c_010_0000.json"

# Get the GW configuration file and configuration file version
def get_GW_config_file(server_directory):
    conf_file = sFGetCompleteFilenameDirectory(server_directory,"c_010")
              
    #If no config file then create the name of a empty config file
    if(conf_file == "ERROR"):
        conf_file = server_directory + EMPTY_JSON_NAME_GW_CONFIGURATION
        dict_in_json(server_directory, EMPTY_JSON_NAME_GW_CONFIGURATION, EMPTY_JSON_DICT_CONFIG_FILE)
        
    return conf_file
   
# Get the GW configuration file version
def get_GW_config_file_version(conf_file,server_directory):
    version = int( conf_file[(len(server_directory) + 6):(len(server_directory) + 10)] )
    return version
    
#Get all entry and Prepare the json object 
def get_all_entry_and_create_JSON_GW_Conf_File():
    
    #Variables to receive the entries of interface 
    VersionGW = IHM.VersionLoRaGWConfigFile_entry.get()
    LanIPFixe = IHM.variable_LANIPFixe_entry.get()                                        
    LanIPAdrr = IHM.variable_LANIPAddr_entry.get()                                             
    LanIPMask = IHM.variable_LANIPMask_entry.get()                                                  
    LanIPGw = IHM.variable_LANIPGw_entry.get()                                                                             
    WwanPIN = IHM.variable_WWANPIN_entry.get()                                              
    WwanPUK = IHM.variable_WWANPUK_entry.get()                                             
    WwanIPType = IHM.variable_WWANIPType_entry.get()                                                  
    WwanAPN = IHM.variable_WWANAPN_entry.get()                                                                             
    WwanAPNUser = IHM.variable_WWANAPNUser_entry.get()                                                                             
    WwanAPNPwd = IHM.variable_WWANAPNPwd_entry.get()
    TimeSNTPServer = IHM.variable_TIMESNTPServer_entry.get()                                              
    TimeTimeZone = IHM.variable_TIMETimeZone_entry.get()
    ServiceDNSServer = IHM.variable_SERVICEDNSServer_entry.get()
    ServicePFSUrl = IHM.variable_SERVICEFTPSUrl_entry.get()
    ServicePFSPort = IHM.variable_SERVICEPFSPort_entry.get()
    ServicePFSUser = IHM.variable_SERVICEDNSServer_entry.get()
    ServicePFSPwd = IHM.variable_SERVICEFTPSPwd_entry.get()
    ServicePFSDataDirectory= IHM.variable_SERVICEPFSDataDirectory_entry.get()
    ServicePFSConfigDirectory= IHM.variable_SERVICEPFSConfigDirectory_entry.get()
    ServicePFSLinkFileName= IHM.variable_SERVICEPFSLinkFileName_entry.get()
    ServicePFSProvisionningFileName= IHM.variable_SERVICEPFSProvisionningFileName_entry.get()
    ServicePFSDataFilePeriodMinutes= IHM.variable_SERVICEPFSDataFilePeriodMinutes_entry.get()
    ServicePFSLinkFilePeriodMinutes= IHM.variable_SERVICEPFSLinkFilePeriodMinutes_entry.get()
    ServiceEndDeviceSilenceTimeOutHours= IHM.variable_SERVICEEndDeviceSilenceTimeOutHours_entry.get()
    ServiceFTPSUrl= IHM.variable_SERVICEFTPSUrl_entry.get()
    ServiceFTPSPort= IHM.variable_SERVICEFTPSPort_entry.get()
    ServiceFTPSUser= IHM.variable_SERVICEFTPSUser_entry.get()
    ServiceFTPSPwd= IHM.variable_SERVICEFTPSPwd_entry.get()     
    DebugSSHServer = IHM.variable_DEBUGSSHServer_entry.get()
    DebugSSHPort = IHM.variable_DEBUGSSHPort_entry.get()
    DebugLogLevel = IHM.variable_DEBUGLogLevel_entry.get()
    DebugWatchDog = IHM.variable_DEBUGWatchDog_entry.get()
    DebugLogUpLoad = IHM.variable_DEBUGLogUpload_entry.get()
        
    #To create a dictionnary
    # Classe OrderedDict : dictionnaire qui se souvient de l'ordre dans lequel les clefs ont été insérées (clé/valeur):                   
    new_json_object = OrderedDict()
        
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME] = OrderedDict()
        
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME]["Version"] = VersionGW
                    
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_LAN] = OrderedDict()
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_LAN]["IPFixe"] = LanIPFixe
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_LAN]["IPAddr"] = LanIPAdrr
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_LAN]["IPMask"] = LanIPMask
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_LAN]["IPGw"] = LanIPGw
                
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_WWAN] = OrderedDict()
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_WWAN]["PIN"] = WwanPIN
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_WWAN]["PUK"] = WwanPUK
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_WWAN]["IPType"] = WwanIPType
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_WWAN]["APN"] = WwanAPN
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_WWAN]["APNUser"] = WwanAPNUser
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_WWAN]["APNPwd"] = WwanAPNPwd
                
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_TIME] = OrderedDict()
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_TIME]["SNTPServer"] = TimeSNTPServer
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_TIME]["TimeZone"] = TimeTimeZone
               
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_SERVICE] = OrderedDict()
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_SERVICE]["DNSServer"] = ServiceDNSServer
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_SERVICE]["PFSUrl"] = ServicePFSUrl
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_SERVICE]["PFSPort"] = ServicePFSPort
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_SERVICE]["PFSUser"] = ServicePFSUser
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_SERVICE]["PFSPwd"] = ServicePFSPwd
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_SERVICE]["PFSDataDirectory"] = ServicePFSDataDirectory
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_SERVICE]["PFSConfigDirectory"] = ServicePFSConfigDirectory
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_SERVICE]["PFSLinkFileName"] = ServicePFSLinkFileName
        
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_SERVICE]["PFSProvisionningFileName"] = ServicePFSProvisionningFileName
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_SERVICE]["PFSDataFilePeriodMinutes"] = ServicePFSDataFilePeriodMinutes
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_SERVICE]["PFSLinkFilePeriodMinutes"] = ServicePFSLinkFilePeriodMinutes
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_SERVICE]["EndDeviceSilenceTimeOutHours"] = ServiceEndDeviceSilenceTimeOutHours
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_SERVICE]["FTPSUrl"] = ServiceFTPSUrl
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_SERVICE]["FTPSPort"] = ServiceFTPSPort
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_SERVICE]["FTPSUser"] = ServiceFTPSUser 
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_SERVICE]["FTPSPwd"] = ServiceFTPSPwd
                
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_DEBUG] = OrderedDict()
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_DEBUG]["SSHServer"] = DebugSSHServer
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_DEBUG]["SSHPort"] = DebugSSHPort
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_DEBUG]["LogLevel"] = DebugLogLevel
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_DEBUG]["WatchDog"] = DebugWatchDog
    new_json_object[JSON_GW_ALLOWED_END_DEVICE_OBJ_NAME][JSON_GW_CONF_TAB_NAME_DEBUG]["LogUpload"] = DebugLogUpLoad
    
    return new_json_object

# Create and Return the name of the new configuration file 
def create_name_config_file(version):
    new_config_file = "c_010_" + (str(version+1).zfill(4)) + ".json"
    return new_config_file

# Create and Return the name with directory of the new configuration file    
def create_name_config_file_directory(server_directory, new_config_file):
    new_config_file_directory = ( server_directory + new_config_file )
    return new_config_file_directory

# Write the new json object and delete the old file
def write_newJSON_delete_oldJSON_updateLinkFile_GW_Conf(new_config_file,new_json_object,conf_file,server_directory):
    with open(server_directory + new_config_file, 'w') as resultjsonfile:
        # Print the json object in a file
        json.dump(new_json_object, resultjsonfile, indent = 4)
        
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
    vFUpdateLinkFile(server_directory, link_file_name_directory, conf_file[-15:], new_config_file[-15:] )
        