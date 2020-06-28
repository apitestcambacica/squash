#!/usr/bin/env python3

import csv
import sys

def create_file(filename):
    with open(filename, 'w', encoding='UTF-8') as file:
        file.write('Josuneu Araujo,jaraujo@gmail.com\n')
        file.write('Anderson Silva,asilva@gmail.com\n')
        file.write('Juliet Lewis,jlewis@gmail.com\n')
        file.write('Moreira Salles,msalles@gmail.com\n')
        file.write('Antonio Carlos,acarlos@gmail.com\n')

create_file('../text_files/user_emails.csv')


def populate_dictionary(filename):
    email_dict = {}
    with open(filename) as csvfile:
        lines = csv.reader(csvfile, delimiter = ',')
        for row in lines:
            name = str(row[0].lower())
            email_dict[name] = row[1]
        return email_dict

def find_email(argv):
    try:
        fullname = str(argv[1] + ' ' + argv[2])
        email_dict = populate_dictionary('../text_files/user_emails.csv')
        if email_dict.get(fullname.lower()):
            return email_dict.get(fullname.lower())
        else:
            return 'No email address found'
    except IndexError:
        return 'Missing parameters'
def main():
    print(find_email(sys.argv))

if __name__ == '__main__':
    main()