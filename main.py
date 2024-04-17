def dec_to_bin(n):
    """Function to convert decimal to binary and remove the 0b from the
    beginning of the binary number"""
    return bin(n).replace("0b", "")


def check_palindrome(n):
    """Function to take the binary number (bin_num) and reverse it (nib_num)
    then check to see if the numbers are the same and therefore a palindrome"""

    bin_num = dec_to_bin(dec)
    nib_num = bin_num[::-1]

    if bin_num == nib_num:
        return "This is a binary palindrome!"
    else:
        return "This is not a binary palindrome."


while True:
    try:
        # Take user input of a decimal number
        dec = int(input("Input an integer in decimal: "))

        # Output of the decimal and converted number
        print(f"Decimal number: {dec}\nBinary number: {dec_to_bin(dec)}")
        print(check_palindrome(dec))
        check_again = input("Check Another (y/n)? ")
        if check_again.lower() == "y":
            pass
        else:
            break

    except ValueError:  # Error handling for non valid entries
        print("Enter a valid number")
