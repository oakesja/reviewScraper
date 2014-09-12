import string
import re


def take_first(x):
    if valid_list(x):
        return remove_whitespace(x[0])
    else:
        return None


def gamespot_review_link(x):
    if valid_list(x):
        return "http://www.gamespot.com" + x[0]
    else:
        return None


def take_all_comma(x):
    return do_take_all(x, ', ')


def take_all(x):
    return do_take_all(x, ' ')


def do_take_all(x, sep):
    if valid_list(x):
        words = map(lambda y: remove_whitespace(y), x)
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


def remove_whitespace(s):
    return re.sub( '\s+', ' ', s ).strip()