#CPF Generator
import random

digit_1 = 0
digit_2 = 0
count = []
cpf = '00625937'

for i in range(9 - len(cpf)):
    cpf += str(random.randint(0,9))

for i in range(10,1, -1): 
    count.append(i) 

for i in range(9):
    digit_1 += (int(cpf[i]) * count[i])
res1 = (digit_1 * 10) % 11
res1 = res1 if res1 <= 9 else 0

count.insert(0, 11)
cpf_val = cpf[:9] + str(res1)

for i in range(10):
    digit_2 += (int(cpf_val[i]) * count[i])
res2 = (digit_2 * 10) % 11
res2 = res2 if res2 <= 9 else 0

cpf_val = cpf[:9] + str(res1) + str(res2)

print(f'CPF: {cpf_val[0:3]}.{cpf_val[3:6]}.{cpf_val[6:9]}-{cpf_val[9:]}')