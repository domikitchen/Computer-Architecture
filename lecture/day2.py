import sys


PRINT_BEEJ = 1
HALT = 2
SAVE_REG = 3
PRINT_REG = 4

memory = [
    1,  # PRINT_BEEJ
    3,  # SAVE_REG R1,37        r1 = 37
    1,  # R1
    37,
    4,  # PRINT_REG R1      print(r[1])
    1,  # R1
    1,  # PRINT_BEEJ
    2   # HALT
]

register = [0,0,0,0,0,0,0,0]

address = 0

if len(sys.argv) != 2:
    print("usage: day2.py da2progname")
    sys.exit(1)

try:
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip()
            
            if line == '' or line[0]  == "#":
                continue

            try:
                str_value = line.split("#")[0]
                value = int(str_value, 10)
            
            except ValueError:
                print(f"Invalid number: {str_value}")
                sys.exit(1)

            memory[address] = value

            address += 1

except FileNotFoundError:
    print(f"File not found: {sys.argv[1]}")

# with open('da2prog2.ls8') as f:
#     for line in f:
#         line = line.strip()

#         if line == "" or line[0] == "#":
#             continue

#         try:
#             str_value = line.split("#")[0]
#             value = int(str_value)

#         except ValueError:
#             print(f"Invalid Number: {str_value}")
#             sys.exit(1)

#         # print(value)
#         memory[address] = value
#         address += 1

pc = 0

halted = False

while not halted:
    instruction = memory[pc]

    if instruction == PRINT_BEEJ:
        print('Beej!')
        pc += 1

    elif instruction == HALT:
        halted = True
        pc += 1

    elif instruction == SAVE_REG:
        pc += 1
        reg_num = memory[pc]
        pc += 1
        value = memory[pc]
        register[reg_num] = value
        pc += 1

    elif instruction == PRINT_REG:
        pc += 1
        reg_num = memory[pc]
        print(register[reg_num])
        pc += 1

    else:
        print(f'fucked up')
        sys.exit(1)
