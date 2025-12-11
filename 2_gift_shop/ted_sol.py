RANGE_DOC = 'ted_ranges.txt'

def get_values(fn):
    """Returns a list of numbers in the specified range"""
    with open(fn, 'r') as f:
        for rg in f.readline().split(','):
            for v in range(int(rg.split('-')[0]), int(rg.split('-')[1]) + 1):
                yield str(v)

def is_repeat(v):
    """Test if a number string is a pattern repeated twice"""
    if len(v) % 2 == 0:
        return v[:len(v) // 2] == v[len(v) // 2:]
    return False

def sub_divide(v: str, div: int) -> list[str]:  # Where len(list) == div or None
    if len(v) % div == 0:
        step = len(v) // div
        return [v[step*i:step*i + step] for i in range(div)]

def all_eq(vs):
    if vs is not None:
        return len(set(vs)) <= 1
    return False


def part_1():
    inv_cnt = 0
    for v in get_values(RANGE_DOC):
        if is_repeat(v):
            inv_cnt += int(v)
    return inv_cnt

def part_2():
    inv_cnt = 0
    for v in get_values(RANGE_DOC):
        for div in range(2, len(v) + 1):
            if all_eq(sub_divide(v, div)):
                inv_cnt += int(v)
                break
    return inv_cnt


import time
s = time.time()
# print(part_1())
print(part_2())
e = time.time()
print(e-s)