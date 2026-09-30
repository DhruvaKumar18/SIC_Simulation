# pass2.py

from opcode_table import OPTAB
from utils import (
    int_to_hex,
    generate_byte_object_code
)


def pass2(intermediate, symbol_table):

    print("\n")
    print("=" * 75)
    print("                         PASS 2")
    print("=" * 75)

    object_codes = []

    for entry in intermediate:

        address = entry["address"]

        opcode = entry["opcode"]

        operand = entry["operand"]

        object_code = ""

        # ==================================================
        # MACHINE INSTRUCTION
        # ==================================================

        if opcode in OPTAB:

            machine_opcode = OPTAB[opcode]

            # ----------------------------------------------
            # RSUB
            # ----------------------------------------------

            if opcode == "RSUB":

                object_code = (
                    machine_opcode +
                    "0000"
                )

            # ----------------------------------------------
            # Other instructions
            # ----------------------------------------------

            else:

                if operand not in symbol_table:

                    raise ValueError(
                        f"Undefined symbol: {operand}"
                    )

                operand_address = symbol_table[operand]

                object_code = (
                    machine_opcode +
                    int_to_hex(
                        operand_address,
                        4
                    )
                )

        # ==================================================
        # WORD
        # ==================================================

        elif opcode == "WORD":

            value = int(operand)

            object_code = format(
                value,
                "06X"
            )

        # ==================================================
        # BYTE
        # ==================================================

        elif opcode == "BYTE":

            object_code = (
                generate_byte_object_code(
                    operand
                )
            )

        # ==================================================
        # RESW / RESB
        # ==================================================

        elif opcode in ("RESW", "RESB"):

            object_code = ""

        # ==================================================
        # START / END
        # ==================================================

        elif opcode in ("START", "END"):

            object_code = ""

        # ==================================================
        # SAVE RESULT
        # ==================================================

        object_codes.append({
            "address": address,
            "source": entry["source"],
            "object_code": object_code
        })

        print(
            f"{int_to_hex(address):<10}"
            f"{entry['source']:<30}"
            f"{object_code}"
        )

    return object_codes


# ==========================================================
# DISPLAY OBJECT CODE
# ==========================================================

def display_object_code(object_codes):

    print("\n")
    print("=" * 75)
    print("                       OBJECT CODE")
    print("=" * 75)

    print(
        f"{'ADDRESS':<12}"
        f"{'SOURCE':<32}"
        f"{'OBJECT CODE':<20}"
    )

    print("-" * 65)

    for item in object_codes:

        object_code = item["object_code"]

        if object_code == "":

            object_code = "--"

        print(
            f"{int_to_hex(item['address']):<12}"
            f"{item['source']:<32}"
            f"{object_code:<20}"
        )   