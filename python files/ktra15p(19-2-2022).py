#BÀI 1
S1 = input("Nhập xâu thứ nhất: ")
S2 = input("Nhập xâu thứ hai: ")
S3 = input("Nhập xâu thứ ba: ")
count=0
if S1 == S1[::-1]:
    count+=1
else:
    count+=0
if S2 == S2[::-1]:
    count+=1
else:
    count+=0
if S3 == S3[::-1]:
    count+=1
else:
    count+=0
print(count)

# BÀI 2
s = str(input('Nhập xâu:'))
for i in range (0,10):
    print(f'số {i} xuất hiện {s.count(str(i))} lần')

# BÀI 3
a = input('Nhập xâu S: ')
b = a.replace('anh','em')
print('S = ',b)
