import string


def take_first(x):
    if valid_list(x):
        return x[0].strip()
    else:
        return None


def take_all_comma(x):
    return do_take_all(x, ', ')


def take_all(x):
    return do_take_all(x, ' ')


def do_take_all(x, sep):
    if valid_list(x):
        words = map(lambda y: y.strip(), x)
        words = filter(lambda y: y != '', words)
        return string.join(words, sep)
    else:
        return None


def valid_list(x):
    return type(x) == list and x != [] and all_strings(x)


def all_strings(ls):
    for x in ls:
        if not hasattr(x, 'strip'):
            return False
    return True