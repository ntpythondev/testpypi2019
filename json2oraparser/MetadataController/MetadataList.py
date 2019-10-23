import pandas as pd
import os

class MetadataList:

    def __init__(self):
        print("Metadata List Generation from CSV is getting started" + '\n')


    def fn_getPath(self, strParent, list):
        
        """ This routine is intended to determine the path object in run time.
        and use that path ("|" separated) to traverse the JSON object.
        :param:strParent: parent level tag / label to identify parent of the child
        :param:list:json metadata / schema / data dictionary
        :return:path label in string format
        """
        try:
            strFinal = ''
            Parent_Nm = strParent.split("|")[0]
            Parent_fld = strParent.split("|")[1]

            for item in list:
                    if item[1] == Parent_Nm and item[13] == Parent_fld:
                        strFinal = item[8]
            return strFinal

        except Exception as e:
            print(e)
            #logging.error(traceback.format_exc())
            #return None

    def fn_createList(self, myList):
        
        """ This routine is intended to create a list object 
        from the metadata / schema / data dictionary to traverse the JSON object accordingly.
        incorporate a runtime path in the metadata / schema per level in the given json
        :param:myList: list object representation of json metadata / schema / data dictionary
        """
        try:
            
            strFinalList = []
    
            lineCount = 0
            for row in myList:
                my_list = []
                my_list = row
                strFinalList.append(my_list)
                lineCount += 1

            count = 0
            for row in strFinalList:
                if count > 0:
                    if row[2] != "1" and row[2] != "0":
                        strPath = self.fn_getPath(row[7], strFinalList)
                        row[8] = strPath + "|" + row[1]
                count = count + 1
            return strFinalList
        
        except Exception as e:
            print(e)
            #logging.error(traceback.format_exc())
            #return None
        

    def fn_createMetadataList(self, file):

        """ This routine is intended to create a 
        list object which represents metadata from the supplied CSV file.
        :param:CSV file
        :return: List object represents metadata / data dictionary / schema object
        """        
        try:

            if os.path.exists(file) and os.path.splitext(file)[1] == '.csv':
                df1 = pd.read_csv(file)
                df1['DOMAIN_NAME'] = 'None'
                df1['RI_NODE'] = 0
                df1['ATTRIBUTE_NAME_concat'] = df1['ATTRIBUTE_NAME'].str.strip().fillna('NO') + '~' + \
                                               df1['LOGICAL_DATATYPE'].str.strip().fillna('NO') + '~' + \
                                               df1['PARENT_COLUMN'].str.strip().fillna('NO')

                df2 = df1[['FIELD_ID', 'TABLE_NAME', 'COLUMN_NAME', 'ATTRIBUTE_NAME_concat']]
                df2 = df2.rename(columns={'FIELD_ID': 'RI_NODE',
                                          'TABLE_NAME': 'RI_DBTABLE',
                                          'COLUMN_NAME': 'RI_TABLEFIELDS',
                                          'ATTRIBUTE_NAME_concat': 'RI_ATTRIBUTENAME'})

                df3 = df1.merge(df2, how='left', on='RI_NODE')
                df3 = df3.loc[df3['CURRENT_IND'] == 'Y']

                dframe = pd.DataFrame()
                dframe['ENTITY_NAME'] = df3['ENTITY_NAME'].str.strip()
                dframe['DOMAINTYPE'] = df3['DOMAIN_NAME'].str.strip().str.upper()
                dframe['JSON_LEVEL'] = df3['NODE_LEVEL']
                dframe['DBTABLE'] = df3['TABLE_NAME'].str.strip()
                dframe['ATTRIBUTE_NAME'] = df3['ATTRIBUTE_NAME_concat'].str.strip()
                dframe['TABLEFIELDS'] = df3['COLUMN_NAME'].str.strip()
                dframe['PARENT'] = df3['PARENT_NODE'].str.strip()
                dframe['JSON_PATH'] = df3['NODE_PATH'].str.strip().fillna('None')
                dframe['ROOTENTRY'] = df3['ROOT_FLAG']
                dframe['SRC_JSONTAG'] = df3['RI_ATTRIBUTENAME'].str.strip().fillna('None')
                dframe['IS_ACTIVE'] = df3['CURRENT_IND'].str.strip()
                dframe['RI_DBTABLE'] = df3['RI_DBTABLE'].str.strip().fillna('None')
                dframe['RI_TABLEFIELDS'] = df3['RI_TABLEFIELDS'].str.strip().fillna('None')
                dframe['ENTITY_ID'] = df3['FIELD_ID']
                dframe = dframe.reset_index(drop=True).sort_values('ENTITY_ID', ascending=True)
                #print(dframe.to_string())

                finalList = []
                for index, row in dframe.iterrows():

                    if row["ROOTENTRY"] == 1:
                        myList = list()
                        myList.append(str(row["DOMAINTYPE"]))
                        myList.append(str(row["ENTITY_NAME"]))
                        myList.append(str(row["JSON_LEVEL"]))
                        myList.append(str(row["DBTABLE"]) + "_array")

                        strFields = ""
                        strTableFields = ""
                        strRIJsonTAG = ""
                        strRITable = ""
                        strRIFieldName = ""
                        strTableName = ""

                        newFrame = dframe.loc[(dframe["ENTITY_NAME"] == row["ENTITY_NAME"]) & (dframe["PARENT"] == row["PARENT"]) & (dframe["DOMAINTYPE"] == row["DOMAINTYPE"]) & (dframe["DBTABLE"] == row["DBTABLE"])]  ## newFrame is required to get all the attributes detail of the the same entity_name under root_flag = 1

                        for index1, row1 in newFrame.iterrows():
                            strTableName = str(row1["DBTABLE"])
                            strFields = strFields + str(row1["ATTRIBUTE_NAME"]) + ","
                            strTableFields = strTableFields + str(row1["TABLEFIELDS"]) + ","
                            if row1["SRC_JSONTAG"] != None :
                                strRIJsonTAG =  str(row1["SRC_JSONTAG"])
                                strRITable = str(row1["RI_DBTABLE"])
                                strRIFieldName = str(row1["RI_TABLEFIELDS"])

                        myList.append(strTableName)
                        myList.append(strFields[:-1])
                        myList.append(strTableFields[:-1])
                        myList.append(str(row["PARENT"]))
                        myList.append(str(row["JSON_PATH"]))
                        myList.append(str(row["IS_ACTIVE"]))
                        myList.append(strRIJsonTAG)
                        myList.append(strRITable)
                        myList.append(strRIFieldName)
                        myList.append(str(row["ENTITY_ID"]))

                        finalList.append(myList)

                finalMetadataList = self.fn_createList(finalList)
                #print('FINAL METADATA LIST:')
                #print(finalMetadataList)

                return finalMetadataList

            else:
                print("REQUIRED CSV INPUT FILE IS NOT AVAILABLE")

        except Exception as e:
            print(e)
            #logging.error(traceback.format_exc())
