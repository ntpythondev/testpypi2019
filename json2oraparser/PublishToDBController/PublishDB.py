from json2oraparser import DBConnectionController


class PublishDB:

    def __init__(self):
        # print("welcome to PublishDB class")
        self.objDBConnetion = DBConnectionController.DBConnection()
        self.TimestampFormat = "RRRR-MM-DD HH24:MI:SS.FF"

    def fn_json_wr_dict(self, dataVal, colList, sPath, strtCollist, fileObj, parentObj):

        """ This routine is intended to create comma separated file (.csv extension)
        from dictionary object.
        :param:eventId: given eventId in the JSON object
        :param:entityId: given entityId in the JSON object
        :param:dataVal: given python dictionary object
        :param:colList: given json fields in the JSON object
        :param:sPath: given "Table" attribute in the JSON object
        :param:strtCollist: given table column names in the JSON object
        :return: string object
        """
        try:
            strDictValue = ''

            for item in colList.split(","):
                col_nm = str(item.split("~")[0])
                col_datatype = str(item.split("~")[1])
                col_parent = str(item.split("~")[2])

                if col_nm in dataVal:
                    if col_parent == 'NO':
                        strDictValue = strDictValue + self.objDBConnetion.fn_col_val_gen(str(dataVal[col_nm]),col_datatype) + "|"
                    else:
                        if col_parent in parentObj:
                            strDictValue = strDictValue + self.objDBConnetion.fn_col_val_gen(str(parentObj[col_parent]),col_datatype) + "|"
                        else:
                            strDictValue = strDictValue + "NULL" + "|"
                else:
                    if col_parent != 'NO':
                        if col_parent in parentObj:
                            strDictValue = strDictValue + self.objDBConnetion.fn_col_val_gen(str(parentObj[col_parent]),col_datatype) + "|"
                        else:
                            strDictValue = strDictValue + "NULL" + "|"
                    else:
                        strDictValue = strDictValue + "NULL" + "|"

            strDictValue = strDictValue[:-1]
            # Insert record to .sql file
            self.objDBConnetion.fn_str_insert_records(sPath, strDictValue, strtCollist, fileObj)

        except Exception as e:
            print(e)
            #logging.error(traceback.format_exc())
            # Logs the error appropriately.

        return None

    def fn_json_wr_list(self, dataVal, colList, sPath, strtCollist, fileObj, parentObj):

        """ This routine is intended to create comma separated file (.csv extension)
        from list object.
        :param:eventId: given eventId in the JSON object
        :param:entityId: given entityId in the JSON object
        :param:dataVal: given python dictionary object
        :param:colList: given json fields in the JSON object
        :param:sPath: given "Table" attribute in the JSON object
        :param:strtCollist: given table column names in the JSON object
        :return: string object
        """

        try:
            for raw1 in dataVal:
                strListValue = ''
                for item in colList.split(","):
                    col_nm = str(item.split("~")[0])
                    col_datatype = str(item.split("~")[1])
                    col_parent = str(item.split("~")[2])

                    if col_nm in raw1:
                        if col_parent == 'NO':
                            strListValue = strListValue + self.objDBConnetion.fn_col_val_gen(str(raw1[col_nm]),col_datatype) + "|"
                        else:
                            if col_parent in parentObj:
                                strListValue = strListValue + self.objDBConnetion.fn_col_val_gen(str(parentObj[col_parent]), col_datatype) + "|"
                            else:
                                strListValue = strListValue + "NULL" + "|"
                    else:
                        if col_parent != 'NO':
                            if col_parent in parentObj:
                                strListValue = strListValue + self.objDBConnetion.fn_col_val_gen(str(parentObj[col_parent]), col_datatype) + "|"
                            else:
                                strListValue = strListValue + "NULL" + "|"
                        else:
                            strListValue = strListValue + "NULL" + "|"

                strListValue = strListValue[:-1]
                # Insert record to .sql file
                self.objDBConnetion.fn_str_insert_records(sPath, strListValue, strtCollist, fileObj)

        except Exception as e:
            print(e)
            #logging.error(traceback.format_exc())
            # Logs the error appropriately.

        return None

