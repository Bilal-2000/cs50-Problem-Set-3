def main():
    temp = {}
    count = 1
    while True:
        try:
            item = input("Item: ").lower()
        except KeyboardInterrupt:
            # To print a free line after exception is catch
            print()
            sort = sorted(temp)
            for index, val in enumerate(sort):
                # Using temp as: it is dict and get function cannot apply on sort as sorted returns a list
                print(temp.get(val), sort[index].upper())
            break
        else:
            if temp == {}:
                temp.update({item: count})
            elif item in temp.keys():
                count += 1
                temp.update({item: count})
            else:
                count = 1
                temp.update({item: count})


main()
