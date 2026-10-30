# Mason Colacicco
# 2/6/2026
# Main file

# Fill string with 0
# "string".zfill(4)

option = 0

while option < 4:
    option = int(input("What number would you like to convert?\n"
          "1 - Decimal to Binary\n"
          "2 - Binary to Decimal\n"
          "3 - Binary multiplication\n"))
    if option == 1:
        n = int(input("Write a decimal number to convert: "))
        bin_str = ""
        groups = []
        # Loop while n is over 0, as it will be decreased in the function
        while n > 0:
            # Remainder
            remain = n % 2
            # Place bit at the front
            bin_str = str(remain) + bin_str
            # floor division
            n = n // 2
        while bin_str:
            groups.insert(0, bin_str[-4:])
            bin_str = bin_str[:-4]
        groups[0] = groups[0].zfill(4)
        for group in groups:
            print(group)
    elif option == 2:
        n = str(input("Write a binary number to convert: "))
        power = len(n) - 1
        decimal = 0
        for i in n:
            if i == "1":
                decimal += 2**power
            power = power - 1
        print(decimal)
    elif option == 3:
        n1 = str(input("Write the first number: "))
        n2 = str(input("Write the second number: "))
        power1 = len(n1) - 1
        power2 = len(n2) - 1
        decimal1 = 0
        decimal2 = 0
        for i in n1:
            if i == "1":
                decimal1 += 2 ** power1
            power1 = power1 - 1
        for i in n2:
            if i == "1":
                decimal2 += 2 ** power2
            power2 = power2 - 1
        big_num = decimal1 * decimal2
        print(decimal1, "*", decimal2, "=", big_num)
        bin_str = ""
        groups = []
        # Loop while n is over 0, as it will be decreased in the function
        while big_num > 0:
            # Remainder
            remain = big_num % 2
            # Place bit at the front
            bin_str = str(remain) + bin_str
            # floor division
            big_num = big_num // 2
        while bin_str:
            groups.insert(0, bin_str[-4:])
            bin_str = bin_str[:-4]
        groups[0] = groups[0].zfill(4)
        for group in groups:
            print(group)
    else:
        print("Cya!")
        exit(0)
