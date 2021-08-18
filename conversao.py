# conversão de temperatura em Fahrenheit para Celsius
# ENTRADA: recebe como entrada o valor da temperatura em float
# SAÍDA: imprimir o valor convertido de Fahrenheit para Celsius. O valor convertido deve ser apresentado com somente uma casa decimal

def converte(fahrenheit):
    celsius = ((fahrenheit - 32)*5/9)
    print(round(celsius, 1))
