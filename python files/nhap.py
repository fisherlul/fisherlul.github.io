n = int(input())
A = []
for i in range(n):
    x=int(input())
    A+=[x]

tong=0
for i in range (n):
    tong+=A[i]

print(tong)

k = int (input("nhập k"))
dem=0
for i in range(n):
    if A[i]%k ==0 :
        dem+=1
print("so phan tu chia het cho k la",dem)

chan, le = 0, 0
for i in A:
    if (i%2) == 0:
        chan += 1
    else:
        le += 1

print("So luong phan tu chan la:", chan)
print("So luong phan tu le la:", le)

am, duong = 0, 0
for i in A:
    if i>0:
        duong += 1
    elif i<0:
        am += 1

print("So luong phan tu duong la:", duong)
print("So luong phan tu am la:", am)

