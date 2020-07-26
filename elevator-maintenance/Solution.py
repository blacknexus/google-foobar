def solution(l):
    l.sort(key=lambda y: [int(x) for x in y.split('.')])
    return l
