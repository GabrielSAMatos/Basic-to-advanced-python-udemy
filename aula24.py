#Check CPF
cpf = "081.114.203-58"
cpf_num = cpf.split('.')
cpf_calc_digt1 = 0
cpf_calc_digt2 = 0
cpf_only_num = []
var_count = []

for conjunto in range(0, 3):
    for num in range(0, 3):
        cpf_only_num.append(int(cpf_num[conjunto][num]))
# for letra in cpf:
#     if letra.isdigit():
#         cpf_only_num.append(int(letra))

# cpf_only_num = cpf_only_num[:9]
print(cpf_only_num)
for i in range(10,1,-1):
    var_count.append(i)

for i in range(9):
    cpf_calc_digt1 += (cpf_only_num[i] * var_count[i])

digt1 = (cpf_calc_digt1 * 10) % 11
digt1 = digt1 if digt1 <= 9 else 0

#===================Part 2 ========================

if digt1 == int(cpf[-2]):
    cpf_only_num.append(int(cpf[-2]))
    var_count.insert(0, 11)
    for i in range(10):
        cpf_calc_digt2 += (cpf_only_num[i] * var_count[i])
        
    digt2 = (cpf_calc_digt2 * 10) % 11
    digt2 = digt2 if digt2 <= 9 else 0

    if digt2 == int(cpf[-1]):
        print('Valid CPF.')
    else:
        print('Invalid CPF')
else:
    print('Invalid CPF.')