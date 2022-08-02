# Вам дана строка состоящая только из цифр. 
# Вам нужно посчитать сколько нулей ("0") находится в начале строки.
# Входные данные: Строка, состоящая только из цифр.
# Выходные данные: Целое число.
def beginning_zeros(number: str) -> int:
    # your code here
    count = 0
    for letter in number:
        if letter == '0':
            count += 1
        else:
            break
    return count
if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('100'))
    print(beginning_zeros('123456'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4
    print("Coding complete? Click 'Check' to earn cool rewards!")