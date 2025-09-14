""" whatsyourname.py """
def main():
    """ whatsyourname.py """
    first_name = input('Hey, what\'s your first name?: ')
    last_name = input('And your last name? : ')
    whole_name = first_name + ' ' + last_name
    return f'Well, pleased to meet you, {whole_name}.'

print(main())
