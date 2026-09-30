# pass1.py

from opcode_table import OPTAB
from parser import parse_line
from utils import hex_to_int, int_to_hex, byte_length


def pass1(source_lines):

    print("\n")
    print("=" * 75)
    print("                         PASS 1")
    print("=" * 75)

    symbol_table = {}

    intermediate = []

    start_address = None

    locctr = None

    for line_number, original_line in enumerate(
        source_lines,
        start=1
    ):

        line = original_line.strip()

        # Ignore empty lines
        if not line:
            continue

        label, opcode, operand = parse_line(line)

        if opcode is None:
            continue

        # ==================================================
        # START
        # ==================================================

        if opcode == "START":

            if operand is None:

                raise ValueError(
                    "START requires an address."
                )

            start_address = hex_to_int(operand)

            locctr = start_address

            intermediate.append({
                "address": locctr,
                "label": label or "",
                "opcode": opcode,
                "operand": operand,
                "source": original_line.strip()
            })

            print(
                f"{int_to_hex(locctr)}   "
                f"{original_line.strip():<30}"
                f"LOCCTR = {int_to_hex(locctr)}"
            )

            continue

        # START must exist
        if locctr is None:

            raise ValueError(
                "START directive must appear first."
            )

        current_address = locctr

        # ==================================================
        # SYMBOL TABLE
        # ==================================================

        if label:

            if label in symbol_table:

                raise ValueError(
                    f"Duplicate symbol: {label}"
                )

            symbol_table[label] = locctr

        # ==================================================
        # MACHINE INSTRUCTION
        # ==================================================

        if opcode in OPTAB:

            locctr += 3

        # ==================================================
        # WORD
        # ==================================================

        elif opcode == "WORD":

            locctr += 3

        # ==================================================
        # BYTE
        # ==================================================

        elif opcode == "BYTE":

            locctr += byte_length(operand)

        # ==================================================
        # RESW
        # ==================================================

        elif opcode == "RESW":

            count = int(operand)

            locctr += 3 * count

        # ==================================================
        # RESB
        # ==================================================

        elif opcode == "RESB":

            count = int(operand)

            locctr += count

        # ==================================================
        # END
        # ==================================================

        elif opcode == "END":

            intermediate.append({
                "address": current_address,
                "label": label or "",
                "opcode": opcode,
                "operand": operand or "",
                "source": original_line.strip()
            })

            print(
                f"{int_to_hex(current_address)}   "
                f"{original_line.strip():<30}"
                f"LOCCTR = {int_to_hex(current_address)}"
            )

            break

        else:

            raise ValueError(
                f"Unknown opcode: {opcode}"
            )

        # ==================================================
        # SAVE INTERMEDIATE CODE
        # ==================================================

        intermediate.append({
            "address": current_address,
            "label": label or "",
            "opcode": opcode,
            "operand": operand or "",
            "source": original_line.strip()
        })

        print(
            f"{int_to_hex(current_address)}   "
            f"{original_line.strip():<30}"
            f"LOCCTR -> {int_to_hex(locctr)}"
        )

    # ======================================================
    # PROGRAM LENGTH
    # ======================================================

    program_length = locctr - start_address

    return (
        symbol_table,
        intermediate,
        start_address,
        program_length
    )


# ==========================================================
# DISPLAY SYMBOL TABLE
# ==========================================================

def display_symbol_table(symbol_table):

    print("\n")
    print("=" * 75)
    print("                       SYMBOL TABLE")
    print("=" * 75)

    print(
        f"{'SYMBOL':<20}"
        f"{'ADDRESS':<15}"
    )

    print("-" * 35)

    for symbol, address in symbol_table.items():

        print(
            f"{symbol:<20}"
            f"{int_to_hex(address):<15}"
        )


# ==========================================================
# DISPLAY INTERMEDIATE CODE
# ==========================================================

def display_intermediate(intermediate):

    print("\n")
    print("=" * 75)
    print("                     INTERMEDIATE CODE")
    print("=" * 75)

    print(
        f"{'ADDRESS':<10}"
        f"{'LABEL':<12}"
        f"{'OPCODE':<10}"
        f"{'OPERAND':<20}"
    )

    print("-" * 55)

    for entry in intermediate:

        print(
            f"{int_to_hex(entry['address']):<10}"
            f"{entry['label']:<12}"
            f"{entry['opcode']:<10}"
            f"{entry['operand']:<20}"
        )