def BDAY():
    err_occur = []
    out = open('Birthday_out.txt', 'w')
    j = 0
    try:
        with open('Birthday.txt', 'rt') as in_file:
            for linenum, line in enumerate(in_file):
                if line.find(substr) != -1:
                    err_occur.append((linenum, line.rstrip('\n')))
                    for linenum, line in err_occur:
                        print("Line ", linenum, ": ", line, sep='')
                    out.write(line + '\n')
                    j = 1
    except FileNotFoundError:
        print("Log file not found.")
    if j == 0:
        print('Not found!')
print("""Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace""")
substr = str(input("Who's birthday do you want to look up? "))
BDAY()
