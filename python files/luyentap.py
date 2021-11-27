#BÀI 1a
x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
if(x**2 + y**2 <= 1):
    print("z bằng ", x**2 + y**2)
elif (y >= x):
    print("z bằng ", x + y)
elif (y < x):
    print("z bằng ", 0.5)

#BÀI 1b
import math 
x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
r = int(input("Nhập bán kính r: "))
a = int(input("Nhập hoành độ của tâm đường tròn: "))
b = int(input("Nhập tung độ của tâm đường tròn: "))
if(math.sqrt((x-a)**2)+math.sqrt((y-b)**2)<= math.sqrt(r)):
    print("z bằng:", abs(x)+abs(y))
else:
    print("z bằng:", x+y)

#BÀI 2
sigma=0
for y in range(1, 51):
    sigma += a/(a+1)
print(f'sigma={sigma:.2f}')

#BÀI 2b
