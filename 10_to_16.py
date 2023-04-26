# 10진수를 16진수로 변환하는 함수
def decimal_to_hex(decimal):
    hex_map = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    result = ''
    while decimal > 0:
        remainder = decimal % 16
        if remainder >= 10:
            result = hex_map[remainder] + result
        else:
            result = str(remainder) + result
        decimal //= 16
    return result

# 16진수를 10진수로 변환하는 함수
def hex_to_decimal(hex_string):
    hex_map = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    decimal = 0
    for i, digit in enumerate(hex_string[::-1]):
        if digit in hex_map:
            decimal += hex_map[digit] * (16**i)
        else:
            decimal += int(digit) * (16**i)
    return decimal

'''
사실 제가 만들지 않았습니다.
Chat gpt가...
'''
