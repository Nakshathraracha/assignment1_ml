
N = int(input("enter no.of students "))
L = []
for i in range(N):
    L.append(input("enter weights one after another "))
k = []
for i in L:
    k.append(float(i) * 0.453592)
print(k)

