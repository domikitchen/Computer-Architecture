import sys


PRINT_BEEJ = 1
HALT = 2
SAVE_REG = 3
PRINT_REG = 4
PUSH = 5
POP = 6

memory = [0] * 256

register = [0] * 8

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
    sys.exit(2)

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

    elif instruction == PUSH:
        # Decrement the stack pointer
        register[7] -= 1

        # Grab the value out of the given register
        pc += 1
        reg_num = memory[pc] # this is what we want to push
        value = register[reg_num]

        # Copy the value onto the stack
        top_of_stack_addr = register[7]
        memory[top_of_stack_addr] = value

        pc += 1

        print(memory[0xf0:0xf4])

    elif instruction == POP:
        # Get value from top of stack
        top_of_stack_addr = register[7]
        value = memory[top_of_stack_addr] # Want to put this in a reg...

        # Store in a register
        pc += 1
        reg_num = memory[pc]
        register[reg_num] = value

        # Increment the SP
        register[7] += 1

        pc += 1

    else:
        print(f'fucked up')
        sys.exit(1)
