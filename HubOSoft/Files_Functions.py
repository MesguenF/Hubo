#============================================================================//
# File ............: "Files_Functions.py"
# Author ..........: MESGUEN Frederic
# Date ............: 28/02/19
#----------------------------------------------------------------------------//
# Description :
# Functions that can be used to manipulate the Hub'O files in a server
#============================================================================//
from collections import OrderedDict
import json
import os
from LoRaLinkFile import JSON_LINK_OBJ_NAME, JSON_LINK_TAB_NAME

# --------------------------------------------------
# Allow to get the complete filename of a file
# Parameters : - Directory where is stored the file 
# 			   - Beginning of the filename
# 				-Return : The name of the found file
#--------------------------------------------------
def sFGetCompleteFilenameDirectory(directory, file_begin ):
	# Get the availables files in the directory 
	available_files = os.listdir( directory ) #List in the directory
			
	# Get the begin length
	begin_length = len(file_begin)
	
	# Initialize the result
	result_file = "ERROR"  
	
	# If Gateway Configuration File
	if(file_begin == "c_010"):		
		# Look if a file like that exists in the directory
		for file in available_files:
			if( file[:begin_length] == file_begin):
				print("file[:begin_length]" , file[:begin_length])
				
				print("AFFICHAGE DE file : " , file)
				if(file != 'c_010.manifest'):
					result_file = (directory + file)
					
	#If Gateway AllowedEndDevice File
	if(file_begin == "p_010"):
		# Look if a file like that exists in the directory
		for file in available_files:
			if( file[:begin_length] == file_begin ):
				result_file = ( directory + file )
				
	return result_file

# --------------------------------------------------
# Allow to get an end-device configuration filename 
# if it exists
# Parameters : - Directory where is stored the file 
# 			   - DevEUI of the end-device
# Return : The name of the found file, an empty
#          string if it does not exist
# --------------------------------------------------
def sFGetEndDevConfigFilename(directory, DevEUI ):
		
	# Get the availables files in the directory
	available_files = os.listdir( directory )

	# Initialize the result
	result_file = ""

	# Look if a file like that exists in the directory
	for file in available_files:
		if( file[:2] == "c_" ):
			if( file.find(DevEUI) != -1 ): 
				result_file = ( directory + file )
				
	return result_file
	
# --------------------------------------------------
# Allow to update a link file with the new value of 
# the file name
# Parameters : - Directory where is stored the file
#              - Name of the link file
# 			   - Name of the old file (to remove)
#              - Name of the new file (to add)
# Return : None
# --------------------------------------------------
def vFUpdateLinkFile(directory, link_file_name_directory, old_file, new_file ):
	print("directory : " + directory)
	print("link_file_name_directory : " + link_file_name_directory)
 	
	full_link_name = link_file_name_directory
	print("full_link_name : " + full_link_name)
	
# First, get the full link file name

	# Get the current filenames inside the link file
	with open(full_link_name, 'r') as jsonfile:
		# Read the content of the json file
		json_content = jsonfile.read()
			
 		# Load the json as a json object 
		parsed_json = json.loads(json_content, object_pairs_hook=OrderedDict)
 	
	# Delete the old file name if it is inside the list
	index = 0
	for dict_element in parsed_json[JSON_LINK_OBJ_NAME][JSON_LINK_TAB_NAME]:
		if( dict_element["File_Name"] == old_file ):
			del parsed_json[JSON_LINK_OBJ_NAME][JSON_LINK_TAB_NAME][index]
		index = index + 1
 	
	# Add the new file name
	new_json_object = OrderedDict()
	new_json_object["File_Name"] = new_file
	parsed_json[JSON_LINK_OBJ_NAME][JSON_LINK_TAB_NAME].append( new_json_object )
 		
	# Re-write the new link file
	with open(full_link_name, 'w') as linkjsonfile:
		# Print the json object in the file
		json.dump( parsed_json, linkjsonfile, indent = 4 )

#-------------------------------------------------------------------------
# Write dictionnary in JSON file in a folder directory, 
# Create the json file name. (SERIALISATION)
#-------------------------------------------------------------------------
def dict_in_json(server_directory, json_name, data_dict):
	with open(server_directory + json_name, "w") as write_file:
		json.dump(data_dict, write_file, indent = 4)

#-------------------------------------------------------------------------
# Set JSON data in a dictionnary,
# And return the dictionnary.
# (load() function of json module) (DESERIALISATION)
#-------------------------------------------------------------------------
def json_in_dict(jsonfile):
	with open(jsonfile, "r") as read_file:
			data_dict = json.load(read_file)
	return data_dict

#-------------------------------------------------------------------------
# Set a dictionnary data in a string with indentation,
# and return the string
#-------------------------------------------------------------------------    
def dict_in_str(data_dict):
	data_str = json.dumps(data_dict,indent = 4)
	return data_str

#-------------------------------------------------------------------------
# Set string data in a dictionnary,
# and return the dictionnary.
#-------------------------------------------------------------------------    
def str_in_dict(data_str):
	data_dict = json.loads(data_str)
	return data_dict
