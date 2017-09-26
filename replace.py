from __future__ import print_function
import fileinput
import os  
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
                if condition == 'uncomment':
                    self.uncomment(file)
                else:
                    self.comment(file)
                
        except Exception as e:
            print(e)
            
            
    def comment(self,file):
        res = ''
        k1=[]
        try:
            with fileinput.FileInput(os.getcwd()+'/%s/%s' %(self.comp,file), inplace=True, backup=None) as file:
                for line in file:
                    for i in self.data.values():
                        if i in line:
                            k1.append(i)
                    for m in k1:
                        if res:
                            res = (res.replace(m,list(self.data.keys())[list(self.data.values()).index(m)]))
                        else:
                            res = (line.replace(m,list(self.data.keys())[list(self.data.values()).index(m)]))
                    if res:
                        print(res,end='')
                        res = ''
                    else:
                        print(line,end='')
            
        except Exception as e:
            print(e)

            
    def uncomment(self,file):
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


if __name__ == "__main__":
    ins = ReplaceScript(cmp='compute2',env='setup1')
#     ins.execute_replace('uncomment')
    ins.execute_replace()
