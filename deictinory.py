page = dict()
names = ['mam','sir','mam','mam','sir','student']
for name in names :
    if name not in page :
        page[name] = 1
    else :
        page[name] = page[name] + 1
print(page)