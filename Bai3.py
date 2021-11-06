import datetime
import re

date_string = "thứ hai, 20 tháng 7 năm 2020 10:37:06 GMT+07:00"

list_number = re.findall('\d+', date_string)

element = ' '.join(list_number)
element = list(element)
del element[len(element) - 3]
element[len(element) - 5] = '+'
element = ''.join(element)

result = datetime.datetime.strptime(element,"%d %m %Y %H %M %S%z").timestamp()

print(result)


