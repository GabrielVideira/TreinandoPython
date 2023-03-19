print("Olá, esse é um programa que calculará a o seu salario mensal")

salario_horas = input("Digite aqui o quanto recebe por hora: ")
salario_horas = float(salario_horas)

horas_trabalhadas = input("Digite aqui quantas horas trabalhou esse mês: ")
horas_trabalhadas = float(horas_trabalhadas)

salario_bruto = salario_horas * horas_trabalhadas

taxa_inss = 0.10 * salario_bruto
imposto_renda = 0.05 * salario_bruto
fgts = 0.11 * salario_bruto

taxas_totais = taxa_inss + imposto_renda + fgts

salario_liquido = salario_bruto - taxas_totais

if salario_bruto in range(0, 900):
    salario_liquido = salario_bruto
elif salario_bruto in range(901, 1500):
    salario_liquido = salario_bruto * 0.05
elif salario_bruto in range(1501, 2500):
    salario_bruto = salario_bruto * 0.1
else:
    salario_bruto = salario_bruto * 0.2

print(" Salário Bruto: ({:.2f} * {})        : R$ {:.2f}".format(
    salario_horas, horas_trabalhadas, salario_liquido))
print("(-) IR (5%)                     : R$   {:.2f}".format(imposto_renda))
print("(-) INSS ( 10%)                     : R$   {:.2f}".format(taxa_inss))
print("FGTS (11%)                     : R$   {:.2f}".format(fgts))
print("Total de descontos                     : R$   {:.2f}".format(
    taxas_totais))
print("Salário Liquido                 : R$  {:.2f}".format(salario_liquido))
