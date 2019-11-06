# json2oraparser

The &#39;json2oraparser&#39; library parses a JSON file according to the metadata file provided by user and stores the Json data into Oracle database by taking care of nesting level (upto n-th level) of the Json.

Program reads the user given metadata for one time and looks it up while level wise parsing the Json file to build the exact path of each Json key at runtime and then extracts all the required database related information like exact table name, column name, dataype by referencing the metadata to generate a sql file with all insert statements which then gets executed in database to finally load Json data into Oracle database.


## Pre-Requisite and Assumption :

- Python should be installed in system. The recommended Python version for this library is v2.7. For higher version of Python, we will later release a new version of this library.
- Oracle client should be available in the system.
- Oracle database, tables, columns related to json data needs to be available
- Library supports only the following date/timestamp format from Json file –  
    Y-m-dTH:M:S.fZ (*e.g. 2018-07-29T17:44:27.633Z*), 
    Y-m-dTH:M:S.f,  
    Y-m-d H:M:S.f, 
    Y-m-d H.M.S.f, 
    Y-m-d H:M:S, 
    Y-m-d H.M.S, 
    Y-m-d 


## Installation :

    pip install json2oraparser


## Usage :

    import json2oraparser

    metadata = json2oraparser.createMetadata (C:/Event_Metadata.csv)

    json2oraparser.loadJson (C:/Event2019.json, metadata, 111.11.11.11, 1111, EVNT, EVNT_USR, EvntPassword@1)


## Overview :

The entire project operation is a 2 step process –

- ### STEP 1: METADATA CREATION :

      The sample code piece related to this step is -

      metadata = json2oraparser.createMetadata (C:/Event_Metadata.csv)
    
### json2oraparser.createMetadata() :

This function will take a csv file (with absolute file path) as input and produces a list of metadata built according to the CSV. This CSV file template ( **&#39;Metadata\_Blank\_Template.csv&#39;** ) is provided in the &#39;METADATA&#39; folder which will be available after library installation. *Please note, all the column names in the CSV should match with template file.*

According to the Json file, user needs to create the CSV file which will contain information about different Json entity and attribute names and their corresponding database table and column details where the Json fields will be stored.

A sample Json data file - **Sample\_Json\_File.json** - is given for your reference in &#39;METADATA&#39; folder.

A sample metadata file - **Sample\_Metadata\_with remarks.csv** - has been built (available in &#39;METADATA&#39; folder) as per the Sample Json (with relevant explanation/remarks in &#39;\_Remarks\_&#39; column). *Please note, &#39;\_Remarks\_&#39; column is added for your reference only, it should NOT be part of the metadata CSV file.*


### **Metadata CSV File Description :**

Metadata CSV file preparation with proper information and correct format is the backbone of this library&#39;s successful execution. The detailed description of different columns in the metadata CSV file as well as the instruction for filling up each of those columns have been given in the file &#39; **Metadata\_CSV\_Preparation\_Guide.txt**&#39; within &#39;METADATA&#39; folder. The same description is also given below -

**FIELD\_ID :** Unique identifier and serial number for each row in the csv.

**ENTITY\_NAME :** Node names (e.g. object/list) from Json file.

**ATTRIBUTE\_NAME :** Key names from Json file.

**NODE\_LEVEL :** Level of any node in json file. Starting node level is denoted as &#39;1&#39;, subsequent child level will be continued as 2, 3, 4... In the sample Json, the starting node name is &#39;event&#39;.

**TABLE\_NAME :** Database table name where the entity will be stored. This can be filled up either by table synonyms (e.g. T\_RL\_RE) or by prefixing schema name [SchemaName].[TableName] (e.g. MARKET.OVR). Typically one json ENTITY\_NAME corresponds to one database TABLE\_NAME. If you don&#39;t want to load an entire node&#39;s data into its corresponding database table, mark the TABLE\_NAME as &#39;DUMMY&#39; in CSV instead of leaving the field as blank.

**COLUMN\_NAME :** Database table name where the attribute value will be stored. This basically represents the granularity of the entire metadata.

**PARENT\_NODE :** Immediate parent node of any node in Json file. It is filled up as [parent ENTITY\_NAME]|[starting FIELD\_ID of that parent node] (e.g. Abs|7).

**NODE\_PATH :** This field needs to be used for all node level of the json. For Level 1 , starting node name from the json of this level should be given as NODE\_PATH . *For remaining levels , there is no need to fill up this column.*

**ROOT\_FLAG :** Starting ROOT\_FLAG of each node will be 1, for other attributes of that node ROOT\_FLAG = 0.

**CURRENT\_IND :** This field must be filled up as &#39;Y&#39; for loading any column in database. In case, you don&#39;t want to load any particular column of a table (even though it&#39;s corresponding attribute is present in Json), fill it up as &#39;N&#39;.

**LOGICAL\_DATATYPE :** Datatype of the database column where you want to store json attribute value.

**PARENT\_COLUMN :** If you want to load a particular column of a node with the value of any attribute of immediate parent node then PARENT\_COLUMN field needs to be used. Please note, the entry in PARENT\_COLUMN field in CSV must exist in Json and should belong to immediate parent node of the current entity.



- ### STEP 2: LOAD JSON TO ORACLE DATABASE :

      The sample code piece related to this step is -

      json2oraparser.loadJson (C:/Event2019.json, metadata, 111.11.11.11, 1111, EVNT, EVNT_USR, EvntPassword@1)

### json2oraparser.loadJson() :

User needs to provide the following parameters to this function as per the below sequence to load a Json file&#39;s data into Oracle database -

- A valid Json file (with absolute file path)
- Metadata variable created in STEP 1
- Oracle database &#39;Hostname&#39;
- Oracle database &#39;Port&#39;
- Oracle database &#39;SID&#39; or &#39;Service name&#39;
- Oracle database &#39;Username&#39;
- Oracle database &#39;Password&#39;


## Contact Info :
For any query/clarification/issue regarding the &#39;json2oraparser&#39; library, please mail to [**ntpythondev@gmail.com**](mailto:ntpythondev@gmail.com) **.**
