def reverse(x: int) -> int:
    str_view = str(x)
    return int(str_view[::-1]) if str_view.isdigit() else int(
        '-' + str_view[1:][::-1])


if __name__ == '__main__':
    number1 = 132
    number2 = -123
    print(reverse(number1))
    print(reverse(number2))
    