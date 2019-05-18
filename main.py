def find_percent_proportion(expected_percentage):
    """ Algorithm: find_percent_proportion
        expected_percentage <- VALUE FROM 1 TO 100
        START
            percentage <- 0
            number <- 99
            bouncy_numbers <- 0
            WHILE percentage NOT EQUAL expected_percentage
                number <- number + 1
                
                IF bouncy_number ( convert_integer_to_list ( number ) ) IS TRUE
                    bouncy_numbers <- bouncy_numbers + 1

                    percentage <- proportion_bouncy_numbers( number, bouncy_numbers )

            PRINT "NUMBER" + number + "PERCENTAGE" + percentage
        END
    """
    percentage = 0
    number = 99
    bouncy_numbers = 0

    while percentage != expected_percentage:
        number = number + 1

        if bouncy_number(convert_integer_to_list(number)) is True:
            bouncy_numbers = bouncy_numbers + 1

            percentage = proportion_bouncy_numbers(number, bouncy_numbers)

    return number, percentage


def increasing_number(numbers_list):
    """ Algorithm: increasing_number

    numbers_list <- INTEGER LIST
    START
        LOOP OVER numbers_list REVERSE
            IF not current_number GREATER than or EQUAL to nex_number
                RETURN FALSE

        RETURN TRUE
    END
    """
    index = 0
    # Reverse list
    numbers_list = numbers_list[::-1]

    for number in numbers_list:
        if len(numbers_list) - 1 > index and not number >= numbers_list[index + 1]:
            return False

        index += 1

    return True


def decreasing_number(numbers_list):
    """ Algorithm: decreasing_number

    numbers_list <- INTEGER LIST
    START
        LOOP OVER numbers_list
            IF not current_number GREATER than or EQUAL to nex_number
                RETURN FALSE

        RETURN TRUE
    END
    """
    index = 0

    for number in numbers_list:
        if len(numbers_list) - 1 > index and not number >= numbers_list[index + 1]:
            return False

        index += 1

    return True


def bouncy_number(numbers_list):
    """ Algorithm: bouncy_number
    numbers_list <- INTEGER LIST
    START
        IF increasing_number IS FALSE AND decreasing_number IS FALSE
            RETURN TRUE

        RETURN FALSE
    END
    """
    if increasing_number(numbers_list) is False and decreasing_number(numbers_list) is False:
        return True

    return False
 
 
def convert_integer_to_list(number):
    """ Algorithm: convert_integer_to_list
    number <- INTEGER
    START
        CONVERT number TO LIST
        RETURN LIST
    END
    """
    if not type(number) in [int]:
        raise TypeError('number must be a integer')

    if number < 0:
        raise ValueError('The number cannot be negative')

    return list(map(int, str(number)))


def proportion_bouncy_numbers(numbers, bouncy_numbers):
    """ Algorithm: proportion_bouncy_numbers
    numbers <- INTEGER
    bouncy_numbers <- INTEGER
    START
        percentage <- (bouncy_numbers * 100) / numbers

        RETURN percentage
    END
    """
    if numbers <= 0:
        raise ValueError('numbers variable must be greater than zero')

    return (bouncy_numbers * 100) / numbers


if __name__ == "__main__":
    # TODO: received dynamic parameter
    number, percentage = find_percent_proportion(99)

    print('{number} least number for which the proportion of bouncy numbers is {percentage}%'.format(
        number=number, percentage=percentage
    ))
