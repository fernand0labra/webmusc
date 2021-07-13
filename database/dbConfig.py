# -*- coding: utf-8 -*-

import sqlite3

def startDB():
    # Connect to our database
    connection = sqlite3.connect('database/database.db')
    cursor = connection.cursor()

    # Create File Descriptor
    sql_file = [open("database/dbInfo/schema.sql", encoding='UTF-8'), open("database/dbInfo/data.sql", encoding='UTF-8')]

    # Obtain Information as a String
    sql_as_string = [sql_file[0].read(), sql_file[1].read()]

    # Execute scripts for structure and Data
    cursor.executescript(sql_as_string[0])
    cursor.executescript(sql_as_string[1])


def getAuthorInfo(author, ttype):
    # Connect to our database
    connection = sqlite3.connect('database/database.db')
    cursor = connection.cursor()

    return cursor.execute("SELECT Work.Name, Work.Opus " +
                   "FROM Work INNER JOIN Author ON Author.ID = Work.AuthorID " +
                   "WHERE Author.Name = ? AND Work.Form = ?", (author, ttype,)).fetchall()

def getWorkInfo(name, opus):
    # Connect to our database
    connection = sqlite3.connect('database/database.db')
    cursor = connection.cursor()

    return cursor.execute("SELECT Author.Name, Work.Form, Work.Year, Work.Opus, Work.URL " +
                   "FROM Work INNER JOIN Author ON Author.ID = Work.AuthorID " +
                   "WHERE Work.Name = ? AND Work.Opus = ?", (name, opus,)).fetchall()