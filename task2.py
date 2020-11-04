file_name = 'book.txt'
read_mode = 'r'

letters = []
frequency = []
try:
    with open(file_name, read_mode) as content:
        for line in content:
            content = line.rstrip('\n')
            for letter in content:
                letter = letter.lower()
                if letter not in letters and ord(letter) >= 97 and ord(letter) <= 122:
                    letters += [letter]
                    frequency += [[letter,1]]
                else:
                    for bracket in frequency:
                        if letter in bracket[0]:
                            frequency[frequency.index(bracket)][1] += 1

    letters.sort()
    summary_file = 'summary.txt'
    write_mode = 'w'
    
    with open(summary_file,'w') as text:
        for letter in letters:
            for bracket in frequency:
                if letter == bracket[0]:
                    text.write(f'{bracket[0].upper()} {bracket[1]}\n')
        if len(letters) == 26:
            text.write(f'It does have all letters')
        else:
            text.write(f'It does NOT have all letters')
except:
    print(f'File {file_name} not found')


    















    
   