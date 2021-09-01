import pandas as pd
import logging

class ManageGroup():
    def __init__(self,groupFile):
        self.groupFile=groupFile
        try:
            self.codes= pd.read_csv(groupFile)
            logging.info('Open group '+str(groupFile))
        except:
            logging.info('Group '+groupFile +' not exist')
            self.codes= pd.DataFrame(columns={'Code','Name'})

    def AddCode(self,newCode,newName):
        # codeArray= self.codes.values
        try:
            codes= self.codes['Code']
            values= codes.values
            for code in values:
                if(newCode==code):
                    logging.info("Code "+newCode+" existed")
                    return False
        except:
            logging.info("Empty codes")

        data={'Code':newCode,'Name':newName}
        self.codes=self.codes.append(data,ignore_index=True)
        self.codes.to_csv(self.groupFile,index=False)
        logging.info("Add code "+newCode+" success")
        
    
    def RemoveCode(self,removeCode):
        for index,row in self.codes.iterrows():
            code= row['Code']
            if(code==removeCode):
                self.codes= pd.DataFrame.drop(self.codes,index=index)
                self.codes.to_csv(self.groupFile,index=False)
                return True
        return False
        # data={'Code':newCode}
        # self.codes=self.codes.append(data,ignore_index=True)
        # self.codes.to_csv(self.groupFile,index=False)
        # logging.info("Add code "+newCode+" success")

    def GetCodes(self):
        return self.codes

# group= ManageGroup("group1.csv")
# group.AddCode('ABC.DEF','ABC')



