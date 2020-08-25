import math

def inputNumber(message):
    while True:
        try:
            num = int(input(message))
            return num
        except Exception:
            print("Invalid input! :(")

def main():
    while True:
        print(
"""(1) + Addition
(2) - Subtraction
(3) * Multiplication
(4) / Division
(5) Remainder
(6) Power
(7) Sin
(8) Cos
(9) Quit""")
        
        selection = inputNumber("Make your choice (1-9): ")

        if selection == 1:
            print("=", inputNumber("Number 1: ") + inputNumber("Number 2: "))

        elif selection == 2:
            print("=", inputNumber("Number 1: ") - inputNumber("Number 2: "))

        elif selection == 3:
            print("=", inputNumber("Number 1: ") * inputNumber("Number 2: "))

        elif selection == 4:
            print("=", int(inputNumber("Number 1: ") / inputNumber("Number 2: ")))
            
        elif selection == 5:
            print("=", inputNumber("Number 1: ") % inputNumber("Number 2: "))
            
        elif selection == 6:
            print("=", inputNumber("Number: ") ** inputNumber("To power: "))

        elif selection == 7:
            print("=", math.sin(inputNumber("Number 1: ") / inputNumber("Number 2: ")))

        elif selection == 8:
            print("=", math.cos(inputNumber("Number 1: ") / inputNumber("Number 2: ")))

        elif selection == 9:
            break       

        else:
            print("Invalid input! :(")

if __name__ == "__main__":
    main()
