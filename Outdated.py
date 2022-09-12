def main():
    month = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12,
    }

    # To produce a list of months number in year
    x = range(0, 13)
    for _ in x:
        month_days = str(list(x))

    # Bool to terminate the infinite loop
    Print = False

    index = 0
    while True:
        if Print:
            break
        text = input("Date: ").replace(",", "")
        text = text.replace("/", ",")
        text = text.replace(" ", ",")
        text = text.split(",")

        months = month.get(text[index])
        # Condition applied to handel the type error i.e if first index is digit
        if months == None:
            if text[index] in month_days:
                first = str(text[index + 2])
                third = str(text[index + 1])
                second = str(text[index])
                if len(second) < 2:
                    second = second.zfill(2)
                if len(third) < 2:
                    third = third.zfill(2)
                print(f"{first}-{second}-{third}")
                Print = True
            # If digit is > 12
            else:
                continue
        dates = int(text[index + 1])

        if dates > 31:
            continue

        # If the first index of text is in Word format
        elif text[index] in month.keys():
            text[index] = month.get(text[index])
            first = str(text[index + 2])
            third = str(text[index + 1])
            second = str(text[index])
            if len(second) < 2:
                second = second.zfill(2)
            if len(third) < 2:
                third = third.zfill(2)
            print(f"{first}-{second}-{third}")
            Print = True


main()
