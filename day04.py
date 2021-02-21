def has_repeated_digits(text, start=0):
    return (
        False if start >= len(text) - 1
        else True if text[start] == text[start+1]
        else has_repeated_digits(text, start+1)
    )


def is_password(text):
    return (
        len(text) == 6
        and has_repeated_digits(text)
        and list(text) == sorted(text)
    )


assert is_password('111111')
assert not is_password('223450')
assert not is_password('123789')


START, END = 128392, 643281
INPUTS = list(map(str, range(START, END + 1)))
print(sum(map(is_password, INPUTS)))


# TODO: Make this a generator, part a only needs to go until it finds
#       a digit with count > 1. Part b stays as is.
def get_counts(text, start=0, counts=None):

    counts = counts[:] if counts is not None else [(text[start], 0)]

    if start >= len(text):
        return counts
    else:
        prev_digit, prev_count = counts[-1]
        curr_digit = text[start]
        if prev_digit == curr_digit:
            counts[-1] = (prev_digit, prev_count + 1)
        else:
            counts.append((curr_digit, 1))
        return get_counts(text, start+1, counts)


def has_n_repeated_digits(text, n=2):
    counts = get_counts(text)
    return 2 in [c[1] for c in counts]


def is_password_2(text):
    return (
        len(text) == 6
        and has_n_repeated_digits(text, n=2)
        and list(text) == sorted(text)
    )


assert is_password_2('112233')
assert not is_password_2('123444')
assert is_password_2('111122')
assert is_password_2('123345')


print(sum(map(is_password_2, INPUTS)))


# def iter_counts(text, start=0, counts=None):

#     counts = counts[:] if counts is not None else [(text[start], 0)]

#     if start >= len(text):
#         return counts
#     else:
#         prev_digit, prev_count = counts[-1]
#         curr_digit = text[start]
#         if prev_digit == curr_digit:
#             counts[-1] = (prev_digit, prev_count + 1)
#         else:
#             counts.append((curr_digit, 1))
#         return get_counts(text, start+1, counts)


# def has_two_repeated_digits(text):
#     counts = get_counts(text)
#     if


#     if counts is None:
#         return has_two_repeated_digits(text, pos+1, counts=[(text[0], 1)])
#     else:
#         result =


#     first = text[start]
#     try:
#         second = text[start+1]
#     except IndexError:
#         return False

#     if first == second:

#         try:
#             third = text[start+2]
#         except IndexError:
#             return True

#         if first == third:
#             return has_two_repeated_digits(text, start+1)

#         return True

#     return has_two_repeated_digits(text, start+1)



    # return (
    #     False if start >= len(text) - 1
    #     else True if start >= len(text) - 2 and text[start] == text[start+1]
    #     else False if start < len(text) - 2 and text[start] == text[start+1] == text[start+2]
    #     else True if start < len(text) - 2 and text[start] == text[start+1] == text[start+2]
    #     else has_two_repeated_digits(text, start+1)
    # )


# def is_password_2(text):
#     return (
#         len(text) == 6
#         and has_two_repeated_digits(text)
#         and list(text) == sorted(text)
#     )




# # print(INPUTS)
# # print(sum(map(is_password_2, INPUTS)))
# valids = [i for i in INPUTS if is_password_2(i)]
