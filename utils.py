# utils.py


def hex_to_int(value):
    """
    Convert hexadecimal string to integer.

    Example:
        5000 -> 20480
    """

    return int(value, 16)


def int_to_hex(value, width=4):
    """
    Convert integer to hexadecimal.

    Example:
        20480 -> 5000
    """

    return format(value, f"0{width}X")


def byte_length(operand):
    """
    Calculate number of bytes occupied by BYTE.

    C'HELLO' -> 5 bytes
    X'F1'    -> 1 byte
    """

    operand = operand.strip()

    # Character constant
    if operand.startswith("C'") and operand.endswith("'"):

        characters = operand[2:-1]

        return len(characters)

    # Hexadecimal constant
    elif operand.startswith("X'") and operand.endswith("'"):

        hex_data = operand[2:-1]

        if len(hex_data) % 2 != 0:
            raise ValueError(
                f"Invalid hexadecimal BYTE constant: {operand}"
            )

        return len(hex_data) // 2

    else:

        raise ValueError(
            f"Invalid BYTE operand: {operand}"
        )


def generate_byte_object_code(operand):
    """
    Convert BYTE operand into object code.

    C'HELLO' -> 48454C4C4F
    X'F1'    -> F1
    """

    operand = operand.strip()

    # Character constant
    if operand.startswith("C'") and operand.endswith("'"):

        characters = operand[2:-1]

        object_code = ""

        for char in characters:

            object_code += format(
                ord(char),
                "02X"
            )

        return object_code

    # Hexadecimal constant
    elif operand.startswith("X'") and operand.endswith("'"):

        hex_data = operand[2:-1]

        if len(hex_data) % 2 != 0:
            raise ValueError(
                f"Invalid hexadecimal BYTE constant: {operand}"
            )

        return hex_data.upper()

    else:

        raise ValueError(
            f"Invalid BYTE operand: {operand}"
        )