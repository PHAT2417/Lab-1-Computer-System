# Lab 1 Assignment
# Group 7 - Xuan Phat Tran, Kristine Nguyen, Fernanda Lugo
# 09/06/2026
# Program description:

#Fernanda Lugo's part:
# Checks whether the number entered is a legal decimal or binary number
def is_legal_number(number, number_type):
    decimal_points = 0
    digit_count = 0

    # The input cannot be empty
    if number == "":
        return False

    for character in number:

        # Allow only one decimal point for floating-point numbers
        if character == ".":
            decimal_points += 1

            if decimal_points > 1:
                return False

        # Decimal numbers can only contain digits 0 through 9
        elif number_type == "decimal":
            if character < "0" or character > "9":
                return False

            digit_count += 1

        # Binary numbers can only contain 0 and 1
        elif number_type == "binary":
            if character != "0" and character != "1":
                return False

            digit_count += 1

        # Reject an invalid number type
        else:
            return False

    # Reject an entry containing only a decimal point
    if digit_count == 0:
        return False

    return True
#Kristine Nguyen's part:



#Xuan Phat Tran's part:
