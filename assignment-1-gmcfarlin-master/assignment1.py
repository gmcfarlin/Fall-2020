"""
Assignment1 ME369P
Name: Grant McFarlin
EID : gjm923

Fill in the 3 functions below
"""

def scifi_faves():
    # Open file
    file = open('scifibookfavorites.txt', 'r')

    # Get the right lines from the file
    # Lines that start with numbers are good lines
    numbers = [str(i) for i in range(0,10)]

    good_lines = [line for line in file.readlines() if line[0] in numbers]

    author_log = []
    dict = {}

    for line in good_lines:

        # Unpack each good line
        stuff, author_name = line.split('--')

        # Count number of nominations (can be double digit numbers)
        if stuff[1] in numbers:
            nomination = int(stuff[0:2])
        else:
            nomination = int(stuff[0])

        # Create log of authors to check for duplicates
        if author_name not in author_log:
            author_log.append(author_name)
            book_total = 1
            nomination_total = nomination
        # if duplicate: add one to the number of books, add nominations from line
        else:
            book_total, nomination_total = dict[author_name]
            book_total += 1
            nomination_total += nomination

        # store information into dictionary

        dict[author_name] =  [book_total, nomination_total]

    # format the final string
    sorted_dict_tuple = sorted(dict.items(), key=lambda e: e[0])
    sorted_dict_tuple = sorted(sorted_dict_tuple, key=lambda e: e[1][1], reverse=True)
    string_list = ''

    for tuple in sorted_dict_tuple:
        author_name, [books, nominations] = tuple
        author_last_name = author_name.split(',')[0]
        string_list += "{}: ".format(author_last_name)

        if books == 1 and nominations == 1:
            string_list += "1 book, with 1 total nomination\n"
        elif nominations == 1:
            string_list += f"{books} books with 1 total nomination\n"
        elif books == 1:
            string_list += f"1 book with {nominations} total nominations\n"
        else:
            string_list += f"{books} books with {nominations} total nominations\n"

    print(string_list)



def animal_col():
    # import relevant pkgs.
    import re
    import random

    # open the file
    file = open('collecti.txt')

    dict = {}

    # parse the file for relevant information
    for line in file.readlines():
        # find all words in each line using regular expression
        words = re.findall('\w+', line)

        # create dictionary
        if len(words) >= 2:
            value = words[0]
            key = words[1:]
            for i in key:
                dict[i] = value

    # user prompt sequence
    while True:
        search = input('What type of animal are you running from? ').lower()
        # basic plurality check (geese won't work, sadly)
        search = search + 's' if search[-1] != 's' else search

        num = random.randint(0,len(dict))

        # if user wants to exit (plural statement adds s)
        if search in ['exits', 'quits']:
            group = list(dict.values())[num]
            animal = list(dict.keys())[num]
            print(f"A {group} of {animal} got you!\n*Exit*")
            break
        # base lookup case
        elif search in list(dict.keys()):
            group = dict[search]
            animal = search
        # not in dictionary case
        else:
            group = list(dict.values())[num]
            animal = search
        # final string
        print(f"A {group} of {animal} is coming to git you!")


def calculator():

    while True:
        operator = input('Enter operation: ')
        result = 0.0

        if operator == 'q':
            break
        else:
            num1 = input('Enter first number: ')
            num2 = input('Enter second number: ')
            num1 = float(num1) if num1 != '' else 0.0
            num2 = float(num2) if num2 != '' else 0.0

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        elif operator == '^':
            result = num1 ** num2

        result = round(result,1)

        print(result)



if __name__ == '__main__':
    scifi_faves()
    animal_col()
    calculator()
    print("Done")
