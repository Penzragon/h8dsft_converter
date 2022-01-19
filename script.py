def celsius_kelvin(number, target):
    """
    Function to convert celsius to kelvin or vice versa.

    Args:
        number (int): Input number either celsius or kelvin.
        target (str): Target temperature (k) for kelvin (c) for celsius.

    Return:
        converted (int): Convertion result
    """

    # Initiating converted variable
    converted = None

    if target == "c":  # Condition if target value is equal to 'c'
        converted = number - 273.15
    elif target == "k":  # Condition if target value is equal to 'k'
        converted = number + 273.15
    else:  # Condition if target value is not equal to either 'c' or 'k'
        converted = "Target value must be 'c' or 'k'"

    # Returning convertion result
    return converted


num = 0
print(f"{num} degrees celsius is equal to {celsius_kelvin(num, 'k')} degrees kelvin.")
print(f"{num} degrees kelvin is equal to {celsius_kelvin(num, 'c')} degrees celsius.")
