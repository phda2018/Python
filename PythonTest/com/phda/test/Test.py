'''
Created on 2019年3月22日
@author: phda
'''
from com.phda.test.Dog import Dog
import json

if __name__ == '__main__':
    pass


print("hello world");


'''
1.文件读写
2.json 与 python 对象之间的转化   
'''

#从控制台读取
'''
    1.读取到exit时推出
'''
def readFromConsole():
    isContinue = True;
    while( isContinue ):
        context = input("读取到exit时停止:")
        print("读取到的内容:",context);
        
        if "exit" == context :
            isContinue =False;

# readFromConsole();

var1='hujb'
var2='hujb'
# print( cmp(var1,var2) ); # python3 中被移除

# 使用is 比较两个对象
'''
dog1 = Dog.init("ahuang");
dog2 = dog1;
print("比较两个对象是否一样："+ str(dog1 is dog2));
print("狗狗的名字是："+ dog1.getName());
'''

dog3 = Dog("a huang");
print("对象的字段形式:",str(dog3.__dict__) );

c = {"name":13};#先转化为key:value
def objToJsonString( obj ):
    #return json.dumps(obj,default=lambda obj: obj.__dict__ );
    return json.dumps(obj.__dict__);
    
#对象转化为json 字符串
print("对象转化为json 字符串：",objToJsonString( dog3 ) ) ;


    













