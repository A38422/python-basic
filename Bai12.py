import re

class MyClass:
    def __init__(self):
        pass
    def phone_number(self, stri):
        lst = []
        lst = re.findall(r'\d+', stri)
        pn = []
        for i in range(0, len(lst)):
            if lst[i][0] == '0':
                if len(lst[i]) == 10:
                    pn.append(lst[i])
                elif str(lst[i + 1]).isnumeric():
                    if len(lst[i + 1]) == 6:
                        temp = lst[i] + lst[i + 1]
                        pn.append(temp)
                    elif len(lst[i + 1]) == 3:
                        if str(lst[i + 2]).isnumeric() and len(lst[i + 2]) == 3:
                            temp = lst[i] + lst[i + 1] + lst[i + 2]
                            pn.append(temp)
                    elif len(lst[i + 1]) == 2:
                        if str(lst[i + 2]).isnumeric() and len(lst[i + 2]) == 2 and str(lst[i + 3]).isnumeric() and len(lst[i + 2]) == 2:
                            temp = lst[i] + lst[i + 1] + lst[i + 2] + lst[i + 3]
                            if len(temp) == 10:
                                pn.append(temp)
        return pn
    def take(self, stri, tag):
        k = re.findall(f'<.*?{tag}>[\W]+', stri)
        l = []
        for i in k:
            temp = re.sub('<.*?>|,|\B ', '', i)
            l.append(temp)
        return l

p = MyClass()


data = """© 2021 - CÔNG TY TNHH YAME VN

Giấy CNĐKDN: 0310874914 – Ngày cấp: 25/11/2011 - Cơ quan cấp: Phòng Đăng Ký Kinh Doanh – Sở Kế Hoạch và Đầu Tư TP.HCM

Địa chỉ đăng ký kinh doanh: 766/3B-3C Sư Vạn Hạnh (Nối dài), Phường 12, Quận 10, TP.HCM - Điện thoại: 028 3868 4857 - Email: cskh@yame.vn"""
print(
    p.phone_number(
        data
        )
    )