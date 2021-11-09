# TÌM SỐ CHÍNH PHƯƠNG
n = int(input("Hãy nhập n: "))
check = False
 
for i in range(1, n+1):
    if(i**2 == n):
       check = True
       break

if (check == True):
    print(n, " là số chính phương")
else:
    print(n, " không phải là số chính phương")


# TÍNH TIỀN ĐIỆN
n = int(input("Hãy nhập n: "))
if n <= 50:
    print(1500*n);
elif n>50 and n<= 100:
    print(1500 * 50 + (n-50) * 2000);
else:
    print(1500 * 50 + 2000 * 50 + (n - 100) * 2500)


# TÍNH TỔNG CÁC SỐ CHẴN
n = int(input("Hãy nhập n: "))
s=2

for i in range (2, n, 2):
    s+=i
print (f"gia tri tong la {s:.2f}")