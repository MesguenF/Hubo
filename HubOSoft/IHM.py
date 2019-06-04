#============================================================================//
# File ............: "IHM.py"
# Author ..........: MESGUEN Frederic
# Date ............: 04/03/19
#----------------------------------------------------------------------------//
# Description : Graphic interface
#         
#============================================================================//
import shutil
from tkinter import Tk, Label, Frame, Button, Menu, ttk, Entry, Checkbutton, messagebox, \
    StringVar, DoubleVar, IntVar, Toplevel,BooleanVar,Pack,Place,filedialog
from tkinter.constants import DISABLED, NORMAL
from Files_Functions import *
from LoRaGWConfigurationFile import get_GW_config_file,\
    get_GW_config_file_version,get_all_entry_and_create_JSON_GW_Conf_File,\
    create_name_config_file, create_name_config_file_directory,\
    write_newJSON_delete_oldJSON_updateLinkFile_GW_Conf
    
from LoRaGWAllowedEndDeviceFile import get_AllowedEndDevice_File,\
    create_name_AllowedEndDevice_File_Name, get_all_entry_and_create_JSON_GW_AllowedEndDevice_File,\
    write_newJSON_delete_oldJSON_updateLinkFile_GW_Allowed,get_AllowedEndDevice_File_version
from LoRaEndDeviceConfigFile import *
from tkinter.tix import *
from CONSTANTS import INDEX_JSON_LIST

#Variable to allow or deny access to entry widgets / DISABLED OR NORMAL
changeStateAllEntry = DISABLED # DISABLED OR NORMAL

#Variable color for entry widgets focus
color_disabled_background_widgets = 'light grey'

#Variable for cursor type
type_cursor ="hand2"

#Variable for configuration folder directory
DIR_NAME_CONFIG = ""

#Variable for data folder directory
DIR_NAME_DATA = ""

#Variables for enable entry access 
bool_config_directory = False
bool_data_directory = False

# Boolean variable to choose OTA or ABP End Device
bool_OTA_or_ABP = False

###################################################
#To return Configuration directory
def get_dir_name_config():
    return DIR_NAME_CONFIG

#To return Data directory
def get_dir_name_data():
    return DIR_NAME_DATA

#To return Data directory
def get_bool_OTA_or_ABP():
    return bool_OTA_or_ABP

# To create configuration of DATA folder ( folder LOGS + index.php)
def create_data_sub_folder_and_index(server_directory):
    #To create Logs folder
    path_directory = server_directory + "Logs"
    if os.path.exists(path_directory) is False:
        os.mkdir(path_directory)
    #To create file index.php 
    f = open(server_directory + 'index.php', 'w')
    f.writelines(INDEX_JSON_LIST)
    f.close()
    
#To ask Configuration directory and configure config directory   
def ask_ConfigFolder_Directory():
    global DIR_NAME_CONFIG
    global DIR_NAME_DATA
    global bool_config_directory
    global bool_data_directory
    
    #If directory don't exist
    if(DIR_NAME_CONFIG == ""):
        DIR_NAME_CONFIG = ((filedialog.askdirectory(title = "SELECTION DOSSIER DES CONFIGURATIONS", initialdir = DIR_NAME_CONFIG)) + "/").replace("/","\\")
        if(DIR_NAME_CONFIG != ""):
            bool_config_directory = True
            messagebox.showinfo(title="Information", message="Le dossier pour les configurations est le suivant :" + DIR_NAME_CONFIG)
        else:
            bool_config_directory = False
            messagebox.showinfo(title="Information", message="Le dossier pour les configurations n'est pas défini!", icon = 'warning')
    #If directory exist
    else:
        test = messagebox.askquestion(title="Confirmation", message="Le dossier actuel pour les configurations est le suivant :" + DIR_NAME_CONFIG + "\n Voulez-vous le modifier ?", icon = 'question')
        print("test = " + test)
        if(test == 'yes'):
            temp = ((filedialog.askdirectory(title = "SELECTION DOSSIER DES CONFIGURATIONS", initialdir = DIR_NAME_CONFIG)) + "/").replace("/","\\")
            if(temp != ""):
                DIR_NAME_CONFIG = temp
                bool_config_directory = True
                messagebox.showinfo(title="Information", message="Le dossier pour les configurations est le suivant :" + DIR_NAME_CONFIG)
            else:
                messagebox.showinfo(title="Information", message="Le dossier pour les configurations n'a pas été modifié.\nLe dossier pour les configurations est le suivant :" + DIR_NAME_CONFIG)
    
    # To initialyse bool_data_directory
#     if(DIR_NAME_DATA == ""):
#         bool_data_directory = False
    # To enable access if OK          
    change_entry_access(bool_config_directory,bool_data_directory)

#To ask Data directory and configure directory
def ask_DataFolder_Directory():
    global DIR_NAME_CONFIG
    global DIR_NAME_DATA
    global bool_config_directory
    global bool_data_directory
    
    #If directory don't exist
    if(DIR_NAME_DATA == ""):
        DIR_NAME_DATA = ((filedialog.askdirectory(title = "SELECTION DOSSIER DES DONNEES", initialdir = DIR_NAME_DATA)) + "/").replace("/","\\")
        if(DIR_NAME_DATA != ""):
            bool_data_directory = True
            messagebox.showinfo(title="Information", message="Le dossier pour les données est le suivant :" + DIR_NAME_DATA)
            create_data_sub_folder_and_index(DIR_NAME_DATA)
                          
        else:
            bool_data_directory = False
            messagebox.showinfo(title="Information", message="Le dossier pour les données n'est pas défini!", icon = 'warning')
    
    #If directory exist
    else:
        test = messagebox.askquestion(title="Confirmation", message="Le dossier actuel pour les configurations est le suivant :" + DIR_NAME_DATA + "\n Voulez-vous le modifier ?", icon = 'question')
        if(test == 'yes'):
            temp = ((filedialog.askdirectory(title = "SELECTION DOSSIER DES DONNEES", initialdir = DIR_NAME_DATA)) + "/").replace("/","\\")
            if(temp != ""):
                DIR_NAME_DATA = temp
                bool_config_directory = True
                messagebox.showinfo(title="Information", message="Le dossier pour les configurations est le suivant :" + DIR_NAME_DATA)
                create_data_sub_folder_and_index(DIR_NAME_DATA)               
            else:
                messagebox.showinfo(title="Information", message="Le dossier pour les configurations n'a pas été modifié.\n Le dossier pour les configurations est le suivant :" + DIR_NAME_DATA)
    
    # To initialyse bool_config_directory
