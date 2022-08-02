fahrenheit = 1
celsius = 1
def converter_far_to_cel( fahrenheit: float):
    celsius = 5/9 * (fahrenheit - 32.0)
    return celsius

if __name__ = '__main__':
    print(converter_far_to_cel(77))