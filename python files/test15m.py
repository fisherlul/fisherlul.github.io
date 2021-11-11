# BÀI 1
n = int(input ("Mời bạn nhập số n:"))
if n<=50:
    print (1500*n, "là số tiền phải trả")
elif 50<n<=100:
    print (1500*50+2000*(n-50), "là số tiền phải trả")
else:
    print (1500*50+2000*50+3000*(n-100), "là số tiền phải trả")

# BÀI 2
N = int(input('nhập số nguyên dương chẵn:'))
s = float()
if N>0 and N%2==0:
    for a in range(2, N+2, 2):
        s += (a+1)/a
    print('tổng là: ' + str(s))
else:
    print('hãy nhập số NGUYÊN DƯƠNG CHẴN')

# BÀI 3
a=int(input("Nhập a = "))
s = 1/a+1;
N = 1;
if a <= 5 :
    print (" hãy nhập a lớn hơn 5")
else:
  while 1/(a+N)> 0.0005:
      s=s+1/(a+N);
      N=N+2
  print (f"giá trị của tổng là {s:.2f}")