#     if(DIR_NAME_CONFIG == ""):
#         bool_config_directory = False
    # To enable access if OK          
    change_entry_access(bool_config_directory,bool_data_directory)
    
#To allow or deny entries access   
def change_entry_access(bool1,bool2):
    if((bool1 == True) and (bool2) == True):
        changeStateAllEntry = NORMAL
    else:
        changeStateAllEntry = DISABLED
    ########################## part o1 of IHM #########################
    VersionLoRaGWConfigFile_entry.config(state=changeStateAllEntry)
    LANIPFixeCombo.config(state=changeStateAllEntry)
    LANIPAddr_entry.config(state=changeStateAllEntry)
    LANIPMask_entry.config(state=changeStateAllEntry)
    LANIPGw_entry.config(state=changeStateAllEntry)
    WWANPIN_entry.config(state=changeStateAllEntry)
    WWANPUK_entry.config(state=changeStateAllEntry)
    WWANIPType_entry.config(state=changeStateAllEntry)
    WWANAPN_entry.config(state=changeStateAllEntry)
    WWANAPNUser_entry.config(state=changeStateAllEntry)
    WWANAPNPwd_entry.config(state=changeStateAllEntry)
    TIMESNTPServer_entry.config(state=changeStateAllEntry)
    TIMETimeZone_entry.config(state=changeStateAllEntry)
    SERVICEDNSServer_entry.config(state=changeStateAllEntry)
    SERVICEPFSUrl_entry.config(state=changeStateAllEntry)
    SERVICEPFSPort_entry.config(state=changeStateAllEntry)
    SERVICEPFSUser_entry.config(state=changeStateAllEntry)
    SERVICEPFSPwd_entry.config(state=changeStateAllEntry)
    SERVICEPFSDataDirectory_entry.config(state=changeStateAllEntry)
    SERVICEPFSConfigDirectory_entry.config(state=changeStateAllEntry)
    SERVICEPFSLinkFileName_entry.config(state=changeStateAllEntry)
    SERVICEPFSProvisionningFileName_entry.config(state=changeStateAllEntry)
    SERVICEPFSDataFilePeriodMinutes_entry.config(state=changeStateAllEntry)
    SERVICEPFSLinkFilePeriodMinutes_entry.config(state=changeStateAllEntry)
    SERVICEEndDeviceSilenceTimeOutHours_entry.config(state=changeStateAllEntry)
    SERVICEFTPSUrl_entry.config(state=changeStateAllEntry)
    SERVICEFTPSPort_entry.config(state=changeStateAllEntry)
    SERVICEFTPSUser_entry.config(state=changeStateAllEntry)
    SERVICEFTPSPwd_entry.config(state=changeStateAllEntry)
    DEBUGSSHServerCombo.config(state=changeStateAllEntry)
    DEBUGSSHPort_entry.config(state=changeStateAllEntry)
    DEBUGLogLevel_entry.config(state=changeStateAllEntry)
    #DEBUGWatchDog_entry.config(state=changeStateAllEntry)
    DEBUGLogUploadCombo.config(state=changeStateAllEntry)
    ########################## part o2 of IHM #########################
    VersionLoRaGWAllowedEndDevFile_entry.config(state=changeStateAllEntry)
    ENDDeviceIDDevEUI_entry.config(state=changeStateAllEntry)
    ENDDeviceIDDevAddr_entry.config(state=changeStateAllEntry)
    ASSOSInfosActivationMode_entry.config(state=changeStateAllEntry)
    ASSOSInfosClass_entry.config(state=changeStateAllEntry)
#     OTAFieldsAppEUI_entry.config(state=changeStateAllEntry)
#     OTAFieldsAppKey_entry.config(state=changeStateAllEntry)
#     ABPFieldsNwkSKey_entry.config(state=changeStateAllEntry)
#     ABPFieldsAppSKey_entry.config(state=changeStateAllEntry)
    ##########################  part o3 of IHM #########################  
    VersionLoRaEndDeviceConfigFile_entry.config(state=changeStateAllEntry)
    ENDDEVICEIDDevEUI_entry.config(state=changeStateAllEntry)
    MACInfoFPort_entry.config(state=changeStateAllEntry)
    MACInfoFrmPayload_entry.config(state=changeStateAllEntry)
    ALARMINFOIsAlarm_entry.config(state=changeStateAllEntry)
    ALARMINFORegEx_entry.config(state=changeStateAllEntry)
    ALARMINFOActOnAlarm_entry.config(state=changeStateAllEntry)
    
# To display alert configuration
def show_Info_Folders(event):
    if((DIR_NAME_CONFIG == "") or (DIR_NAME_DATA == "")):
        messagebox.showinfo(title="Information", message="Les dossiers pour les CONFIGURATIONS et/ou  pour les DONNEES ne sont pas configurés!\n Veuillez sélectionner ces dossiers pour continuer!")

