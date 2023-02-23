def main():
    number = int(input("Enter a whole number between 20 and 100: "))
    good_number = validate(number)
    two = divisible_by_two(good_number)
    three = divisible_by_three(good_number)
    five = divisible_by_five(good_number)
    output(good_number, two, three, five)


def validate(num):
    if 20 <= num <= 100:
        return num
    else:
        while num < 20 or num > 100:
            print("this isn't a valid number")
            num = int(input("Enter a whole number between 20 and 100:"))
        else:
            return num


def divisible_by_two(num):
    if num % 2 == 0:
        return " is divisible by two"
    else:
        return " is not divisible by two"


def divisible_by_three(num):
    if num % 3 == 0:
        return " is divisible by three"
    else:
        return " is not divisible by three"


def divisible_by_five(num):
    if num % 5 == 0:
        return " is divisible by five"
    else:
        return " is not divisible by five"


def output(num, two_div, three_div, five_div):
    print(str(num) + two_div)
    print(str(num) + three_div)
    print(str(num) + five_div)


main()

