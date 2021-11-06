def my_function(stri , prop):
    temp = stri.split(f'{prop}="')
    temp = temp[1].split(f'"')
    return temp[0]

print(
    my_function(
        '<meta property="og:image" itemprop="thumbnailUrl" content="https://s1.vnecdn.net/vnexpress/restruct/i/v341/logo_default.jpg">',
         'content'
        )
    )