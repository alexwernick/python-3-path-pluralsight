def find_acronym():
    look_up = input("What software acronym would you like to look up?\n")

    found = False
    try:
        with open('acronyms.txt') as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print('File not found')
        return

    if not found:
        print('The acronym does not exist')

def add_acronym():
    acronym = input("What acronym would you like to add?\n")
    definition = input("Whatis the definition?\n")

    with open('acronyms.txt', 'a') as file:
        file.write(acronym + ' - ' + definition + '\n')

def main():
    choice = input("do you want to find(F) or add(A) an acronym?")
    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()
    
main()
    