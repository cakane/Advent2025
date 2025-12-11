RANGE_DOC = 'ranges.txt'

def get_values(fn):
    """Returns a list of numbers in the specified range"""
    with open(fn, 'r') as f:
        for rg in f.readline().split(','):
            for v in range(int(rg.split('-')[0]), int(rg.split('-')[1])):
                yield str(v)

import time
s = time.time()
inv_cnt = 0
for v in get_values(RANGE_DOC):
    if len(v) % 2 == 0:
        if v[:len(v) // 2] == v[len(v) // 2:]:
            inv_cnt += int(v)
            
e = time.time()
print(inv_cnt)
print(e-s)