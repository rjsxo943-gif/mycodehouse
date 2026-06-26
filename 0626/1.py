y = []

i = 0
c=0
for  i in range(5):    
    a = int(input("5개의 정수값을 입력하시오: "))
    y.append(a)


c = int(len(y))

print(y)
print(f'mean = {sum(y)/c}, sum = {sum(y)}, min = {min(y)}, max = {max(y)}')

