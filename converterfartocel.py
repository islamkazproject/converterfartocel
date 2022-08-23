def cel_to_far(cels):
    if type(cels) not in [int, float]:
        raise TypeError("Celsius must be non-negative real number only")
    return (cels * 9 / 5) + 32


# if __name__ == "__main__":
#     print(cel_to_far(90))
