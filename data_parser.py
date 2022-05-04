file = open('data.txt', 'r')
lines = file.readlines()
data = [[float(record) for record in line.replace('\n', '').split(',')] for line in lines]
for datum in data:
    print(datum)


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


def signed_decimal_to_binary(number):
    binary_string = decimal_to_binary(abs(number))
    if abs(number) == number:
        return binary_string
    else:
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


print(signed_decimal_to_binary(-0.523))
