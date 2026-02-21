from pathlib import Path
p=Path(r'c:\Users\shivs\OneDrive\Desktop\gla\app\services\ai_service.py')
s=p.read_text()
print('lines', len(s.splitlines()))
print('triple_quotes', s.count('"""'))
for i,line in enumerate(s.splitlines(),1):
    if '"""' in line:
        print(i, line)
    if 'f"""' in line:
        print(' f-string at', i)
