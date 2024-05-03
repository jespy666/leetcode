def my_atoi(s: str) -> int:
    lst = s.split(' ')
    digit = list(map(lambda x: x.replace('-', ''), lst))
    is_negative = '-' in s
    number = int(list(filter(lambda x: x.isdigit(), digit))[0])
    if is_negative:
        return number - (number * 2)
    return number

