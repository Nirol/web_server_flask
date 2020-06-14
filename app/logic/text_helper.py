
import re

def __dequote(s:str ):

    if (s[0] == s[-1]) and s.startswith(("'", '"')):
        return s[1:-1]
    return s

def __remove_sequence_quote(s: str):
    s_new = re.sub('\"\"','"',s)
    return s_new



def dequote_wrapper(s: str):
    if s.count('"') == 0:
        return s
    s_new = __dequote(s)
    s_clean = __remove_sequence_quote(s_new)
    return s_clean