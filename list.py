#LIST adalah collection yang bersifat ordered, changeable, allow duplicate
a = [2,3,4,7,8]
print(a)
a[1] = 100
a.insert(2,200)
a.append(100)
print(a)
print(len(a))
del a[1]
print(a)
b=[]
for record in a :
    record *=10
    b.append(record)
print(b)
b.sort(reverse = True)
c =  b+a
print(c)
c.remove(2000)
print(c)