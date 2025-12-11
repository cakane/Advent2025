from pathlib import Path 
doc_path = Path('ted_doc.txt')
arrow_location = 50
zero_count = 0
for line in doc_path.read_text().splitlines():
    if line.startswith('L'):
        arrow_location -= int(line[1:])
    if line.startswith('R'):
        arrow_location += int(line[1:])
    if arrow_location % 100 == 0:
        zero_count += 1 
print(zero_count)
