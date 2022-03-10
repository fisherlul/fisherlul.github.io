#Câu 2
a = []
#a)
n = int(input("Nhập số phần tử của danh sách a: "))
for i in range(n):
    a.append(int(input(f"Nhập phần tử ở vị trí số {i} của danh sách: ")))

#b)
tong_le = 0
for i in a:
    if (i % 2) != 0:
        tong_le += i
print(f"Tổng các phần tử lẻ của danh sách là {tong_le}")

#c)
print("Số các phần tử ở vị trí chẵn và là ước của 10 trong danh sách là", len([y for y in a if y%10==0 and a.index(y)%2==0]))

#d)
a.sort()
print(f"Các phần tử của danh sách được sắp xếp theo chiều không giảm là {a}")

#Câu 3
#a)
s1 = input('Nhập xâu s1: ')
s2 = input('Nhập xâu s2: ')

#b)
dem = 0
for i in range(1, len(s1)):
    if s1[i] >= '0' and s1[i] <= '9':
        dem += 1
print('Số ký tự số trong xâu s1 là', dem)

#c)
ss = s1 + s2
for j in range(10):
    ss=ss.replace(str(j),'')
print(ss)

#d)
if len(ss)%2==0 and ss==ss[::-1]:
    print('ss là xâu đặc biệt')
else:
    print('ss không là xâu đặc biệt')