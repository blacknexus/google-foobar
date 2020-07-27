from __future__ import division
#Python 2.7.13? Really? Weak move

def end_radius(start_radius, gaps):
    diff = start_radius
    for value in gaps:
        if diff > 0:
            diff = value - diff
        else:
            return None
    return diff

def solution(pegs):
    gaps = []
    for index, item in enumerate(pegs):
        try:
            gaps.append(pegs[index+1] - item)
        except:
            pass

    count = 0
    found = None
    while count < len(pegs)-2:
        start_radius = 2
        current_gap = gaps[count]
        next_gap = gaps[count +1]
        while start_radius < current_gap:
            current_radius = current_gap - start_radius
            next_radius = next_gap - current_radius
            if next_radius < 1:
                start_radius += 2
            else:
                end = end_radius(start_radius, gaps)
                if not end:
                    start_radius += 2
                else:
                    if start_radius/end == 2:
                        found = start_radius
                        return [found, 1]
                    else:
                        start_radius += 2
        count += 1
    if not found:
        return [-1, -1]