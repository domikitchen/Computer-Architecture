"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.register = [0,0,0,0,0,0,0,0]
        self.PC = 0
        self.InTheWorks = True
        self.HALT = 1
        self.LDI = 130
        self.PRN = 71
        self.MUL = 162
        self.registerThing = 0

    def ram_read(self, MAR):
        return self.memory[MAR]
    
    def ram_write():
        pass

    def load(self):
        """Load a program into memory."""

        address = 0

        if len(sys.argv) != 2:
            print("usf;kj")
            sys.exit(1)

        try:
            with open(sys.argv[1]) as f:
                for line in f:
                    line = line.strip()
                    
                    if line == '' or line[0]  == "#":
                        continue

                    try:
                        str_value = line.split("#")[0]
                        value = int(str_value, 2)
                    
                    except ValueError:
                        print(f"Invalid number: {str_value}")
                        sys.exit(1)

                    self.ram[address] = value

                    address += 1

        except FileNotFoundError:
            print(f"File not found: {sys.argv[1]}")

        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.register[self.registerThing] = reg_a + reg_b
        elif op == "SUB":
            self.register[self.registerThing] = reg_a - reg_b
        elif op == "MUL":
            self.register[self.registerThing] = reg_a * reg_b
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        while self.InTheWorks == True:
            if self.ram[self.PC] == self.HALT:
                self.PC += 1
                break

            elif self.ram[self.PC] == self.LDI:
                self.PC += 1
                thing = self.ram[self.PC]
                self.PC += 1
                self.register[thing] = self.ram[self.PC]
                self.PC += 1

            elif self.ram[self.PC] == self.PRN:
                self.PC += 1
                self.registerThing = self.ram[self.PC]
                print(self.register[self.registerThing])
                self.PC += 1

            elif self.ram[self.PC] == self.MUL:
                self.PC += 1
                num1 = self.register[self.ram[self.PC]]
                self.PC += 1
                num2 = self.register[self.ram[self.PC]]
                self.alu("MUL", num1, num2)
                self.PC += 1

            else:
                print(f'{self.ram}\n{self.register}\n{self.ram[self.PC]}\n{self.PC}')
                print("------------------")
                print("WhAT dID YOu DO?!?")
                sys.exit(1)