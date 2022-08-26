def far_to_cel(far: str) -> int or float:
    """Returns converted Fahrenheit to Celsius"""
    if type(far) not in [int, float]:
        raise TypeError("Fahrenheit must be non-negative real number only")
    if far < -459.66999999999996:
        return "Error, the number cannot be lower than absolute zero (-459.67), please try again!"
    return (far - 32) * 5 / 9


if __name__ == "__main__":
    print(far_to_cel(-460))
