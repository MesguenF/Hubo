#============================================================================//
# File ............: "CONSTANTS.py"
# Author ..........: MESGUEN F
# Date ............: 04/03/19
#----------------------------------------------------------------------------//
# Description : To create the files:
#
# - index.php
# - empty LoRaGWConfigurationFile JSON
# - empty empty LoRaGWAllowedEndDevice JSON
#         
#===========================================================================//

#List with data for index.php
INDEX_JSON_LIST = ['<?php\n',
'// Set the destination directory\n',
'$target_dir = "./Logs/";\n',
'// Get the date with the wanted format\n',
'$date = date("Ymdhis");\n',
'// Form the new file name of the file that will be saved\n',
'$underscore = "_";\n', '$extension = ".json";\n',
'$filename = urldecode($_GET["Filename"]);\n',
'// Get the file content from the POST\n',
'$json_data = file_get_contents("php://input");\n',
'\n', '// Check if the file is an association request\n',
'if( stristr($filename, "asso_request_") == FALSE )\n',
'{\n', '        if( stristr($filename, "d_") != FALSE )\n',
'        {\n', '                $head = "data_";\n',
'                $devEUI = substr($filename, 2, 16);\n',
'        }\n', '        else if( stristr($filename, "a_") != FALSE )\n',
'        {\n', '                $head = "alarm_";\n',
'                $devEUI = substr($filename, 2, 16);\n',
'        }\n', '        else if( stristr($filename, "topology_lora") != FALSE )\n',
'        {\n', '                $head = "paired_devices";\n',
'                $devEUI = "";\n', '        }\n', '\n',
'        $target_file = $target_dir . $head . $devEUI . $underscore . $date . $extension;\n',
'\n', '        // Save this content in the new created file\n',
'        file_put_contents($target_file, $json_data);\n', '}\n', 'else\n',
'{\n', '        // The file is an association request\n', '        // Get the end-device devEUI\n',
'        $devEUI = substr($filename, 13, 16); // Get rid of "asso_request_" and ".json"\n', '\n', '\t\t// OK file\n',
'        $fileToAns = "{\\n\\"LoRa_GW_Asso_Answer_File\\":{\\n\\"End_Device_ID\\":{\\n\\"DevEUI\\":\\"$devEUI\\",\\n},\\n\\"Asso_status\\":\\"OK\\"\\n}\\n}";\n',
'\t\t\n', '\t\t// KO file\n',
'        //$fileToAns = "{\\n\\"LoRa_GW_Asso_Answer_File\\":{\\n\\"End_Device_ID\\":{\\n\\"DevEUI\\":\\"$devEUI\\",\\n},\\n\\"Asso_status\\":\\"KO\\"\\n}\\n}";\n',
'\t\t\n', '\t\t// WAIT file\n',
'        //$fileToAns = "{\\n\\"LoRa_GW_Asso_Answer_File\\":{\\n\\"End_Device_ID\\":{\\n\\"DevEUI\\":\\"$devEUI\\",\\n},\\n\\"Asso_status\\":\\"WAIT\\"\\n}\\n}";\n',
'\t\t\n', "        header('Content-Type: application/json');\n", '\n', '        // Send the file as an answer to the POST\n',
'        echo $fileToAns;\n', '\n', '        $head = "asso_request_";\n', '        $target_file = $target_dir . $head . $devEUI . $underscore . $date . $extension;\n', '\n',
'        // Save this content in the new created file\n', '        file_put_contents($target_file, $json_data);\n', '}\n',
'?>\n']

#Dictionnary with data for empty LoRaGWConfigurationFile JSON
EMPTY_JSON_DICT_CONFIG_FILE = {
    "LoRa_GW_Configuration_File": {
        "Version": "02.00",
        "Lan": {
            "IPFixe": "",
            "IPAddr": "",
            "IPMask": "",
            "IPGw": ""
        },
        "Wwan": {
            "PIN": "",
            "PUK": "",
            "IPType": "",
            "APN": "",
            "APNUser": "",
            "APNPwd": ""
        },
        "Time": {
            "SNTPServer": "",
            "TimeZone": ""
        },
        "Service": {
            "DNSServer": "",
            "PFSUrl": "",
            "PFSPort": "",
            "PFSUser": "",
            "PFSPwd": "",
            "PFSDataDirectory": "",
            "PFSConfigDirectory": "",
            "PFSLinkFileName": "",
            "PFSProvisionningFileName": "",
            "PFSDataFilePeriodMinutes": "",
            "PFSLinkFilePeriodMinutes": "",
            "EndDeviceSilenceTimeOutHours": "",
            "FTPSUrl": "",
            "FTPSPort": "",
            "FTPSUser": "",
            "FTPSPwd": ""
        },
        "Debug": {
            "SSHServer": "",
            "SSHPort": "",
            "LogLevel": "",
            "WatchDog": "",
            "LogUpload": ""
        }
    }
}

#Dictionnary with data for empty LoRaGWAllowedEndDevice JSON
EMPTY_JSON_DICT_ALLOWEDENDEVICE_FILE = {
  "LoRa_GW_Allowed_End_Dev_File": {
    "Version": "02.00",
    "End_Device_Objects": [
    ]
  }
}

#Dictionnary with data for empty LoRaEndDevcieConfigurationFile JSON
EMPTY_JSON_DICT_END_DEVICE_CONFIG_FILE = {
  "LoRa_End_Device_Config_File": {
    "Version": "02.00",
    "End_Device_ID": {
      "DevEUI": ""
    },
    "MAC_Info": {
      "FPort": "",
      "FrmPayload": ""
    },
    "Alarm_Info": {
      "Is_Alarm": "",
      "Reg_Ex": "",
      "Act_On_Alarm": ""
    }
  }
}