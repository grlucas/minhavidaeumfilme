# eq_segundo_grau.py
import math

def eq_segundo_grau(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return None, None
    elif delta == 0:
        return -b / (2*a), None
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        return raiz1, raiz2

# eh_bissexto.py
def eh_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

# calcula_salario.py
def calcula_salario(valor_hora, qtd_horas, irpf=0.275):
    salario_bruto = valor_hora * qtd_horas
    salario_liquido = salario_bruto * (1 - irpf)
    return salario_liquido