def boarding():
    print("boarding")

def inquire():
    print("inquire")

def Edit_information():
    print("Edit information")
 
if __name__ == "__main__":
    boarding()
    inquire()
    Edit_information()


class Luggage:
    #遊戲戲類別的建構子
    def  __init__(self, weight, id,  setoffairport, arriveairport, name):
        self._weight = weight
        self._id  = id
        self._setoffairport  = setoffairport
        self._arriveairport  = arriveairport
        self._name  = name
        

class luggage(object):
    #副函式定義，名稱為method1，參數有a,b,c
    def method1(self, weight, id,  setoffairport, arriveairport, name ):
        # 副函式程式內容，計算3個數字相乘的積
        return weight*id*setoffairport*arriveairport*name,
        #呼叫副函式，先建立類別物件
obj1 = luggage()
#再利用建立好的類別物件obj1呼叫副函式method1
weight=1
id=2
setoffairport=3
arriveairport=4
name=5
result = obj1.method1( weight, id,  setoffairport, arriveairport, name, ) #呼叫副函式method1，將結果存入變數result中
print(result) #列印結果
 
class Boardingpass:
    #遊戲戲類別的建構子
    def  __init__(self,name, boardingpassid, boardingdoor, boardingtime, luggagequantity,  luggageid,  seatnumber):
        self._name  = name
        self._boardingpassid  = boardingpassid
        self._boardingdoor  = boardingdoor
        self._boardingtime  = boardingtime
        self._luggagequantity  = luggagequantity
        self._luggageid   =  luggageid
        self._seatnumber  = seatnumber

class boardingpass(object):
    def  method2( self,name, boardingpassid, boardingdoor, boardingtime, luggagequantity,  luggageid,  seatnumber ):
        return name*boardingpassid*boardingdoor*boardingtime*luggagequantity*luggageid*seatnumber
obj2 = boardingpass()
name=1
boardingpassid=2 
boardingdoor=3 
boardingtime=4 
luggagequantity=5  
luggageid=6  
seatnumber=7
result = obj2.method2(name, boardingpassid, boardingdoor, boardingtime, luggagequantity,  luggageid,  seatnumber) #呼叫副函式method1，將結果存入變數result中
print(result) #列印結果
