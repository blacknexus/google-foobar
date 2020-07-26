import re

def solution(s):
    aggregate = ""
    pos = 0
    aggregate += s[pos]
    check = s.replace(aggregate, "")
    count = len(re.findall(aggregate, s))
    while check:
        pos += 1
        aggregate += s[pos]
        check = s.replace(aggregate, "")
        count = len(re.findall(aggregate, s))
    return count
