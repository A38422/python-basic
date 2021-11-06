# file = open('Id_Facebook.txt', 'r')

# data = file.read()

# lst = data.split('\n')
# print(lst)

def get_fb_id(file_name):
    with open(file_name, 'r') as f:
        for data in f:
            yield data.strip()
        f.close()


for i in get_fb_id('Id_Facebook.txt'):
    print(i)