# https://www.geeksforgeeks.org/program-decimal-binary-conversion/
def decimal_to_binary(number):
    precision = 10
    binary = ""
    integral = int(number)
    fractional = number - integral
    while integral:
        rem = integral % 2
        binary += str(rem)
        integral //= 2
    binary = binary[:: -1]
    binary = binary.rjust(16, '0')
    while precision:
        fractional *= 2
        fractional_bit = int(fractional)
        if fractional_bit == 1:
            fractional -= fractional_bit
            binary += '1'
        else:
            binary += '0'
        precision -= 1
    return binary


# https://www.geeksforgeeks.org/efficient-method-2s-complement-binary-string/
def signed_decimal_to_binary(number):
    binary_string = decimal_to_binary(abs(number))
    if abs(number) == number:
        return binary_string
    else:
        return get_2s_complement(binary_string)


def get_2s_complement(binary_string):
    n = len(binary_string)
    i = n - 1
    while i >= 0:
        if binary_string[i] == '1':
            break
        i -= 1

    if i == -1:
        return '1' + binary_string

    k = i - 1
    while k >= 0:
        if binary_string[k] == '1':
            binary_string = list(binary_string)
            binary_string[k] = '0'
            binary_string = ''.join(binary_string)
        else:
            binary_string = list(binary_string)
            binary_string[k] = '1'
            binary_string = ''.join(binary_string)
        k -= 1
    return binary_string


# https://www.geeksforgeeks.org/convert-binary-fraction-decimal/
def binary_to_decimal(binary_string):
    length = len(binary_string)
    point = binary_string.find('.')

    if point == -1:
        point = length

    int_decimal = 0
    fractional_decimal = 0
    twos = 1

    for i in range(point - 1, -1, -1):
        int_decimal += ((ord(binary_string[i]) -
                         ord('0')) * twos)
        twos *= 2

    twos = 2

    for i in range(point + 1, length):
        fractional_decimal += ((ord(binary_string[i]) - ord('0')) / twos)
        twos *= 2.0

    ans = int_decimal + fractional_decimal

    return ans


def binary_to_signed_decimal(binary_string):
    positive = True
    if binary_string[0] == '1':
        binary_string = get_2s_complement(binary_string)
        positive = False

    decimal = binary_to_decimal(binary_string[0:16] + '.' + binary_string[16:])
    return decimal if positive else -decimal


def read_data():
    file = open('data.txt', 'r')
    lines = file.readlines()
    data = [[float(record) for record in line.replace('\n', '').split(',')] for line in lines]
    for datum in data:
        print(datum)
    file.close()
    return data


def write_data(data):
    file = open('binary_data.txt', 'w')
    for record in data:
        binary_elements = ''.join([signed_decimal_to_binary(element) for element in record]) + '\n'
        file.write(binary_elements)
        print(binary_elements)
    file.close()


print(signed_decimal_to_binary(-0.523))
print(binary_to_signed_decimal('11111111111111110111101001'))
parsed_data = read_data()
write_data(parsed_data)
