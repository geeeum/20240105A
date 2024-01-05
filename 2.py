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

class luggage(object):
    #副函式定義，名稱為method1，參數有a,b,c
    def method1(self, weight, id,  setoffairport, arriveairport, name, ):
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
 


class boardingpass(object):
    def  method2( self,name, boardingpassid, boardingdoor, boardingtime, luggagequantity,  luggageid,  seatnumber,  ):
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
