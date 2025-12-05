from pathlib import Path 
doc_path = Path('document.txt')
arrow_location = 50
zero_count = 0
for line in doc_path.read_text().splitlines():
    #print(line)
    #arrow_location 
    if line.startswith('L'):
        print('hello')
    if line.startswith('R'):
        print('goodbye')
#mod_location = running total mod 100 
#if mod location == 0 increment counter 
#else keep going 

print((doc_path.read_text().splitlines())[0])
