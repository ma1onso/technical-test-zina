import sys

from src.bouncy_numbers import find_percentage_proportion


if __name__ == "__main__":
    try:
        number, percentage = find_percentage_proportion(int(sys.argv[1]))
    except IndexError:
        number, percentage = find_percentage_proportion()

    print('{number} least number for which the proportion of bouncy numbers is {percentage}%'.format(
        number=number, percentage=percentage
    ))
