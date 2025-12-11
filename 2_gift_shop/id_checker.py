from pathlib import Path 
import time

t1 = time.time()

doc_path = Path('ranges.txt')
ranges_list = doc_path.read_text().split(',')
num_invalid = 0
for i in ranges_list:
    start = int(i.split('-')[0])
    end = int(i.split('-')[1])
    range_list = list(range(start, end + 1))
    for i in range_list:
        length = int(len(str(i)))
        if length % 2 == 0: 
            id = str(i)
            mid = int(length / 2)
            first = id[:mid]
            last = id[mid:]
            if first == last:
                num_invalid += i

t2 = time.time()    
print(num_invalid)
print(t2 - t1)
