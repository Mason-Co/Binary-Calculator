# Mason Colacicco
# 2/6/2026
# Main file

# Fill string with 0
# "string".zfill(4)

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
