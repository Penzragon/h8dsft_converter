def celsius_kelvin(number, target):
    """
    Function to convert celsius to kelvin or vice versa.

    Args:
        number (int): Number to convert.
        target (str): Target temperature (k) for kelvin (c) for celsius.

    Return:
        converted (int): Convertion result
    """

    # Initiating converted variable
    converted = None

    # Change target string to lowercase to handle uppercase letter
    target = target.lower()

    if target == "c":  # Condition if target value is equal to 'c'
        converted = number - 273.15
    elif target == "k":  # Condition if target value is equal to 'k'
        converted = number + 273.15
    else:  # Condition if target value is not equal to either 'c' or 'k'
        converted = "Target value must be 'c' or 'k'"

    # Returning convertion result
    return converted


def convert_to_fahrenheit(number, initial):
    """
    Function to convert celsius or kelvin to fahrenheit.

    Args:
        number (int): Number to convert.
        initial (str): Initial temperature (k) for kelvin (c) for celsius.

    Return:
        converted (int): Convertion result
    """

    # Initiating converted variable
    converted = None

    # Change initial string to lowercase to handle uppercase letter
    initial = initial.lower()

    if initial == "c":  # Condition if initial value is equal to 'c'
        converted = round((number * 9 / 5) + 32, 2)
    elif initial == "k":  # Condition if initial value is equal to 'k'
        converted = round(((number - 273.15) * 9 / 5) + 32, 2)
    else:  # Condition if initial value is not equal to either 'c' or 'k'
        converted = "Initial value must be 'c' or 'k'"

    # Returning convertion result
    return converted


def convert_fahrenheit_to(number, target):
    """
    Function to convert fahrenheit to celsius or kelvin.

    Args:
        number (int): Number to convert.
        target (str): Target temperature (k) for kelvin (c) for celsius.

    Return:
        converted (int): Convertion result
    """

    # Initiating converted variable
    converted = None

    # Change target string to lowercase to handle uppercase letter
    target = target.lower()

    if target == "c":  # Condition if target value is equal to 'c'
        converted = round((number - 32) * 5 / 9, 2)
    elif target == "k":  # Condition if target value is equal to 'k'
        converted = round(((number - 32) * 5 / 9) + 273.15, 2)
    else:  # Condition if target value is not equal to either 'c' or 'k'
        converted = "Target value must be 'c' or 'k'"

    # Returning convertion result
    return converted


num = 0
print(f"{num} degrees celsius is equal to {celsius_kelvin(num, 'K')} degrees kelvin.")
print(f"{num} degrees kelvin is equal to {celsius_kelvin(num, 'c')} degrees celsius.")

print(
    f"{num} degrees kelvin is equal to {convert_to_fahrenheit(num, 'K')} degrees fahrenheit."
)
print(
    f"{num} degrees celsius is equal to {convert_to_fahrenheit(num, 'c')} degrees fahrenheit."
)

print(
    f"{num} degrees fahrenheit is equal to {convert_fahrenheit_to(num, 'K')} degrees kelvin."
)
print(
    f"{num} degrees fahrenheit is equal to {convert_fahrenheit_to(num, 'c')} degrees celsius."
)
