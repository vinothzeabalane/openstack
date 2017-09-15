import os  
import configparser
from configobj import ConfigObj
import json

from ConfigParser import SafeConfigParser
import glob
import codecs
import sys


class ReplaceScript:
    
    
    def __init__(self,cmp,env):

        try:
            with open("user_input.json") as f:
                data = json.load(f)
            
            self.setup = env
            self.comp = cmp
            self.data= data[env]['replace']
        except Exception as e:
            print(e)
        
        
    def execute_replace(self,condition=None):
        
        try:
            res =  os.listdir(os.getcwd()+'/%s' %self.comp)
            for file in res:
                
                print("Executing the file for %s" %file)
                self.config = configparser.RawConfigParser()
                self.config.optionxform=str
                self.config.read(os.getcwd()+'/%s/%s' %(self.comp,file))
                
                self.config1 = ConfigObj(os.getcwd()+'/%s/%s' %(self.comp,file))
                
                
                if condition == 'uncomment':
                    self.uncomment()
                else:
                    self.comment()
           
        except Exception as e:
            print(e)
                
    def write1(self,l1):
        
        parser = SafeConfigParser()
        parser.optionxform=str

        with codecs.open('/opt/prakash/openstack/dashboard.ini', 'r', encoding='utf-8') as f:
            parser.readfp(f)
        
        fp = open('/opt/prakash/openstack/dashboard.ini', 'w')
        
        for i in l1:
            
            parser.set(i[0], i[1], i[2])
        parser.write(fp)
        
        
    def uncomment(self,file=None):
        try:
            l1=[]
            print("Executing the file for %s" %file)
            self.config = configparser.RawConfigParser()
            self.config.optionxform=str
            self.config.read(os.getcwd()+'/%s/%s' %(self.comp,file))
            
#             self.config1 = ConfigObj(os.getcwd()+'/%s/%s' %(self.comp,file))
            
            for l in self.data.keys():
                for i in self.config.sections():
                    for k in self.config.items(i):
                        if l in str(k[1]):
                            val= self.data[l]
#                             print(i,self.config[i][k[0]], self.config[i][k[0]].replace(l,val))
                            l1.append((i,self.config[i][k[0]], self.config[i][k[0]].replace(l,val)))
#                             self.config1[i][k[0]] = self.config1[i][k[0]].replace(l,val)
#                             self.config1.write()
            self.write1(l1)
        except Exception as e:
            if 'File contains no section headers.' in str(e):
                pass
            else:
                print(e)        
        
    
    def comment(self):
        try:
            for l in self.data.values():
                for i in self.config.sections():
                    for k in self.config.items(i):
                        if l in str(k[1]):
                            val = (list(self.data.keys())[list(self.data.values()).index(l)])
                            print("Expression changed as '%s' " % val )
                            self.config1[i][k[0]] = self.config1[i][k[0]].replace(l,val)
                            self.config1.write()
        except Exception as e:
            print(e)

            
if __name__ == "__main__":
    ins = ReplaceScript(cmp='controller',env='setup1')
#     ins.comment("config_system.ini")
    ins.uncomment("dashboard.ini")
#     ins.execute_replace('uncomment')
#     ins.execute_replace()
    
