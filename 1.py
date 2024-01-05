class game:
    def  __init__(self, Attributes, name,  level):
        self._Attributes = Attributes
        self._name   = name
        self._level  = level

        s1 = game('風','刃', 'UR')
        print("崩鐵=屬性",s1._Attributes)
        print("崩鐵=姓名",s1._name)
        print("崩鐵=稀有度",s1._level)

        s1 = game('雷','卡芙卡', 'UR')
        print("崩鐵=屬性",s1._Attributes)
        print("崩鐵=姓名",s1._name)
        print("崩鐵=稀有度",s1._level)

        s1 = game('虛數','馭空', 'SR')
        print("崩鐵=屬性",s1._Attributes)
        print("崩鐵=姓名",s1._name)
        print("崩鐵=稀有度",s1._level)
