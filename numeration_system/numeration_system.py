# Converter numero de decimal para binario
def decimal_to_binary(decimal_number=int, step_by_step=False):
    """
    Write in the parentheses a number in decimal to convert in binary.
    """
    binary, binary_number = "", ""
    if step_by_step:
        print(f"Converting number {decimal_number} to binary...")
        while decimal_number > 0:
            if decimal_number % 2 == 0:
                binary += "0"
            else:
                binary += "1"
            print(f"{decimal_number} ÷ 2 = {decimal_number//2} | remainder = {decimal_number % 2}")
            decimal_number //= 2
        for letter in binary[::-1]:
            binary_number += letter
    else:
        while decimal_number > 0:
            if decimal_number % 2 == 0:
                binary += "0"
            else:
                binary += "1"
            decimal_number //= 2
        for letter in binary[::-1]:
            binary_number += letter
    if len(str(binary_number)) < 3:
        binary_number = str(binary_number[::-1])
        binary_number += (3-len(binary_number))*"0"
        binary_number = binary_number[::-1]
    return str(binary_number)
# convertendo para octal
def decimal_to_octal(decimal_number=int, step_by_step=False):
    """
    Write in the parentheses a number in decimal to convert in octal.
    """
    octal, octal_number = "", ""
    if step_by_step:
        print(f"Converting number {decimal_number} to octal...")
        
        while decimal_number > 0:
            remainder = decimal_number % 8
            print(f"{decimal_number} ÷ 8 = {decimal_number//8} | remainder = {remainder}")
            octal += str(remainder)
            decimal_number //= 8    
        for number in reversed(octal):
            octal_number += number
        return f"{int(octal_number)}"
    else:
        while decimal_number > 0:
            remainder = decimal_number % 8
            octal += str(remainder)
            decimal_number //= 8    
        for number in reversed(octal):
            octal_number += number
        return f"{int(octal_number)}"
# converter para hexadecimal
def decimal_to_hexadecimal(decimal_number=int, step_by_step=False):
    """
    Write in the parentheses a number in decimal to convert in hexadecimal.
    """
    hexadecimal, hexadecimal_number = "", ""
    letters = {
        "10": "A",
        "11": "B",
        "12": "C",
        "13": "D",
        "14": "E",
        "15": "F",
    }
    if step_by_step:
        print(f"Converting number {decimal_number} to hexadecimal...")
        while decimal_number > 0:
            remainder = decimal_number % 16
            if remainder < 10:
                hexadecimal += str(remainder)
            else:
                hexadecimal += letters[f"{str(remainder)}"]
            print(f"{decimal_number} ÷ 16 = {decimal_number//16} | remainder = {remainder}")
            decimal_number //= 16
        return f"{hexadecimal[::-1]}"
    else:
        while decimal_number > 0:
            remainder = decimal_number % 16
            if remainder < 10:
                hexadecimal += str(remainder)
            else:
                hexadecimal += letters[f"{str(remainder)}"]
            decimal_number //= 16
        for number in reversed(hexadecimal):
            hexadecimal_number += number
        return f"{str(hexadecimal_number)}"
# Convertendo fracionario para binario
def decimal_fractionary_to_binary(fractionary_number=float):
    """
    (This function still not have step by step) Write in the parentheses a string of fractionary number to convert in binary.
    """
    separated_number = str(fractionary_number).replace(".", ",").split(",")
    integer_part = int(separated_number[0])
    fractionary_part = float(separated_number[1])/(10**len(separated_number[1]))
    integer_part_binary = decimal_to_binary(integer_part)
    fractionary_number_binary = str(integer_part_binary) + ","
    fractionary_part_separated = None
    while fractionary_part != 0:
        fractionary_part *= 2
        fractionary_part_separated = str(fractionary_part).split(".")
        fractionary_number_binary += str(fractionary_part_separated[0])
        fractionary_part = float(fractionary_part_separated[1])
        fractionary_part /= 10**(len(str(fractionary_part))-2)
        if len(fractionary_number_binary.split(",")[1]) >= 5:
            break
    return f"{str(fractionary_number_binary)}"
# Binario para decimal
def binary_to_decimal(binary_number=int):
    """
    (This function still not have step by step) Write a binary number to convert in decimal.
    """
    decimal, number_list = 0, []
    for number in str(binary_number).lstrip():
        number_list.append(number)
    for number in enumerate(number_list[::-1]):
        decimal += int(number[1]) * (2 ** number[0])
    return decimal
# Binario para octal
def binary_to_octal(binary_number=int):
    """
    (This function still not have step by step) Write a binary number to convert in octal.
    """
    octal, bins = "", []
    binary_number = str(binary_number)
    binary_number = binary_number[::-1]
    if len(str(binary_number)) % 3 != 0:
        while len(str(binary_number)) % 3 != 0:
            binary_number += "0"
    for group in range(0, len(binary_number), 3):
        bins.append(binary_number[group:group+3])
    for group in bins:
        octal += str(binary_to_decimal(int(group[::-1])))
    return octal[::-1]
# Binario para hexadecimal
def binary_to_hexadecimal(binary_number=int):
    """
    (This function still not have step by step) Write a binary number to convert in hexadecimal.
    """
    hexadecimal, bins = "", []
    letters = {
        "10": "A",
        "11": "B",
        "12": "C",
        "13": "D",
        "14": "E",
        "15": "F",
    }
    binary_number = str(binary_number)
    binary_number = binary_number[::-1]
    if len(str(binary_number)) % 4 != 0:
        while len(str(binary_number)) % 4 != 0:
            binary_number += "0"
    for group in range(0, len(binary_number), 4):
        bins.append(binary_number[group:group+4])
    for group in bins:
        if binary_to_decimal(int(group[::-1])) < 10:
            hexadecimal += str(binary_to_decimal(int(group[::-1])))
        else:
            hexadecimal += letters[str(binary_to_decimal(int(group[::-1])))]
    return f"{hexadecimal[::-1]}"
# Octal para decimal
def octal_to_decimal(octal_number=int):
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
def octal_to_binary(octal_number=int):
    """
    Write in the parentheses a string of octal number to convert in binary.
    """
    binary = ""
    for letter in str(octal_number):
        binary += decimal_to_binary(int(letter))
    return f"{int(binary)}"
# Octal para hexadecimal
def octal_to_hexadecimal(octal_number):
    """
    Write in the parentheses a string of octal number to convert in hexadecimal.
    """
    decimal = octal_to_decimal(octal_number)
    return f"{decimal_to_hexadecimal(decimal)}"