#定義遊戲類別
class Game:
    #遊戲戲類別的建構子
    def  __init__(self, Attributes, name,  level):
        self._Attributes = Attributes
        self._name   = name
        self._level  = level
    #定義遊戲的物件
        s1 = Game('風','刃', 'UR')
        print("崩鐵S1屬性=",s1._Attributes)
        print("崩鐵S1姓名=",s1._name)
        print("崩鐵S1稀有度=",s1._level)

        s2 = Game('雷','卡芙卡', 'UR')
        print("崩鐵S2屬性=",s2._Attributes)
        print("崩鐵S2姓名=",s2._name)
        print("崩鐵S2稀有度=",s2._level)

        s3 = Game('虛數','馭空', 'SR')
        print("崩鐵S3屬性=",s3._Attributes)
        print("崩鐵S3姓名=",s3._name)
        print("崩鐵S3稀有度=",s3._level)

class Game(object):
    #副函式定義，名稱為method1，參數有a,b,c
    def method1(self, Attributes, name,  level):
        # 副函式程式內容，計算3個數字相乘的積
        return Attributes*name*level
           
 
#呼叫副函式，先建立類別物件
obj1 = Game()
#再利用建立好的類別物件obj1呼叫副函式method1
Attributes=1
name=2
level=3
result = obj1.method1(Attributes, name,  level) #呼叫副函式method1，將結果存入變數result中
print(result) #列印結果
 
