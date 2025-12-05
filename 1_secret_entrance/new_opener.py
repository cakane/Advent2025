from pathlib import Path 
doc_path = Path('./document.txt')
#doc_path = Path('./test_doc.txt')
arrow_location = 50
zero_count = 0
for line in doc_path.read_text().splitlines():
    dt = int(line[1:])
    zero_count += (dt // 100)
    dt = dt % 100
    if line.startswith('L'):
        if arrow_location != 0 and dt >= arrow_location: 
            zero_count += 1
        arrow_location -= dt    
    if line.startswith('R'):
        if arrow_location != 0 and (arrow_location + dt) >= 100:
            zero_count += 1
        arrow_location += dt    
    arrow_location = arrow_location % 100
print(zero_count)