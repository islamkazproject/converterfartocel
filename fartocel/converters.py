def cel_to_far(cels: str) -> int or float:
    """Returns converted Celsius to Fahrenheit."""
    if type(cels) not in [int, float]:
        raise TypeError("Celsius must be non-negative real number only")
    if cels < -273.15:
        return "Error, the number cannot be lower than absolute zero (-273.15), please try again!"
    return (cels * 9 / 5) + 32


def far_to_cel(far: str) -> int or float:
    """Returns converted Fahrenheit to Celsius"""
    if type(far) not in [int, float]:
        raise TypeError("Fahrenheit must be non-negative real number only")
    if far < -459.66999999999996:
        return "Error, the number cannot be lower than absolute zero (-459.67), please try again!"
    return (far - 32) * 5 / 9

