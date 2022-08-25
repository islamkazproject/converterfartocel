def far_to_cel(far):
    if type(far) not in [int, float]:
        raise TypeError("Celsius must be non-negative real number only")
    return (far - 32) * 5 / 9


# if __name__ == "__main__":
#     print(far_to_cel(-40))
