page = dict()
line = input("Enter the line")

word = line.split()

print("counting....")
print("number of word : " ,len(line))

print("reading...")
print("word : ",word)
for lines in line :
    if lines not in page :
        page[lines] = 1
    else :
        page[lines] = page[lines] + 1

print("fainally")
print(page)