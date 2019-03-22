'''
Created on 2019年3月22日
@author: phda
'''

class Dog(object):
    '''
        this is a dog class
    '''
    num=0;#类属性
    __name="";#私有属性
    

    def __init__(self, name):
        '''
        Constructor
        '''
        self.__name = name;
        
        
    @classmethod
    def init(dog,name):
        return  dog(name);
    
    
    def setName(self,name):
        self.__name = name;
         
    
    def getName(self):
        return  self.__name;   
        
    def __str__(self, *args, **kwargs):
        return "name:"+self.getName();
    
    def __dict__(self):
        pass
    
    