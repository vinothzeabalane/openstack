import os  
import configparser
from configobj import ConfigObj
from argparse import ArgumentParser

import replace

class OpenStack:
    
    def __init__(self,comp):
        
        self.comp = comp
        self.config1 = configparser.RawConfigParser()
        self.config1.optionxform=str
        self.config2 = configparser.RawConfigParser()
        self.config2.optionxform=str
        
        self.env_file = configparser.RawConfigParser()
        self.env_file.optionxform=str
        
        self.config_file = configparser.RawConfigParser()
        self.config_file.optionxform=str
        
    
    def exec_config_file(self,org_file,replace_file):

        try:
            config = ConfigObj(org_file)
            
            self.config1.read(replace_file)
            self.config2.read(org_file)
            
            for i in self.config1.sections():
                if i in self.config2.sections():
                    for k in self.config1.items(i):
                        if k[0] in str(self.config2.items(i)):
                            config[i][k[0]] = k[1]
                            config.write()
                        else:
                            config[i][k[0]] = k[1]
                            config.write()
                else:
                    for j in self.config1.items(i):
                        config[i] = {}
                        config[i][j[0]] = j[1]
                        config.write()
                
        except Exception as e:
            print(e)
            
            
    
    def read_config_file(self):
        
        try:
            self.env_file.read('%s/%s/env.ini' %(os.getcwd(),self.comp))
            self.config_file.read('%s/%s/config_system.ini' %(os.getcwd(),self.comp))
            
            for i in self.config_file.sections():
                print('Started Installing "%s" section' %i)
                
                for k in self.config_file.items(i):
                    if k[1].startswith("/"):
                        
                        self.exec_config_file(k[1], '%s/%s/%s' %(os.getcwd(),self.comp,k[0]))
                        
                    elif k[1] == 'admin' or k[1] == 'demo':
                        print("Setup Client Environment for '%s' user" %k[1])
                        for m in self.env_file.items(k[1]):
                            os.environ[m[0]]= m[1]
                    else:
                        print("Executing the cmd: %s" %k[1])
                        os.system(k[1])
            
        except Exception as e:
            print(e)
            
            
if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-c", "--component", type=str,help="component to install")
    parser.add_argument("-e", "--env", type=str,help="environment")
    args = parser.parse_args()
    ins = OpenStack(args.component)
    rep = replace.ReplaceScript(args.component,args.env)
#     rep.execute_replace('uncomment')
    ins.read_config_file()
#     rep.execute_replace()
    