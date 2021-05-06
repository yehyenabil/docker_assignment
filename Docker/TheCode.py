punctuations = '''!()-[]{};:”'"“—\,<>./?@#$%^&*_~'''
nopun='                               '
file = open('Beyond the Wall of Sleep.txt', encoding="utf8")
Beyond= file.read()
Beyond = Beyond.translate(str.maketrans(punctuations, nopun))   
file2 = open('Pride and Prejudice.txt', encoding="utf8")
Pride= file2.read()
Pride = Pride.translate(str.maketrans(punctuations, nopun))   
Beyond=Beyond.lower().split()
Pride=Pride.lower().split()
intersection = set(Beyond) & set(Pride)
print(f"Numper of words : {len(intersection)}")
print(intersection)

file.close()
file2.close()