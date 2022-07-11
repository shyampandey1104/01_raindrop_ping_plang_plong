def convert():
    num = int(input('enter a number: '))

    if num%5 == 0 and num%3 == 0:
        print("pling plang")

    elif num%5 == 0 and num%7 == 0:
        print('Plang plong')

    elif num%3 == 0 and num%7 == 0:
        print('pling plong')

    elif num%3 == 0:
        print('pling')

    elif num%5 == 0:
        print('Plang')

    elif num%7 == 0:
        print('Plong')

    else:
        print(num)
convert()