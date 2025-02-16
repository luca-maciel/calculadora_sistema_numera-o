# Converter numero de decimal para binario
from time import sleep

def decimal_to_binary(decimal_number=int):
    """
    Write in the parentheses a number in decimal to convert in binary.
    """
    print(f"Converting number {decimal_number} to binary...")
    sleep(.2)
    binary = ""
    binary_number = ""
    while decimal_number > 0:
        if decimal_number % 2 == 0:
            binary += "0"
        else:
            binary += "1"
        print(f"{decimal_number} ÷ 2 = {decimal_number//2} | remainder = {decimal_number % 2}")
        sleep(.2)
        decimal_number //= 2
    for letter in binary[::-1]:
        binary_number += letter
    return int(binary_number)
    # for number in reversed(binary):
    #     print(number, end="")
def valueof_decimal_to_binary(decimal_number=int):
    """
    Write in the parentheses a number in decimal to convert in binary.
    """
    binary = ""
    binary_number = ""
    while decimal_number > 0:
        if decimal_number % 2 == 0:
            binary += "0"
        else:
            binary += "1"
        decimal_number //= 2
    for letter in binary[::-1]:
        binary_number += letter
    return int(binary_number)
# convertendo para octal
def decimal_to_octal(decimal_number):
    """
    Write in the parentheses a number in decimal to convert in octal.
    """
    print(f"Converting number {decimal_number} to octal...")
    octal = ""
    octal_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 8
        print(f"{decimal_number} ÷ 8 = {decimal_number//8} | remainder = {remainder}")
        sleep(.2)
        octal += str(remainder)
        decimal_number //= 8    
    for number in reversed(octal):
        octal_number += number
    return int(octal_number)
def valueof_decimal_to_octal(decimal_number):
    """
    Write in the parentheses a number in decimal to convert in octal.
    """
    octal = ""
    octal_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 8
        octal += str(remainder)
        decimal_number //= 8    
    for number in reversed(octal):
        octal_number += number
    return int(octal_number)
# converter para hexadecimal
def decimal_to_hexadecimal(decimal_number):
    """
    Write in the parentheses a number in decimal to convert in hexadecimal.
    """
    print(f"Converting number {decimal_number} to hexadecimal...")
    hexadecimal = ""
    while decimal_number > 0:
        remainder = decimal_number % 16
        if remainder < 10:
            hexadecimal += str(remainder)
        else:
            hexadecimal += chr(ord('A') + remainder - 10)
        print(f"{decimal_number} ÷ 16 = {decimal_number//16} | remainder = {remainder}")
        sleep(.2)
        decimal_number //= 16
    for number in reversed(hexadecimal):
        print(number, end="")
def valueof_decimal_to_hexadecimal(decimal_number):
    """
    Write in the parentheses a number in decimal to convert in hexadecimal.
    """
    hexadecimal = ""
    hexadecimal_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 16
        if remainder < 10:
            hexadecimal += str(remainder)
        else:
            hexadecimal += chr(ord('A') + remainder - 10)
        decimal_number //= 16
    for number in reversed(hexadecimal):
        hexadecimal_number += number
    return hexadecimal_number
# Convertendo fracionario para binario
def decimal_fractionary_to_binary(fractionary_number=str):
    """
    Write in the parentheses a string of fractionary number to convert in binary.
    """
    numero_separado = fractionary_number.split(",")
    parte_inteira = int(numero_separado[0])
    parte_fracionaria = float(numero_separado[1])/(10**len(numero_separado[1]))
    parte_inteira_binaria = valueof_decimal_to_binary(parte_inteira)

    fractionary_number_binario = str(parte_inteira_binaria) + ","

    parte_fracionaria_separada = None

    while parte_fracionaria != 0:
        parte_fracionaria *= 2
        parte_fracionaria_separada = str(parte_fracionaria).split(".")
        fractionary_number_binario += str(parte_fracionaria_separada[0])
        parte_fracionaria = float(parte_fracionaria_separada[1])
        parte_fracionaria /= 10**(len(str(parte_fracionaria))-2)
        sleep(.1)
        if len(fractionary_number_binario.split(",")[1]) >= 5:
            break
    return fractionary_number_binario
# Binario para decimal
def binary_to_decimal(binary_number):
    """
    Write a binary number to convert in decimal.
    """
    decimal = 0
    number_list = []
    for number in str(binary_number).lstrip():
        number_list.append(number)
    for number in enumerate(number_list[::-1]):
        decimal += int(number[1]) * (2 ** number[0])
    return decimal
# Binario para octal
def binary_to_octal(binary_number):
    """
    Write a binary number to convert in octal.
    """
    decimal = binary_to_decimal(binary_number)
    return valueof_decimal_to_octal(decimal)
# Binario para hexadecimal
def binary_to_hexadecimal(binary_number):
    """
    Write a binary number to convert in hexadecimal.
    """
    decimal = binary_to_decimal(binary_number)
    return valueof_decimal_to_hexadecimal(decimal)
# Octal para decimal
def octal_to_decimal(octal_number):
    """
    Write in the parentheses a string of octal number to convert in decimal.
    """
    decimal = 0
    number_list = []
    for number in str(octal_number).lstrip():
        number_list.append(number)
    for number in enumerate(number_list[::-1]):
        decimal += int(number[1]) * (8 ** number[0])
    return decimal
# Octal para binario
def octal_to_binary(octal_number):
    """
    Write in the parentheses a string of octal number to convert in binary.
    """
    decimal = octal_to_decimal(octal_number)
    return valueof_decimal_to_binary(decimal)
# Octal para hexadecimal
def octal_to_hexadecimal(octal_number):
    """
    Write in the parentheses a string of octal number to convert in hexadecimal.
    """
    decimal = octal_to_decimal(octal_number)
    return valueof_decimal_to_hexadecimal(decimal)