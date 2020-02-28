'''
Author: Shiyu Cheng (23329948)
ISTA 350 Hw3
date: 02/27/2020
SL: Jacob Heller
This homework is intended to review and extend your knowledge of classes in Python
and to practice storing a program’s state in a database between runs. You will be
 writing the first class in a program that encapsulates the concept behind Facebook.
 We may finish the program later in the semester. Don’t turn in code that hangs the
  test program – this will result in a 0.
'''

import os
import sqlite3, sys


class Person:
    def __init__(self, first="", last="", bday="", email=""):
        '''
        init: Each Person object has four instance variables, called first, last, bday,
         and email, and init has four corresponding string parameters, each of which
         has the empty string as a default argument. The first parameter is the
         Person’s first name, the second the last name, the third his/her birthday,
         and the last the Person’s e-mail. If any of the parameters are the empty
         string, get a value from the user using one of the following prompts
        :param first: string
        :param last: string
        :param bday: string
        :param email: string
        '''
        if first:
            self.first = first
        else:
            self.first = input('Enter person\'s first name: ')
        self.last = last if last else input('Enter person\'s last name: ')
        self.bday = bday if bday else input('Enter person\'s birthday: ')
        self.email = email if email else input('Enter person\'s e-mail: ')

    def __repr__(self):
        '''
        This method returns a string in the following format: 'Rich Thompson: 5/21, rm@g'.
        :return:
        '''
        return self.first + ' ' + self.last + ': ' + self.bday + ', ' + self.email

    @classmethod
    def read_person(cls, file):
        """
        This is a class method that reads the data necessary from a text file to create
        and return a Person instance. It takes one argument, a file object (not a
        filename). It reads a line from the file. If the line is empty, return False.
        Otherwise, use the contents of this and the next three lines as the first name,
        last name, birthday, and e-mail of a new Person. Remember to use the
        classmethod decorator.
        """
        first = file.readline().strip()
        if not first:
            return False
        last = file.readline().strip()
        bday = file.readline().strip()
        email = file.readline().strip()
        return cls(first, last, bday, email)

    def write_person(self, file):
        '''
        This instance method takes one argument, a file object. It writes the instance
         variables, one per line, to the file in this order: first, last, birthday,
         email.
        :param file: file
        :return:
        '''
        file.write(self.first+'\n')
        file.write(self.last+'\n')
        file.write(self.bday+'\n')
        file.write(self.email+'\n')

# ---------------------------------------------------------------------
# ---------------------- FUNCTION METHODS -----------------------------
# ---------------------------------------------------------------------


def open_persons_db():
    '''
    This function returns a connection to a database. Read the os.path documentation
    to learn how to determine if a file exists. Determine whether or not persons.db
    exists and store this information in a variable. Connect to persons.db. Set its
    row_factory to sqlite3.Row. If it's a new database, create friends and colleagues
    tables with column names first, last, bday, and email. These are all TEXT fields.
    email is the primary key. Return the database.
    '''
    exits = False

    if os.path.exists('persons.db'):
        exits = True

    conn = sqlite3.connect('persons.db')
    conn.row_factory = sqlite3.Row

    if not exits:
        c = conn.cursor()
        query_1 = 'CREATE TABLE friends (first TEXT, last TEXT, bday TEXT,email TEXT PRIMARY KEY);'
        query_2 = 'CREATE TABLE colleagues (first TEXT, last TEXT, bday TEXT,email TEXT PRIMARY KEY);'
        c.execute(query_1)
        c.execute(query_2)
        conn.commit()
    return conn


def add_person(person_db, person, friend=True, colleague=False):
    '''
    This function has four parameters. The first is a Person database as described above.
    The second is a Person object. The third is a Boolean with a default argument of
    True that tells the function if the Person is a friend. The last is a Boolean with
    a default argument of False that tells the function if the Person is a colleague.
    Name the last two parameters friend and colleague, respectively (this is necessary
    for testing purposes)
    :param person_db: db
    :param person: Person
    :param friend: boolean
    :param colleague: boolean
    :return: boolean
    '''

    if not friend and not colleague:
        print(f'Warning: {person.email} not added - must be friend or colleague', file=sys.stderr)
        return False
    c = person_db.cursor()
    if friend:
        query = 'INSERT INTO friends (first, last, bday, email) VALUES' \
                ' (?,?,?,?);'
        c.execute(query, (person.first, person.last, person.bday, person.email))
    if colleague:
        query = 'INSERT INTO colleagues (first, last, bday, email) VALUES' \
                ' (?,?,?,?);'
        c.execute(query,(person.first, person.last, person.bday, person.email))
    person_db.commit()
    return True


def delete_person(person_db, person):
    '''
    This function takes a Person database and a Person. Delete the Person from all
    tables.
    :param person_db: db
    :param person: Person
    '''

    c = person_db.cursor()
    query = 'DELETE FROM friends WHERE first=? AND last=? AND bday=? AND email=?'
    c.execute(query,(person.first, person.last, person.bday, person.email))
    query = 'DELETE FROM colleagues WHERE first=? AND last=? AND bday=? AND email=?'
    c.execute(query, (person.first, person.last, person.bday, person.email))
    person_db.commit()


def to_Person_list(cursor):
    '''
    This function takes a cursor object as its sole argument and returns a list of Person
     objects constructed from the data in the rows iterated over by the cursor.
    :param cursor:
    :return: list
    '''
    query = 'SELECT * FROM friends'
    return list(map(_function, cursor.execute(query)))


def get_friends(person_db):
    '''
    This function takes a Person database as its sole argument and returns a list of
    Person objects representing all of the friends in the database.
    :param person_db: db
    :return:list
    '''
    c = person_db.cursor()
    query = 'SELECT * FROM friends'
    return list(map(_function, c.execute(query)))


def get_colleagues(person_db):
    '''
    This function takes a Person database as its sole argument and returns a list of
    Person objects representing all of the colleagues in the database.
    :param person_db: db
    :return: list
    '''
    c = person_db.cursor()
    query = 'SELECT * FROM colleagues'
    return list(map(_function, c.execute(query)))


def get_all(person_db):
    '''
    This function takes a Person database as its sole argument and returns a list of
    Person objects representing all of the friends and colleagues in the database
    without duplicates.
    :param person_db: db
    :return: list
    '''
    c = person_db.cursor()
    query = 'SELECT * FROM colleagues UNION SELECT * FROM friends'
    return list(map(_function, c.execute(query)))


def _function(person):
    '''
    map function
    :param person: Person
    :return: Person
    '''
    return Person(person[0], person[1], person[2], person[3])


def get_and(person_db):
    '''
    This function takes a Person database as its sole argument and returns a list of
    Person objects representing all of the people who are both friends and colleagues
    in the database.
    :param person_db: db
    :return: list
    '''
    c = person_db.cursor()
    query = 'SELECT friends.first, friends.last, friends.bday, friends.email FROM '\
            'friends JOIN colleagues ON friends.email = colleagues.email;'

    return list(map(_function, c.execute(query)))


def main():
    pass


if __name__ == '__main__':
    main()