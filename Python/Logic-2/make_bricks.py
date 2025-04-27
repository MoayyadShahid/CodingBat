def make_bricks(small, big, goal):
    if small + 5 * big < goal:
        return False
    used_big = min(big, goal // 5)
    return small >= goal - used_big * 5
