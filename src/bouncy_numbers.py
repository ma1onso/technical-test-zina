def find_percentage_proportion(expected_percentage=99):
    """ Stop when find expected percentage proportion for bounty numbers

    :param int expected_percentage: expected porcentage
    :return: number and percentage for bounty numbers
    :rtype: tuple
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


def increasing_number(numbers):
    """ Working from left-to-right if no digit is exceeded by the digit to
    its left it is called an increasing number; for example, 134468

    :param list numbers: split number into a list
    :return: True if number is increasing, False if not
    :rtype: bool
    """
    index = 0
    # Reverse list
    numbers = numbers[::-1]

    for number in numbers:
        if len(numbers) - 1 > index and not number >= numbers[index + 1]:
            return False

        index += 1

    return True


def decreasing_number(numbers):
    """ Working from left-to-right if no digit is exceeded by the digit to its
    right it is called a decreasing number; for example, 66420

    :param list numbers: split number into a list
    :return: True if number is decreasing, False if not
    :rtype: bool
    """
    index = 0

    for number in numbers:
        if len(numbers) - 1 > index and not number >= numbers[index + 1]:
            return False

        index += 1

    return True


def bouncy_number(numbers):
    """ We shall call a positive integer that is neither increasing nor
     decreasing a "bouncy" number; for example, 155349

    :param list numbers: split number into a list
    :return: True if number is bouncy, False otherwise
    :rtype: bool
    """
    if increasing_number(numbers) is False and decreasing_number(numbers) is False:
        return True

    return False
 
 
def convert_integer_to_list(number):
    """ Convert positive integer to list. Example 859 -> [8, 5, 9]

    :param int number: positive integer
    :return: number split in a list
    :rtype: list
    """
    if not type(number) in [int]:
        raise TypeError('number must be a integer')

    if number < 0:
        raise ValueError('The number cannot be negative')

    return list(map(int, str(number)))


def proportion_bouncy_numbers(number, bouncy_numbers):
    """ Calculate percentage for proportion of bouncy numbers

    :param int number: current positive integer number
    :param int bouncy_numbers: quantity of bouncy numbers discovered
    :return: percentage
    :rtype: float
    """
    if number <= 0:
        raise ValueError('number variable must be greater than zero')

    if bouncy_numbers > number:
        raise ValueError('Not is possible that bouncy numbers must be greater than number')

    return (bouncy_numbers * 100) / number
