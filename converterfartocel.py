def cel_to_far(cels: str) -> int or float:
    """Returns converted Celsius to Fahrenheit."""
    if type(cels) not in [int, float]:
        raise TypeError("Celsius must be non-negative real number only")
    if cels < -273.15:
        return "Error, the number cannot be lower than absolute zero (-273.15), please try again!"
    return (cels * 9 / 5) + 32


if __name__ == "__main__":
    print(cel_to_far(-274))
