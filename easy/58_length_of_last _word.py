def length_of_last_word(s: str) -> int:
    words: list = list(filter(lambda x: x.isalpha(), s.split(' ')))
    return len(words[-1])


string1 = 'Hello World'
string2 = '   fly me   to   the moon  '
string3 = 'luffy is still joyboy'
string4 = 'Today is a nice day'

max_len = length_of_last_word(string1)
assert max_len == 5
max_len = length_of_last_word(string2)
assert max_len == 4
max_len = length_of_last_word(string3)
assert max_len == 6
max_len = length_of_last_word(string4)
assert max_len == 3