# To display a window with the folders directory
def show_Folders():
    TEXT ="Non défini"
    # test NAME_CONFIG              
    if(DIR_NAME_CONFIG == ""):
        text_directory_config = TEXT
    else:
        text_directory_config = DIR_NAME_CONFIG
    # test NAME_DATA     
    if(DIR_NAME_DATA == ""):
        text_directory_data = TEXT
    else:
        text_directory_data = DIR_NAME_DATA
    
    messagebox.showinfo(title="Information", message="\nChemin des configurations =  " + text_directory_config + "\nChemin des données = " + text_directory_data)

# To display a window to ask to exit the program
def ask_OK_Cancel():
    test_exit = messagebox.askokcancel(title="Confirmation", message="Vous allez quitter le logiciel,\n veuillez confirmer !", icon = 'question')
    if(test_exit):
        mainWindow.destroy()

# To enable OTA and disable ABP       
def show_OTA():
    bool_OTA_or_ABP = True
    OTAFieldsAppEUI_entry.config(state=NORMAL)
    OTAFieldsAppKey_entry.config(state=NORMAL)
    ASSOSInfosActivationMode_entry.delete (0, len(ASSOSInfosActivationMode_entry.get()))
    ASSOSInfosActivationMode_entry.insert(0,"OTA")
    ABPFieldsAppSKey_entry.selection_clear()
    ABPFieldsNwkSKey_entry.config(state=DISABLED)
    ABPFieldsAppSKey_entry.config(state=DISABLED)
    return bool_OTA_or_ABP

# To enable ABP and disable OTA 
def show_ABP():
    bool_OTA_or_ABP = False
    ABPFieldsNwkSKey_entry.config(state=NORMAL)
    ABPFieldsAppSKey_entry.config(state=NORMAL)
    ASSOSInfosActivationMode_entry.delete (0, len(ASSOSInfosActivationMode_entry.get()))
    ASSOSInfosActivationMode_entry.insert(0,"ABP")
    OTAFieldsAppEUI_entry.config(state=DISABLED)
    OTAFieldsAppKey_entry.config(state=DISABLED)
    return bool_OTA_or_ABP
    
# To create the GW configuration Json
def get_GWConfigFile():
    conf_file = get_GW_config_file(get_dir_name_config())
    version = get_GW_config_file_version(conf_file,get_dir_name_config())
    new_json_object = get_all_entry_and_create_JSON_GW_Conf_File()
    new_config_file = create_name_config_file(version)
    new_config_file_directory = create_name_config_file_directory(get_dir_name_config(), new_config_file)
    write_newJSON_delete_oldJSON_updateLinkFile_GW_Conf(new_config_file,new_json_object,conf_file,get_dir_name_config())
        
    # To create manifest file
    text1 = "bin\make-manifest.exe --type CFG --file " 
    text2 = new_config_file_directory
    text = text1 + text2
    # example command : make-manifest.exe --type CFG --file c_010_0000.json     
    os.system(text)
    # To copy the manifest file in configuration directory
    cpfich=os.path.basename("c_010.manifest")
    shutil.move("c_010.manifest",DIR_NAME_CONFIG + cpfich)
    #To display window with informations
    messagebox.showinfo(title="Information", message="Les fichiers suivants ont été créé : \n\n" + new_config_file + "\nc_010.manifest \n\nDans le dossier : " + DIR_NAME_CONFIG)

# To create a allowedEndDevice file Json    NOT FINISH
def get_GWAllowedEndDeviceFile():
    #To get the provissionning file
    prov_file = get_AllowedEndDevice_File(get_dir_name_config())
    print("The provisionning file directory and name :",prov_file)
    
    #To get the version of provisionning file
    version = get_AllowedEndDevice_File_version(prov_file, get_dir_name_config())
    print("The provisionning version :",version)
    
    #To get the new_json_object to add
    parsed_json = get_all_entry_and_create_JSON_GW_AllowedEndDevice_File(get_bool_OTA_or_ABP(),prov_file,version,get_dir_name_config())
     
    #To create the new provisionning file
    new_prov_file = create_name_AllowedEndDevice_File_Name(version, get_dir_name_config())

    #To write the new JSON file     
    write_newJSON_delete_oldJSON_updateLinkFile_GW_Allowed(new_prov_file,parsed_json,prov_file,get_dir_name_config())
#     #To display window with informations
    messagebox.showinfo(title="Information", message="Les fichiers suivants ont été créé : \n\n" + new_prov_file + "\n\nDans le dossier : " + DIR_NAME_CONFIG)

# To create a EndDeviceConfig file Json
def get_EndDeviceConfigFile():
    #prov_file = get_AllowedEndDevice_File(get_dir_name_config())
    #version_prov_file = get_AllowedEndDevice_File_version(prov_file, get_dir_name_config())
    #parsed_json = get_list_EndDevice(prov_file)
    #conf_file = test_if_existing_config_file(get_dir_name_config())
    #new_json_object = get_all_entry_and_create_JSON_GW_EndDeviceConfigFile()
    get_all_entry_and_create_JSON_GW_EndDeviceConfigFile(get_dir_name_config())
    #get_Version_Config_File(conf_file, get_dir_name_config())
#     version_conf_file = get_Version_Config_File(conf_file, get_dir_name_config())
#    
#        
#     new_config_file = create_name_EndDeviceConfig_File_Name(version_conf_file, get_dir_name_config())
#        
#     write_newJSON_delete_oldJSON_updateLinkFile_EndDeviceConf(new_config_file,new_json_object,conf_file,get_dir_name_config())
#     messagebox.showinfo(title="Information", message="Le fichier suivants a été créé : \n\n" + new_prov_file + "\n\nDans le dossier : " + DIR_NAME_CONFIG)
#     messagebox.showinfo(title="Information", message="Le fichier suivant a été créé : \n\n c_0010_70B3D5E75F0000D8.json\n\nDans le dossier : " + DIR_NAME_CONFIG)

