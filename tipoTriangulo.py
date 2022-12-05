A = float(input())
B = float(input())
C = float(input())


if A >= B + C:
    print(f"NAO FORMA TRIANGULO")
if (A ** 2) == (B ** 2) + (C ** 2):
    print(f"TRIANGULO RETANGULO")
if (A  ** 2) > (B ** 2) + (C ** 2):
    print(f"TRIANGULO OBTUSANGULO")
if (A ** 2) < (B ** 2) + (C ** 2):
    print(f"TRIANGULO ACUTANGULO")
if A == B and B == C and C == A:
    print(f"TRIANGULO EQUILATERO")
if (A == B and B != C) or (A != C and B == C) or (A == C and B != A):
    print(f"TRIANGULO ISOSCELES")
  