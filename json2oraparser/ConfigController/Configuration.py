import yaml
import os
from os.path import dirname, abspath


class Configuration:

    def __init__(self):
        #print("welcome to Configuration class")
        self.rootDir = (dirname(dirname(abspath(__file__)))).replace(os.sep, '/')
        self.CONFIG_FILE = self.rootDir + '/Config/Config.yml'

    def updateDbConfigaration(self, ip, port, sid, userid, password):
        try:
            dbconnectiondata = dict(
                SQL=dict(
                    sql_path= self.rootDir + '/Resources/SQL/'
                ),
                Connection=dict(

                    ip=ip,
                    port=port,
                    SID=sid,
                    DB_ORA_USER=userid,
                    DB_ORA_PWD=password
                )
            )
            yml_file_path = self.CONFIG_FILE

            with open(yml_file_path, 'w') as ymlfile:
                yaml.dump(dbconnectiondata, ymlfile, default_flow_style=False)

        except Exception as e:
            print(e)


    def getConfiguration(self, strKey):
        """
            This routine is intended to read items under
            a pre-defined configuration structure
            YML config file and return the object as per.
            :param: Key in Configuration file
            :return: object list
        """
        try:

            yml_file_path = self.CONFIG_FILE

            with open(yml_file_path, 'r') as ymlfile:
                cfg = yaml.load(ymlfile)

            i = 0
            obj = []

            for item in strKey.split("|"):
                if i == 0:
                    obj = cfg[str(item)]
                else:
                    obj = obj[str(item)]

                i = i + 1

            return str(obj)

        except Exception as e:
            print(e)

            # Logs the error appropriately.