##############GRAPHIC INTERFACE######################           
mainWindow = Tk()
mainWindow.title('CREATION DE FICHIER HUBO')  # Title
mainWindow.geometry("800x775-650+50")  # Size of mainWindow window and placement on screen
mainWindow.resizable(False, False)  # Disabled resizing
menubar = Menu(mainWindow)
mainWindow.config(menu=menubar)
#-------------------------------------------
menuparametres = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Paramètres", menu=menuparametres)
menuparametres.add_command(label = "Choisir chemin du dossier -> Configurations Hub'O ", command=ask_ConfigFolder_Directory)
menuparametres.add_command(label = "Choisir chemin du dossier -> Données Hub'O ", command=ask_DataFolder_Directory)
menuparametres.add_separator()
menuparametres.add_command(label="Afficher informations sur les chemins des dossiers", command=show_Folders)
menuparametres.add_separator()
menuparametres.add_command(label="Quitter le logiciel", command=ask_OK_Cancel)
#-------------------------------------------
n = ttk.Notebook(mainWindow)  # Creation of tab systems
bal = Balloon()
n.pack()

###EVENEMENTS####
mainWindow.bind("<Button-1>", show_Info_Folders)
mainWindow.bind("<Key>", show_Info_Folders("<Key>"))
mainWindow.protocol("WM_DELETE_WINDOW", ask_OK_Cancel)
    
