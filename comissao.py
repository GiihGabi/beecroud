#beecrowd
nome = input()
salarioFixo = float(input())
totalVendas = float(input())
comissao = (totalVendas * 0.15)
total = (salarioFixo + comissao)
print(f"{nome}")
print(f"TOTAL = {total:.2f}")