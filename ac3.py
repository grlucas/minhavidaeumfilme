# triangulo.py
def determina_tipo_triangulo(lado1, lado2, lado3):
    if not (lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1):
        return "Não é um triângulo"
    elif lado1 == lado2 == lado3:
        return "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Isósceles"
    else:
        return "Escaleno"

# testa_triangulo.py
def testa_triangulo():
    from triangulo import determina_tipo_triangulo
    print(determina_tipo_triangulo(4, 4, 4)) # Equilátero
    print(determina_tipo_triangulo(2, 4, 4)) # Isósceles
    print(determina_tipo_triangulo(3, 4, 5)) # Escaleno
    print(determina_tipo_triangulo(1, 1, 4)) # Não é um triângulo
# dia_semana.py
def dia_semana(dia_numero):
    dias_semana = {
        1: 'domingo',
        2: 'segunda-feira',
        3: 'terça-feira',
        4: 'quarta-feira',
        5: 'quinta-feira',
        6: 'sexta-feira',
        7: 'sábado'
    }
    return dias_semana.get(dia_numero, '')

# testa_dia_semana.py
def testa_dia_semana():
    from dia_semana import dia_semana
    print(dia_semana(2)) # segunda-feira
    print(dia_semana(6)) # sexta-feira
    print(dia_semana(7)) # sábado
    print(dia_semana(9)) # string vazia