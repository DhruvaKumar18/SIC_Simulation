# parser.py


def parse_line(line):
    """
    Parse one assembly statement.

    Returns:
        label, opcode, operand
    """

    line = line.strip()

    # Empty line
    if not line:
        return None, None, None

    # Comment
    if line.startswith("."):
        return None, None, None

    parts = line.split()

    # -----------------------------------------
    # Label + Opcode + Operand
    # -----------------------------------------

    if len(parts) >= 3:

        label = parts[0]
        opcode = parts[1].upper()
        operand = " ".join(parts[2:])

    # -----------------------------------------
    # Opcode + Operand
    # -----------------------------------------

    elif len(parts) == 2:

        label = None
        opcode = parts[0].upper()
        operand = parts[1]

    # -----------------------------------------
    # Opcode only
    # -----------------------------------------

    elif len(parts) == 1:

        label = None
        opcode = parts[0].upper()
        operand = None

    else:
        return None, None, None

    return label, opcode, operand