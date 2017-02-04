import sqlite3
import time
import timeit

usernames = [
    'Ace',
    'Amy',
    'Ana',
    'Ann',
    'Bea',
    'Ben',
    'Bob',
    'Bud',
    'Dan',
    'Doc',
    'Don',
    'Eve',
    'Fay',
    'Gus',
    'Hal',
    'Jon',
    'Kim',
    'Lee',
    'Leo',
    'Lou',
    'Luc',
    'Max',
    'Meg',
    'Mel',
    'Mia',
    'Moe',
    'Ray',
    'Rob',
    'Ron',
    'Roy',
    'Sal',
    'Sam',
    'Sid',
    'Ted',
    'Tim',
    'Tod',
    'Tom',
    'Vic',
    'Zed',
    'Zoe'
]

projects = [
    'Alien',
    'Avatar',
    'Batman',
    'Brazil',
    'Fargo',
    'Goodfellas',
    'Manhattan',
    'Memento',
    'Oldboy',
    'Psycho',
    'Superman',
    'Thor',
    'Titanic',
    'Tron',
    'Twins',
    'Vertigo',
    'Watchmen',
    'Zombieland',
]

department = [
    'anim',
    'comp',
    'dev',
    'fx',
    'lighting',
    'mm',
    'model',
    'roto',
]

task = [
    'anim',
    'cleanup',
    'cloth',
    'cloud',
    'comp',
    'dust',
    'fluid',
    'grade',
    'hair',
    'light',
    'lookdev',
    'particles',
    'render',
    'rgb',
    'rig',
    'roto',
    'sim',
    'techanim',
    'track',
    'water',
]

SCHEMA = """
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS project;
DROP TABLE IF EXISTS task;
DROP TABLE IF EXISTS department;

CREATE TABLE user (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT UNIQE
);

CREATE TABLE project (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT UNIQE
);

CREATE TABLE task (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT UNIQE
);

CREATE TABLE department (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT UNIQE
);
"""


DB_FILE ='vfxhouse.db'


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print ('::', func.__name__, '--> elapsed time:', time.time() - start)
        return result
    return wrapper


@timer
def create_db():
    with sqlite3.connect(DB_FILE) as con:
        cursor = con.cursor()
        cursor.executescript(SCHEMA)


@timer
def fill_table_user():
    sql_template = 'INSERT INTO user VALUES ({id}, "{name}");\n'
    sql = ''

    for idx, name in enumerate(usernames):
        sql = sql + sql_template.format(id=idx, name=name)

    with sqlite3.connect(DB_FILE) as con:
        cursor = con.cursor()
        cursor.executescript(sql)


@timer
def fill_table_user_2():
    sql_template = 'INSERT INTO user VALUES ({id}, "{name}");'

    with sqlite3.connect(DB_FILE) as con:
        cursor = con.cursor()

        for idx, name in enumerate(usernames):
            sql = sql_template.format(id=idx, name=name)
            cursor.execute(sql)

@timer
def fill_table_user_3():
    sql_template = 'INSERT INTO user VALUES (?, ?);'
    data = [(idx, name) for idx, name in enumerate(usernames)]

    with sqlite3.connect(DB_FILE) as con:
        cursor = con.cursor()

        cursor.executemany(sql_template, data)
    #     for idx, name in enumerate(usernames):
    #         sql = sql_template.format(id=idx, name=name)
    #         cursor.execute(sql)



def main():
    create_db()
    fill_table_user()
    create_db()
    fill_table_user_2()
    create_db()
    fill_table_user_3()

    # stmt, setup = 'fill_table_user()', 'from __main__ import fill_table_user'
    # t1 = timeit.repeat(stmt=stmt, setup=setup, repeat=3, number=5)
    # print('\n'.join([str(k) for k in t1]))




if __name__ == '__main__':
    main()