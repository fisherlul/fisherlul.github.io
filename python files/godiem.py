## BÀI 21
Y = int(input("Mời bạn nhập tháng: "))
while not(1<=Y and Y <=12):
    Y = int(input("Mời bạn nhập lại tháng: "))
if Y in(4,6,9,11):
    print("Tháng",Y ,"có 30 ngày")
elif Y == 2:
    print("Tháng",Y ,"có 28 ngày")
else:
    print("Tháng",Y ,"có 31 ngày")

## BÀI 22
n = int(input("Nhập số nguyên dương n = "));
giai_thua = 1;
if (n == 0 or n == 1):
    print("Giai thừa của số bạn nhập là 1")
elif(n%2 != 0):
    for i in range(1, n+1,2):
        giai_thua = giai_thua * i;
    print("Giai thừa kép của số bạn nhập là", n, "là", giai_thua);
else: 
    for i in range(2, n+1,2):
        giai_thua = giai_thua * i;
    print("Giai thừa kép của số bạn nhập là", n, "là", giai_thua);

## BÀI 23
n=int(input("nhập n="))
a=0
b=0
for i in range (1,n+1):
    if n%i==0:
        b+=1
print("số ước là",b)

while n>0:
   a+=1
   n=int(n/10)
print("số chữ số là",a)
    
if a==b:
    print("n là số đặc biệt")
else:
    print("n không phải là số đặc biệt")
