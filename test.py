

from __future__ import print_function
from configobj import ConfigObj
from configparser import SafeConfigParser
import codecs
import sys
import fileinput
import os  
import configparser

import json


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
                self.write1(file)
                
#                 print("Executing the file for %s" %file)
#                 self.config = configparser.RawConfigParser()
#                 self.config.optionxform=str
#                 self.config.read(os.getcwd()+'/%s/%s' %(self.comp,file))
#                 
#                 self.config1 = ConfigObj(os.getcwd()+'/%s/%s' %(self.comp,file))
#                 
#                 if condition == 'uncomment':
#                     self.uncomment()
#                 else:
#                     self.comment()
           
        except Exception as e:
            print(e)
                
    def write1(self,file):
        res = ''
        k1=[]
        try:
            with fileinput.FileInput(os.getcwd()+'/%s/%s' %(self.comp,file), inplace=True, backup=None) as file:
                for line in file:
                    for i in self.data.keys():
                        if i in line:
                            k1.append(i)
                    for m in k1:
                        if res:
                            res = (res.replace(m,self.data[m]))
                        else:
                            res = (line.replace(m,self.data[m]))
                    if res:
                        print(res,end='')
                        res = ''
                    else:
                        print(line,end='')
            
        except Exception as e:
            print(e)
        
        
    def uncomment(self,file=None):
        try:
            l1=[]
            print("Executing the file for %s" %file)
            self.config = configparser.RawConfigParser()
            self.config.optionxform=str
            self.config.read(os.getcwd()+'/%s/%s' %(self.comp,file))
            
            for l in self.data.keys():
                for i in self.config.sections():
                    for k in self.config.items(i):
                        if l in str(k[1]):
                            val= self.data[l]
                            l1.append((i,k[0], self.config[i][k[0]].replace(l,val)))
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
    ins = ReplaceScript(cmp='compute',env='setup1')
#     ins.write1()
#     ins.comment("config_system.ini")
#     ins.uncomment("dashboard.ini")
    ins.execute_replace('uncomment')
#     ins.execute_replace()
    
