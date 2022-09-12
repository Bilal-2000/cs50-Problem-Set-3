def main():
    while True:
        try:
            str = input("Fraction: ")
            str = str.split("/")
            x = int(str[0])
            y = int(str[1])
            result = float(x / y)
        except (ValueError, ZeroDivisionError) as err:
            pass
        else:
            if x > y:
                continue
            else:
                break
    check_fuel(result)


def check_fuel(result):
    if result >= 0 and result < 0.125:
        print("E")
    elif result >= 0.125 and result < 0.25:
        print("25%")
    elif result >= 0.25 and result < 0.375:
        print("25%")
    elif result >= 0.375 and result < 0.5:
        print("50%")
    elif result >= 0.5 and result < 0.625:
        print("50%")
    elif result >= 0.625 and result < 0.75:
        print("75%")
    elif result >= 0.75 and result < 0.875:
        print("75%")
    elif result >= 0.875 and result <= 1:
        print("F")


main()
