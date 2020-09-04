count = 0


def str_count(string, sub_string):
    global count
    if len(string) <= 1:
        return count
    if string[0] != sub_string[0] :
        return str_count(string[1:],sub_string)

    if string[:len(sub_string)] == sub_string:
        count += 1

    return str_count(string[len(sub_string)-1:],sub_string)