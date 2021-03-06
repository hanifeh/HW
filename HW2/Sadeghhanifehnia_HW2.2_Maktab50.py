# numbers = input("vorodi ra vared konid : ")
# numbers = numbers.strip()
# mylist = numbers.split(" ")
# mytuple = tuple(mylist)
# print(mylist)
# print(mytuple)

numbers = input("vorodi ra vared konid : ")
saver = ""
mylist = []
for i in numbers:
    if i != " ":
        saver += i

    elif saver != "":
        mylist.append(saver)
        saver = ""
if saver != "":
    mylist.append(saver)
mytuple = tuple(mylist)
print(mylist)
print(mytuple)
