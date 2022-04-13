middle_initials_1 = 'abcdefghij'
middle_initials_2 = 'klmnopqr'
middle_initials_3 = 'stuvwxyz'

vowels = 'aeiıoöuü'
finalname = ''

count = 2


firstname = input("\n Please type your first name for the Zaun Name Genrator:\n")

if firstname.lower()[-1] in vowels:
    finalname += firstname + 'o'
else:
    for i in range(len(firstname)):
        if not firstname.lower()[-count] in vowels:
            count += 1
        else:
            finalname += firstname[:-(count-1)]
            break

middlename = input ("\n Please type your middle name; if you don't have one, press enter\n")
if middlename == '':
    finalname += ' ' + str("Phantom of")
elif middle_initials_1.lower()[0] in middle_initials_1:
    finalname += ' ' + str("Thief of")
elif middlename in middle_initials_2:
    finalname += ' ' + str("Shadow of")
elif middlename in middle_initials_3:
    finalname += ' ' + str("Master of")

month = input("\n Please type the number of the month you were born in: (1-12) \n")
if int(month) in range(6):
    finalname += ' ' + str("The Lanes")
elif int(month) in range(6, 9):
    finalname += ' ' + str ("The Undercity")
elif int(month) in range (9, 13):
    finalname += ' ' + str("Zaun")
print()
print(finalname)
