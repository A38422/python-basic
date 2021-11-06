import random
import re

class MyClass:    
    def __init__(self):
        self.list = []
    def random_list(self):
        for i in range(0, 5):    
            self.list.append(random.randrange(102, 198, 3))
        return self.list
    def number_in_string(self, stri):
        self.list = re.findall(r'\d+', stri)
        for i in range(0, len(self.list)):
            self.list[i] = int(self.list[i])
        return self.list

lst = MyClass()
print(lst.random_list())
print(
    lst.number_in_string(
        "Tôi từng tự ý bán cả danh mục 20-30 mã cổ phiếu của một chị khách rất thân quen trong năm 2007 và bị cằn nhằn không dứt, may là tình chị em vẫn còn sau đợt khủng hoảng đó."
        )
    )