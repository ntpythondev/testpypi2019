# json2oraparser

The ‘json2oraparser’ library parses a JSON file according to the metadata user provides and it stores the Json data into Oracle database by taking care of nesting level of the Json.

  
PRE-REQUISITES AND ASSUMPTIONS :

a. Python should be installed in system. The recommended Python version for this library is v2.7. For higher version of Python, we will later release a new version of this library.

b. Oracle client should be available in the system.

c. Oracle database, tables, columns related to json data needs to be available.

d. Library supports only the following date/timestamp format from Json file :  
Y-m-dTH:M:S.fZ (e.g. 2018-07-29T17:44:27.633Z),  
Y-m-dTH:M:S.f,  
Y-m-d H:M:S.f,  
Y-m-d H.M.S.f,  
Y-m-d H:M:S,  
Y-m-d H.M.S,  
Y-m-d  

The entire processing is a 3 step process – 

STEP 1: INSTALL AND IMPORT LIBRARY :

a.	User first needs to install ‘json2oraparser’ library through pip from command prompt –  
pip install json2oraparser

b.	After installation, user needs to import the library in the code to use it –  
import json2oraparser  


STEP 2: METADATA CREATION :

The sample code piece related to this step is -  
metadata = json2oraparser.createMetadata('C:/Event_Metadata.csv')

json2oraparser.createMetadata() : This method will take a csv file (with absolute file path) as input and produces a list of metadata built according to the CSV. This CSV file template ('Metadata_Blank_Template.csv') is provided in the 'METADATA' folder which will be available after library installation. Please note, All the column names in the CSV should be same as given in template file.

According to the Json file, user needs to create the CSV file which will contain information about different Json entity and attribute names and their corresponding database table and column details where the Json fields will be stored.  
 
A sample Json data file - Sample_Json_File.json - is given for your reference in 'METADATA' folder.   

A sample metadata file - Sample_Metadata_with remarks.csv - has been built (available in 'METADATA' folder) as per the Sample Json (with relevant explanation/remarks in '_Remarks_' column). Please note, '_Remarks_' column is additional and is given for your reference only, it should NOT be part of the metadata CSV file.

The CSV file preparation step with proper information with correct format is the backbone of this library's successful execution. The detailed description of different columns in the metadata CSV file as well as the instruction for filling up each of those columns have been given in the file ‘Metadata_CSV_Preparation_Guide.txt’ within ‘METADATA’ folder. The same description is also given below -

FIELD_ID : 
Unique identifier and serial no. for each row in the csv.

ENTITY_NAME : 
Node names (e.g. object/list) from Json file.

ATTRIBUTE_NAME : 
Key names from Json file.

NODE_LEVEL : 
Level of any node in json file. Starting node level is denoted as '1', subsequent child level will be continued as 2, 3, 4.... In our sample Json, the starting node name is 'event'.

TABLE_NAME : 
Database table name where the entity will be stored. This can be filled up either by table synonyms (e.g. T_RL_RE) or by prefixing schema name <SchemaName>.<TableName> (e.g. MARKET.OVR). Typically one json ENTITY_NAME corresponds to one database TABLE_NAME. 
If you don't want to load an entire node's data into its corresponding database table, mark the TABLE_NAME as 'DUMMY' in CSV instead of leaving the field as blank.

COLUMN_NAME : 
Database table name where the attribute value will be stored. This basically represents the granularity of the entire metadata.

PARENT_NODE : 
Immediate parent node of any node in Json file. It is filled up as <parent ENTITY_NAME>|<starting FIELD_ID of that parent node> (e.g. Abs|7).

NODE_PATH : 
This field needs to be used for all node level of the json. For Level 1 , starting node name from the json of this level should be given as NODE_PATH . For remaining levels , there is no need to fill up this column.

ROOT_FLAG : 
Starting ROOT_FLAG of each node will be 1, for other attributes of that node ROOT_FLAG = 0.

CURRENT_IND : 
This field must be filled up as 'Y' for loading any column in database. In case, you don't want to load any particular column of a table (even though it's corresponding attribute is present in Json), fill it up as 'N'.

LOGICAL_DATATYPE : 
Datatype of the database column where you want to store json attribute value.

PARENT_COLUMN : 
If you want to load a particular column of a node with the value of any attribute of immediate parent node then PARENT_COLUMN field needs to be used. Please note, the entry in PARENT_COLUMN field in CSV must exist in Json and should belong to immediate parent node of the current entity.  


STEP 3: LOAD JSON TO ORACLE DATABASE :

The sample code piece related to this step is -  
json2oraparser.loadJson ('C:/Event2019.json', metadata, '111.11.11.11', '1111', 'EVNT', 'EVNT_USR', 'EvntPassword01')

json2oraparser.loadJson() : User needs to provide the following parameters as per the below sequence to load a json file's data to the oracle database -  
a. A data json absolute file path  
b. Metadata variable created in STEP 2  
c. Oracle database 'Hostname'  
d. Oracle database 'Port'  
e. Oracle database 'SID' or 'Service name'  
f. Oracle database 'Username'   
g. Oracle database 'Password'  


So, the entire sample code to call all the available library functions by user -  

import json2oraparser  
metadata = json2oraparser.createMetadata ('C:/Event_Metadata.csv')  
json2oraparser.loadJson ('C:/Event2019.json', metadata, '111.11.11.11', '1111', 'EVNT', 'EVNT_USR', 'EvntPassword01')  


For any query/clarification/issues regarding ‘json2oraparser’ library, please mail to ntpythondev@gmail.com.