################################################################################################
o1 = ttk.Frame(n, width=250)  # Add tab 1
Label(o1, text='Lora_GW_Configuration_File:').place(x=20, y=5)
###############################################
Label(o1, text='Version:').place(x=70, y=25)
VersionLoRaGWConfigFile_entry = Entry(o1, width=20, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
VersionLoRaGWConfigFile_entry.place(x=120, y=25)
variable_VersionLoRaGWConfigFile_entry = StringVar()  
variable_VersionLoRaGWConfigFile_entry.set("02.00")            
VersionLoRaGWConfigFile_entry.config(textvariable=variable_VersionLoRaGWConfigFile_entry, state=changeStateAllEntry, cursor= type_cursor)
bal.bind_widget(VersionLoRaGWConfigFile_entry, msg="02.00 par défaut")

##############################################
Label(o1, text='Lan:').place(x=70, y=40)
  
Label(o1, text='IPFixe:').place(x=100, y=55)
# Liste déroulante
variable_LANIPFixe_entry = BooleanVar()        # Variable de type str associée à la valeur affichée dans la liste
LANIPFixeCombo = ttk.Combobox(o1, textvariable=variable_LANIPFixe_entry, state=changeStateAllEntry, cursor=type_cursor)
LANIPFixeCombo.place(x=170, y=55)
#LANIPFixeCombo.config(textvariable=variable_LANIPAddr_entry, state=changeStateAllEntry, cursor=type_cursor)
LANIPFixeCombo['values'] = ('true', 'false')    # Liste des valeurs de la liste
LANIPFixeCombo.current(1)                                        # Choix de la valeur courante
#LANIPFixeCombo.bind('<<ComboboxSelected>>', choixLD)    # Action déclenchée par une sélection dans la liste 

Label(o1, text='IPAddr:').place(x=100, y=75)
LANIPAddr_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
LANIPAddr_entry.place(x=170, y=75)
variable_LANIPAddr_entry = StringVar()
LANIPAddr_entry.config(textvariable=variable_LANIPAddr_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(LANIPAddr_entry, msg="exemple : 192.168.4.192") 
   
Label(o1, text='IPMask:').place(x=100, y=95)
LANIPMask_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
LANIPMask_entry.place(x=170, y=95)
variable_LANIPMask_entry = StringVar()
LANIPMask_entry.config(textvariable=variable_LANIPMask_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(LANIPMask_entry, msg="exemple : 255.255.255.0")  
       
Label(o1, text='IPGw:').place(x=100, y=115)
LANIPGw_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
LANIPGw_entry.place(x=170, y=115)
variable_LANIPGw_entry = StringVar()
LANIPGw_entry.config(textvariable=variable_LANIPGw_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(LANIPGw_entry, msg="192.168.4.1")
        
#############################################
Label(o1, text='Wwan:').place(x=370, y=40)
    
Label(o1, text='PIN:').place(x=420, y=55)
WWANPIN_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
WWANPIN_entry.place(x=490, y=55)
variable_WWANPIN_entry = StringVar()
WWANPIN_entry.config(textvariable=variable_WWANPIN_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(WWANPIN_entry, msg="")
        
Label(o1, text='PUK:').place(x=420, y=75)
WWANPUK_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
WWANPUK_entry.place(x=490, y=75)
variable_WWANPUK_entry = StringVar()
WWANPUK_entry.config(textvariable=variable_WWANPUK_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(WWANPUK_entry, msg="")
        
Label(o1, text='IPType:').place(x=420, y=95)
WWANIPType_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
WWANIPType_entry.place(x=490, y=95)
variable_WWANIPType_entry = StringVar()
variable_WWANIPType_entry.set("IP")
WWANIPType_entry.config(textvariable=variable_WWANIPType_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(WWANIPType_entry, msg="IP par défaut")
       
Label(o1, text='APN:').place(x=420, y=115)
WWANAPN_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
WWANAPN_entry.place(x=490, y=115)
variable_WWANAPN_entry = StringVar()
WWANAPN_entry.config(textvariable=variable_WWANAPN_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(WWANAPN_entry, msg="")
       
Label(o1, text='APNUser:').place(x=420, y=135)
WWANAPNUser_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
WWANAPNUser_entry.place(x=490, y=135)
variable_WWANAPNUser_entry = StringVar()
WWANAPNUser_entry.config(textvariable=variable_WWANAPNUser_entry , state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(WWANAPNUser_entry, msg="")
        
Label(o1, text='APNPwd:').place(x=420, y=155)
WWANAPNPwd_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
WWANAPNPwd_entry.place(x=490, y=155)
variable_WWANAPNPwd_entry = StringVar()
WWANAPNPwd_entry.config(textvariable=variable_WWANAPNPwd_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(WWANAPNPwd_entry, msg="")
       
#############################################
Label(o1, text='Time:').place(x=70, y=175)
    
Label(o1, text='SNTPServer:').place(x=100, y=190)
TIMESNTPServer_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
TIMESNTPServer_entry.place(x=180, y=190)
variable_TIMESNTPServer_entry = StringVar()
variable_TIMESNTPServer_entry.set("time.nist.gov")
TIMESNTPServer_entry.config(textvariable=variable_TIMESNTPServer_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(TIMESNTPServer_entry, msg="time.nist.gov par défaut")
       
Label(o1, text='TimeZone:').place(x=100, y=210)
TIMETimeZone_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
TIMETimeZone_entry.place(x=180, y=210)
variable_TIMETimeZone_entry = StringVar()
variable_TIMETimeZone_entry.set("Europe/Paris")
TIMETimeZone_entry.config(textvariable=variable_TIMETimeZone_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(TIMETimeZone_entry, msg="Europe/Paris par défaut")
        
#############################################
Label(o1, text='Service:').place(x=70, y=240)
   
Label(o1, text='DNSServer:').place(x=100, y=260)
SERVICEDNSServer_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
SERVICEDNSServer_entry.place(x=180, y=260)
variable_SERVICEDNSServer_entry = StringVar()
variable_SERVICEDNSServer_entry.set("8.8.8.8")
SERVICEDNSServer_entry.config(textvariable=variable_SERVICEDNSServer_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(SERVICEDNSServer_entry, msg="8.8.8.8 par défaut")
        
Label(o1, text='PFSUrl:').place(x=100, y=280)
SERVICEPFSUrl_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
SERVICEPFSUrl_entry.place(x=180, y=280)
variable_SERVICEPFSUrl_entry = StringVar()
SERVICEPFSUrl_entry.config(textvariable=variable_SERVICEPFSUrl_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(SERVICEPFSUrl_entry, msg="exemple : https://192.168.4.3")
       
Label(o1, text='PFSPort:').place(x=100, y=300)
SERVICEPFSPort_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
SERVICEPFSPort_entry.place(x=180, y=300)
variable_SERVICEPFSPort_entry = IntVar()
variable_SERVICEPFSPort_entry.set("443")
SERVICEPFSPort_entry.config(textvariable=variable_SERVICEPFSPort_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(SERVICEPFSPort_entry, msg="443 par défaut")
        
Label(o1, text='PFSUser:').place(x=100, y=320)
SERVICEPFSUser_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
SERVICEPFSUser_entry.place(x=180, y=320)
variable_SERVICEPFSUser_entry = StringVar()
SERVICEPFSUser_entry.config(textvariable=variable_SERVICEPFSUser_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(SERVICEPFSUser_entry, msg="")
        
Label(o1, text='PFSPwd:').place(x=100, y=340)
SERVICEPFSPwd_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
SERVICEPFSPwd_entry.place(x=180, y=340)
variable_SERVICEPFSPwd_entry = StringVar()
SERVICEPFSPwd_entry.config(textvariable=variable_SERVICEPFSPwd_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(SERVICEPFSPwd_entry, msg="")
        
Label(o1, text='PFSDataDirectory:').place(x=100, y=362)
SERVICEPFSDataDirectory_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
SERVICEPFSDataDirectory_entry.place(x=280, y=360)
variable_SERVICEPFSDataDirectory_entry = StringVar()
SERVICEPFSDataDirectory_entry.config(textvariable=variable_SERVICEPFSDataDirectory_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(SERVICEPFSDataDirectory_entry, msg="")
       
Label(o1, text='PFSConfigDirectory:').place(x=100, y=380)
SERVICEPFSConfigDirectory_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
SERVICEPFSConfigDirectory_entry.place(x=280, y=380)
variable_SERVICEPFSConfigDirectory_entry = StringVar()
SERVICEPFSConfigDirectory_entry.config(textvariable=variable_SERVICEPFSConfigDirectory_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(SERVICEPFSConfigDirectory_entry, msg="")
        
Label(o1, text='PFSLinkFileName:').place(x=100, y=400)
SERVICEPFSLinkFileName_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
SERVICEPFSLinkFileName_entry.place(x=280, y=400)
variable_SERVICEPFSLinkFileName_entry = StringVar()
variable_SERVICEPFSLinkFileName_entry.set("corresp_file.json")
SERVICEPFSLinkFileName_entry.config(textvariable=variable_SERVICEPFSLinkFileName_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(SERVICEPFSLinkFileName_entry, msg="corresp_file.json par défaut")
        
Label(o1, text='PFSProvisionningFileName:').place(x=100, y=420)
SERVICEPFSProvisionningFileName_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
SERVICEPFSProvisionningFileName_entry.place(x=280, y=420)
variable_SERVICEPFSProvisionningFileName_entry = StringVar()
variable_SERVICEPFSProvisionningFileName_entry.set("p")
SERVICEPFSProvisionningFileName_entry.config(textvariable=variable_SERVICEPFSProvisionningFileName_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(SERVICEPFSProvisionningFileName_entry, msg="p par défaut")
        
Label(o1, text='PFSDataFilePeriodMinutes:').place(x=100, y=440)
SERVICEPFSDataFilePeriodMinutes_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
SERVICEPFSDataFilePeriodMinutes_entry.place(x=280, y=440)
variable_SERVICEPFSDataFilePeriodMinutes_entry = IntVar()
variable_SERVICEPFSDataFilePeriodMinutes_entry.set(1)
SERVICEPFSDataFilePeriodMinutes_entry.config(textvariable=variable_SERVICEPFSDataFilePeriodMinutes_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(SERVICEPFSDataFilePeriodMinutes_entry, msg="1 par défaut")
        
Label(o1, text='PFSLinkFilePeriodMinutes:').place(x=100, y=460)
SERVICEPFSLinkFilePeriodMinutes_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
SERVICEPFSLinkFilePeriodMinutes_entry.place(x=280, y=460)
variable_SERVICEPFSLinkFilePeriodMinutes_entry = IntVar()
variable_SERVICEPFSLinkFilePeriodMinutes_entry.set(1)
SERVICEPFSLinkFilePeriodMinutes_entry.config(textvariable=variable_SERVICEPFSLinkFilePeriodMinutes_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(SERVICEPFSLinkFilePeriodMinutes_entry, msg="1 par défaut")
        
Label(o1, text='EndDeviceSilenceTimeOutHours:').place(x=100, y=480)
SERVICEEndDeviceSilenceTimeOutHours_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
SERVICEEndDeviceSilenceTimeOutHours_entry.place(x=280, y=480)
variable_SERVICEEndDeviceSilenceTimeOutHours_entry = IntVar()
variable_SERVICEEndDeviceSilenceTimeOutHours_entry.set(25)
SERVICEEndDeviceSilenceTimeOutHours_entry.config(textvariable=variable_SERVICEEndDeviceSilenceTimeOutHours_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(SERVICEEndDeviceSilenceTimeOutHours_entry, msg="25 heures par défaut")
        
Label(o1, text='FTPSUrl:').place(x=100, y=500)
SERVICEFTPSUrl_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
SERVICEFTPSUrl_entry.place(x=180, y=500)
variable_SERVICEFTPSUrl_entry = StringVar()
SERVICEFTPSUrl_entry.config(textvariable=variable_SERVICEFTPSUrl_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(SERVICEFTPSUrl_entry, msg="exemple ftp://192.168.1.27")
        
Label(o1, text='FTPSPort:').place(x=100, y=520)
SERVICEFTPSPort_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
SERVICEFTPSPort_entry.place(x=180, y=520)
variable_SERVICEFTPSPort_entry = IntVar()
variable_SERVICEFTPSPort_entry.set(21)
SERVICEFTPSPort_entry.config(textvariable=variable_SERVICEFTPSPort_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(SERVICEFTPSPort_entry, msg="21 par défaut")
        
Label(o1, text='FTPSUser:').place(x=100, y=540)
SERVICEFTPSUser_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
SERVICEFTPSUser_entry.place(x=180, y=540)
variable_SERVICEFTPSUser_entry = StringVar()
SERVICEFTPSUser_entry.config(textvariable=variable_SERVICEFTPSUser_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(SERVICEFTPSUser_entry, msg="Identifiant FTP")
      
Label(o1, text='FTPSPwd:').place(x=100, y=560)
SERVICEFTPSPwd_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
SERVICEFTPSPwd_entry.place(x=180, y=560)
variable_SERVICEFTPSPwd_entry = StringVar()
SERVICEFTPSPwd_entry.config(textvariable=variable_SERVICEFTPSPwd_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(SERVICEFTPSPwd_entry, msg="Mot de passe FTP")
        
#############################################
Label(o1, text='Debug:').place(x=70, y=580)
    
Label(o1, text='SSHServer:').place(x=100, y=600)
    
# Liste déroulante
variable_DEBUGSSHServer_entry = BooleanVar()        # Variable de type str associée à la valeur affichée dans la liste
DEBUGSSHServerCombo = ttk.Combobox(o1, textvariable=variable_DEBUGSSHServer_entry, state=changeStateAllEntry, cursor=type_cursor)
DEBUGSSHServerCombo.place(x=180, y=600)
#LANIPFixeCombo.config(textvariable=variable_LANIPAddr_entry, state=changeStateAllEntry, cursor=type_cursor)
DEBUGSSHServerCombo['values'] = ('true', 'false')    # Liste des valeurs de la liste
DEBUGSSHServerCombo.current(0)                                       # Choix de la valeur courante
bal.bind_widget(DEBUGSSHServerCombo, msg="true par défaut")
#DEBUGSSHServerCombo.bind('<<ComboboxSelected>>', choixLD)    # Action déclenchée par une sélection dans la liste 

     
Label(o1, text='SSHPort:').place(x=100, y=620)
DEBUGSSHPort_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
DEBUGSSHPort_entry.place(x=180, y=620)
variable_DEBUGSSHPort_entry = IntVar()
variable_DEBUGSSHPort_entry.set(8322)
DEBUGSSHPort_entry.config(textvariable=variable_DEBUGSSHPort_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(DEBUGSSHPort_entry, msg="8322 par défaut")
     
Label(o1, text='LogLevel:').place(x=100, y=640)
DEBUGLogLevel_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
DEBUGLogLevel_entry.place(x=180, y=640)
variable_DEBUGLogLevel_entry = IntVar()
variable_DEBUGLogLevel_entry.set(2)
DEBUGLogLevel_entry.config(textvariable=variable_DEBUGLogLevel_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(DEBUGLogLevel_entry, msg="2 par défaut")
     
Label(o1, text='WatchDog:').place(x=100, y=660)
DEBUGWatchDog_entry = Entry(o1, width=25, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
DEBUGWatchDog_entry.place(x=180, y=660)
variable_DEBUGWatchDog_entry = BooleanVar()
variable_DEBUGWatchDog_entry.set(True)
DEBUGWatchDog_entry.config(textvariable = variable_DEBUGWatchDog_entry, state= DISABLED, cursor=type_cursor)
bal.bind_widget(DEBUGWatchDog_entry, msg="Valeur non modifiable - Toujours sur True")
     
Label(o1, text='LogUpload:').place(x=100, y=680)

# Liste déroulante
variable_DEBUGLogUpload_entry = BooleanVar()        # Variable de type str associée à la valeur affichée dans la liste
DEBUGLogUploadCombo = ttk.Combobox(o1, textvariable=variable_DEBUGLogUpload_entry, state=changeStateAllEntry, cursor=type_cursor)
DEBUGLogUploadCombo.place(x=180, y=680)
#LANIPFixeCombo.config(textvariable=variable_LANIPAddr_entry, state=changeStateAllEntry, cursor=type_cursor)
DEBUGLogUploadCombo['values'] = ('true', 'false')    # Liste des valeurs de la liste
DEBUGLogUploadCombo.current(1)                                       # Choix de la valeur courante
bal.bind_widget(DEBUGLogUploadCombo, msg="false par défaut")
#DEBUGSSHServerCombo.bind('<<ComboboxSelected>>', choixLD)    # Action déclenchée par une sélection dans la liste 

button_save = Button(o1, text='Enregistrer', cursor="hand2", activebackground='green', state=NORMAL, command=get_GWConfigFile).place(x=550, y=675)
  
o1.pack()
###################################################################################################
o2 = ttk.Frame(n, width=650)  # Add tab 2
Label(o2, text='Lora_GW_Allowed_End_Dev_File:').place(x=20, y=5)
###############################################
Label(o2, text='Version:').place(x=70, y=30)
VersionLoRaGWAllowedEndDevFile_entry = Entry(o2, width=20, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
VersionLoRaGWAllowedEndDevFile_entry.place(x=120, y=30)
variable_VersionLoRaGWAllowedEndDevFile_entry = StringVar()
variable_VersionLoRaGWAllowedEndDevFile_entry.set("02.00")
VersionLoRaGWAllowedEndDevFile_entry.config(textvariable=variable_VersionLoRaGWAllowedEndDevFile_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(VersionLoRaGWAllowedEndDevFile_entry, msg="02.00 par défaut")
##############################################
Label(o2, text='End_Device_Objects:').place(x=70, y=53)
    
Label(o2, text='End_Device_ID:').place(x=110, y=70)
    
Label(o2, text='DevEUI:').place(x=140, y=90)
ENDDeviceIDDevEUI_entry = Entry(o2, width=30, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
ENDDeviceIDDevEUI_entry.place(x=200, y=90)
variable_ENDDeviceIDDevEUI_entry = StringVar()
ENDDeviceIDDevEUI_entry.config(textvariable=variable_ENDDeviceIDDevEUI_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(ENDDeviceIDDevEUI_entry, msg="exemple 70B3D5E75F0000D8")
    
Label(o2, text='DevAddr:').place(x=140, y=115)
ENDDeviceIDDevAddr_entry = Entry(o2, width=30, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
ENDDeviceIDDevAddr_entry.place(x=200, y=115)
variable_ENDDeviceIDDevAddr_entry = StringVar()
ENDDeviceIDDevAddr_entry.config(textvariable=variable_ENDDeviceIDDevAddr_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(ENDDeviceIDDevAddr_entry, msg="exemple 010000D8")
    
Label(o2, text='Assos Infos:').place(x=110, y=135)
    
Label(o2, text='Activation_Mode:').place(x=140, y=155)
ASSOSInfosActivationMode_entry = Entry(o2, width=20, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
ASSOSInfosActivationMode_entry.place(x=240, y=155)
variable_ASSOSInfosActivationMode_entry = StringVar()
ASSOSInfosActivationMode_entry.config(textvariable=variable_ASSOSInfosActivationMode_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(ASSOSInfosActivationMode_entry, msg="OTA ou ABP")
    
Label(o2, text='Class:').place(x=140, y=180)
ASSOSInfosClass_entry = Entry(o2, width=20, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
ASSOSInfosClass_entry.place(x=240, y=180)
variable_ASSOSInfosClass_entry = StringVar()
ASSOSInfosClass_entry.config(textvariable=variable_ASSOSInfosClass_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(ASSOSInfosClass_entry, msg="A ou B ou C")
    
Label(o2, text='OTA_Fields:').place(x=110, y=200)
button_ota = Button(o2, text='CAPTEUR OTA', cursor="hand2", default=DISABLED, activebackground='green', state = NORMAL, command = show_OTA).place(x=20, y=198)

Label(o2, text='ABP_Fields:').place(x=110, y=275)
button_abp = Button(o2, text='CAPTEUR ABP', cursor="hand2", default=DISABLED, activebackground='green', state = NORMAL, command = show_ABP).place(x=20, y=273)   

Label(o2, text='AppEUI:').place(x=140, y=225)
OTAFieldsAppEUI_entry = Entry(o2, width=40, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
OTAFieldsAppEUI_entry.place(x=200, y=225)
variable_OTAFieldsAppEUI_entry = StringVar()
OTAFieldsAppEUI_entry.config(textvariable=variable_OTAFieldsAppEUI_entry, cursor=type_cursor, state = changeStateAllEntry)
bal.bind_widget(OTAFieldsAppEUI_entry, msg="exemple 70B3D5E75F600000")

Label(o2, text='AppKey:').place(x=140, y=250)
OTAFieldsAppKey_entry = Entry(o2, width=40, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
OTAFieldsAppKey_entry.place(x=200, y=250)
variable_OTAFieldsAppKey_entry = StringVar()
OTAFieldsAppKey_entry.config(textvariable=variable_OTAFieldsAppKey_entry, cursor=type_cursor, state = changeStateAllEntry)
bal.bind_widget(OTAFieldsAppKey_entry, msg="exemple 4B7E151628AED2A6ABF7158809CF4F3C")

Label(o2, text='NwkSKey:').place(x=140, y=300)
ABPFieldsNwkSKey_entry = Entry(o2, width=40, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
ABPFieldsNwkSKey_entry.place(x=200, y=300)
variable_ABPFieldsNwkSKey_entry = StringVar()
ABPFieldsNwkSKey_entry.config(textvariable=variable_ABPFieldsNwkSKey_entry, cursor=type_cursor, state = changeStateAllEntry)
bal.bind_widget(ABPFieldsNwkSKey_entry, msg="exemple 2B7E151628AED2A6ABF7158809CF4F3C")

Label(o2, text='AppSKey:').place(x=140, y=325)
ABPFieldsAppSKey_entry = Entry(o2, width=40, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
ABPFieldsAppSKey_entry.place(x=200, y=325)
variable_ABPFieldsAppSKey_entry = StringVar()
ABPFieldsAppSKey_entry.config(textvariable=variable_ABPFieldsAppSKey_entry, cursor=type_cursor, state = changeStateAllEntry)
bal.bind_widget(ABPFieldsAppSKey_entry, msg="exemple 4B7E151628AED2A6ABF7158809CF4F3C")

buttonAddDevice = Button(o2, text='AJOUTER LE CAPTEUR', cursor="hand2", default=DISABLED, activebackground='green', state=NORMAL, command=get_GWAllowedEndDeviceFile).place(x=450, y=625)
o2.pack()
##############################################################################################
o3 = ttk.Frame(n, width=650, height=750)  # Add tab 3
   
Label(o3, text='Lora_End_Device_Config_File:').place(x=20, y=5)
###############################################
Label(o3, text='Version:').place(x=70, y=30)
VersionLoRaEndDeviceConfigFile_entry = Entry(o3, width=20, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
VersionLoRaEndDeviceConfigFile_entry.place(x=120, y=30)
variable_VersionLoRaEndDeviceConfigFile_entry = StringVar()
variable_VersionLoRaEndDeviceConfigFile_entry.set("02.00")
VersionLoRaEndDeviceConfigFile_entry.config(textvariable=variable_VersionLoRaEndDeviceConfigFile_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(VersionLoRaEndDeviceConfigFile_entry, msg="02.00 par défaut")
    
Label(o3, text='End_Device_ID:').place(x=110, y=55)
    
Label(o3, text='DevEUI:').place(x=140, y=80)
ENDDEVICEIDDevEUI_entry = Entry(o3, width=20, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
ENDDEVICEIDDevEUI_entry.place(x=210, y=80)
variable_ENDDEVICEIDDevEUI_entry = StringVar()
ENDDEVICEIDDevEUI_entry.config(textvariable=variable_ENDDEVICEIDDevEUI_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(ENDDEVICEIDDevEUI_entry, msg="Message")

Label(o3, text='MAC_Info:').place(x=110, y=105)
    
Label(o3, text='FPort:').place(x=140, y=130)
MACInfoFPort_entry = Entry(o3, width=20, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
MACInfoFPort_entry.place(x=210, y=130)
variable_MACInfoFPort_entry = IntVar()
MACInfoFPort_entry.config(textvariable=variable_MACInfoFPort_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(MACInfoFPort_entry, msg="Message")
    
Label(o3, text='FrmPayload:').place(x=140, y=155)
MACInfoFrmPayload_entry = Entry(o3, width=40, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
MACInfoFrmPayload_entry.place(x=210, y=155)
variable_MACInfoFrmPayload_entry = StringVar()
MACInfoFrmPayload_entry.config(textvariable=variable_MACInfoFrmPayload_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(MACInfoFrmPayload_entry, msg="Message")
    
Label(o3, text='Alarm_Info:').place(x=110, y=180)
    
Label(o3, text='Is_Alarm:').place(x=140, y=205)
ALARMINFOIsAlarm_entry = Entry(o3, width=20, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
ALARMINFOIsAlarm_entry.place(x=210, y=205)
variable_ALARMINFOIsAlarm_entry = IntVar()
ALARMINFOIsAlarm_entry.config(textvariable=variable_ALARMINFOIsAlarm_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(ALARMINFOIsAlarm_entry, msg="Message")
    
Label(o3, text='Reg_Ex:').place(x=140, y=230)
ALARMINFORegEx_entry = Entry(o3, width=20, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
ALARMINFORegEx_entry.place(x=210, y=230)
variable_ALARMINFORegEx_entry = StringVar()
ALARMINFORegEx_entry.config(textvariable=variable_ALARMINFORegEx_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(ALARMINFORegEx_entry, msg="Message")
    
Label(o3, text='Act_On_Alarm:').place(x=125, y=255)
ALARMINFOActOnAlarm_entry = Entry(o3, width=20, disabledbackground=color_disabled_background_widgets, highlightcolor='green', highlightthickness=2)
ALARMINFOActOnAlarm_entry.place(x=210, y=255)
variable_ALARMINFOActOnAlarm_entry = IntVar()
ALARMINFOActOnAlarm_entry.config(textvariable=variable_ALARMINFOActOnAlarm_entry, state=changeStateAllEntry, cursor=type_cursor)
bal.bind_widget(ALARMINFOActOnAlarm_entry, msg="Message")
    
buttonSaveConfig = Button(o3, text='ENREGISTRER LA CONFIGURATION', cursor="hand2", activebackground='green', state=NORMAL, command=get_EndDeviceConfigFile).place(x=450, y=625)
o3.pack()
    
n.add(o1, text='Configuration HubO')  # Name tab 1
n.add(o2, text='Provisionnement')  # Name tab 2
n.add(o3, text='Configuration Capteurs')  # Name tab 3
