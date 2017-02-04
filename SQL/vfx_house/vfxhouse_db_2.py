import sqlite3
import time
import timeit
import random
from collections import defaultdict

user_db = {'Ace': 0, 'Amy': 1, 'Ana': 2, 'Ann': 3, 'Bea': 4, 'Ben': 5, 'Bob': 6,
        'Bud': 7, 'Dan': 8, 'Doc': 9, 'Don': 10, 'Eve': 11, 'Fay': 12, 'Gus': 13,
        'Hal': 14, 'Jon': 15, 'Kim': 16, 'Lee': 17, 'Leo': 18, 'Lou': 19, 'Luc': 20,
        'Max': 21, 'Meg': 22, 'Mel': 23, 'Mia': 24, 'Moe': 25, 'Ray': 26, 'Rob': 27,
        'Ron': 28, 'Roy': 29, 'Sal': 30, 'Sam': 31, 'Sid': 32, 'Ted': 33, 'Tim': 34,
        'Tod': 35, 'Tom': 36, 'Vic': 37, 'Zed': 38, 'Zoe': 39,
}

project_db = {
'Alien': 0,
'Avatar': 1,
'Batman': 2,
'Brazil': 3,
'Fargo': 4,
'Goodfellas': 5,
'Manhattan': 6,
'Memento': 7,
'Oldboy': 8,
'Psycho': 9,
'Superman': 10,
'Thor': 11,
'Titanic': 12,
'Tron': 13,
'Twins': 14,
'Vertigo': 15 ,
'Watchmen': 16,
'Zombieland': 17,
}

department_db = {'anim': 0, 'comp': 1, 'dev': 2, 'fx': 3, 'lighting': 4, 'mm': 5,
        'model': 6, 'roto': 7,
}

task_db = {'anim': 0, 'cleanup': 1, 'cloth': 2, 'cloud': 3, 'comp': 4, 'dust': 5,
        'fluid': 6, 'grade': 7, 'hair': 8, 'light': 9, 'lookdev': 10, 'particles': 11,
        'render': 12, 'rgb': 13, 'rig': 14, 'roto': 15, 'sim': 16, 'techanim': 17,
        'track': 18, 'water': 19,
}


DB_FILE ='vfxhouse.db'


SCHEMA = """
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS project;
DROP TABLE IF EXISTS task;
DROP TABLE IF EXISTS department;
DROP TABLE IF EXISTS user_X_project_id;
DROP TABLE IF EXISTS user_X_department_id;
DROP TABLE IF EXISTS todo;

--PRAGMA foreign_keys = ON;

CREATE TABLE user (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    name            TEXT UNIQE
);

CREATE TABLE project (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    name            TEXT UNIQE
);

CREATE TABLE task (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    name            TEXT UNIQE
);

CREATE TABLE department (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    name            TEXT UNIQE
);

CREATE TABLE user_X_project_id (
    project_id      INTEGER,
    user_id         INTEGER,
    FOREIGN KEY (project_id) REFERENCES project(id),
    FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE user_X_department_id (
    project_id      INTEGER,
    user_id         INTEGER,
    FOREIGN KEY (project_id) REFERENCES project(id),
    FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE todo (
    todo            TEXT,
    user_id         INT,
    task_id         INT,
    project_id      INT,
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (task_id) REFERENCES task(id),
    FOREIGN KEY (project_id) REFERENCES project(id)
);
"""


# --> TABLE DATA:
users_to_project_db = {
    'Alien': ['Ace', 'Bea', 'Rob'],
    'Avatar': ['Ace', 'Max', 'Roy', 'Tod'],
    'Batman': ['Doc', 'Gus', 'Hal', 'Leo', 'Max', 'Rob', 'Ted'],
    'Brazil': ['Rob', 'Vic'],
    'Fargo': ['Ana', 'Bud', 'Roy', 'Sam'],
    'Goodfellas': ['Don', 'Fay', 'Leo', 'Ron', 'Roy', 'Sal', 'Vic'],
    'Manhattan': ['Ann'],
    'Memento': ['Fay', 'Meg', 'Tod'],
    'Oldboy': ['Zed'],
    'Psycho': ['Ana', 'Roy'],
    'Superman': ['Doc', 'Gus'],
    'Thor': ['Bud', 'Don', 'Kim'],
    'Titanic': ['Hal', 'Rob'],
    'Tron': ['Ann', 'Bud', 'Lou', 'Moe', 'Ron'],
    'Twins': ['Bea', 'Fay', 'Mel', 'Moe', 'Ray', 'Tim'],
    'Vertigo': ['Luc', 'Ray', 'Sid'],
    'Watchmen': ['Ace', 'Ana', 'Don', 'Luc', 'Meg', 'Ron'],
    'Zombieland': ['Ana', 'Ann', 'Jon', 'Rob', 'Ted'],
}

users_to_department_db = {
    'anim': ['Lee', 'Leo'],
    'comp': ['Zoe', 'Dan', 'Kim', 'Bob', 'Mel'],
    'dev': ['Tom', 'Luc', 'Rob', 'Jon'],
    'fx': ['Lou', 'Max', 'Moe', 'Ben', 'Ace', 'Doc', 'Ron', 'Ray'],
    'lighting': ['Tod', 'Amy', 'Bud', 'Ana', 'Ann'],
    'mm': ['Mia', 'Don', 'Fay', 'Eve', 'Sam', 'Roy'],
    'model': ['Tim', 'Gus'],
    'roto': ['Hal', 'Meg', 'Zed', 'Bea', 'Vic', 'Sal', 'Ted', 'Sid'],
}


def data_generator():
    print '\n--> user TO project:'
    alluser = sorted(user_db.keys())
    varstring = 'users_to_project_db = {'

    for prj in sorted(project_db):
        usercount = random.randint(1, 8)
        userlist = [random.choice(alluser) for k in range(usercount)]

        varstring += '\n\t\'{0}\': {1},'.format(prj, sorted(list(set(userlist))))

    varstring += '\n}'
    print varstring

    print '\n--> user TO department:'
    varstring = 'users_to_department_db = {'

    dep_to_usr = {usr: random.choice(department_db.keys()) for usr in user_db.keys()}
    usr_to_dep = defaultdict(list)

    for name, dep in dep_to_usr.items():
        usr_to_dep[dep].append(name)

    # print dict(usr_to_dep)
    for dep in sorted(department_db):
        varstring += '\n\t\'{0}\': {1},'.format(dep, usr_to_dep[dep])

    # varstring += ','.join(usr_to_dep)
    varstring += '\n}'
    print varstring



def single_timer(func):
    def wrapper(*args, **kwargs):
        t = time.time
        start = t()
        result = func(*args, **kwargs)
        print '<@> {0:35} - elapsed time: {1}'.format(func.__name__, t() - start)
        return result
    return wrapper

def timer_timer(stmt, r=3, n=10):
    setup = 'from __main__ import ' + stmt[:-2]
    t1 = timeit.repeat(stmt=stmt, setup=setup, repeat=r, number=n)

    print ''.join(['\n'+stmt+': '+str(k/n) for k in t1])


@single_timer
def create_db():
    with sqlite3.connect(DB_FILE) as con:
        cursor = con.cursor()
        cursor.executescript(SCHEMA)


# @single_timer
# !!! SLOWEST !!!
def filltable_user():
    return

    sql_template = 'INSERT INTO user VALUES ({id}, "{name}");\n'
    sql = ''

    for idx, name in enumerate(usernames):
        sql = sql + sql_template.format(id=idx, name=name)

    with sqlite3.connect(DB_FILE) as con:
        cursor = con.cursor()
        cursor.executescript(sql)


# @single_timer
# !!! FASTEST !!!
def filltable_user_2():
    return

    sql_template = 'INSERT INTO user VALUES ({id}, "{name}");'

    with sqlite3.connect(DB_FILE) as con:
        cursor = con.cursor()

        for idx, name in enumerate(usernames):
            sql = sql_template.format(id=idx, name=name)
            cursor.execute(sql)

# @single_timer
# !!! SLOWER !!!
def filltable_user_3():
    return

    sql_template = 'INSERT INTO user VALUES (?, ?);'
    data = [(idx, name) for idx, name in enumerate(usernames)]

    with sqlite3.connect(DB_FILE) as con:
        cursor = con.cursor()

        cursor.executemany(sql_template, data)


@single_timer
def filltable(table, data):
    sql_template = 'INSERT INTO {table} VALUES (:id, :name);'
    sql_template = sql_template.format(table=table)

    with sqlite3.connect(DB_FILE) as con:
        cursor = con.cursor()

        for celldata, rowid in data.items():
            cursor.execute(sql_template, {'id': rowid, 'name': celldata})


@single_timer
def filltable_per_id(table, data):
    sql = 'INSERT INTO {table} VALUES (:prj_id, :usr_id)'.format(table=table)

    with sqlite3.connect(DB_FILE) as con:
        cursor = con.cursor()

        for project in data:
            for user in data[project]:
                cursor.execute(sql, {'prj_id': project, 'usr_id': user})


@single_timer
def filltable_user_X_project_id():
    sql_template = ('INSERT INTO user_X_project_id'
                    ' VALUES (:prjid, :usrid)')

    with sqlite3.connect(DB_FILE) as con:
        cursor = con.cursor()

        for project in sorted(project_db):
            prjid = int(project_db[project])

            for user in users_to_project_db[project]:
                usrid = int(user_db[user])
                cursor.execute(sql_template, {'prjid': prjid, 'usrid': usrid})


@single_timer
def filltable_user_X_department_id():
    sql_template = ('INSERT INTO user_X_department_id'
                    ' VALUES (:depid, :usrid)')

    with sqlite3.connect(DB_FILE) as con:
        cursor = con.cursor()

        for dep in sorted(department_db):
            depid = int(department_db[dep])

            for user in users_to_department_db[dep]:
                usrid = int(user_db[user])
                cursor.execute(sql_template, {'depid': depid, 'usrid': usrid})


@single_timer
def filltable_todo(todocount=100000):
    sql_template = 'INSERT INTO todo VALUES (:td, :usr, :tsk, :prj)'

    with sqlite3.connect(DB_FILE) as con:
        cursor = con.cursor()
        cursor.execute('PRAGMA foreign_keys = ON;')

        for k in range(todocount):
            data = {'td': random.choice(task_db.keys()),
                    'usr': int(user_db[random.choice(user_db.keys())]),
                    'tsk': int(task_db[random.choice(task_db.keys())]),
                    'prj': int(project_db[random.choice(project_db.keys())])
            }

            cursor.execute(sql_template, data)



@single_timer
def main():
    create_db()
        #! filltable_user()
        #! create_db()
        #! filltable_user_2()
        #! create_db()
        #! filltable_user_3()
        #! create_db()
    filltable('user', user_db)
    filltable('project', project_db)
    filltable('department', department_db)
    filltable('task', task_db)
    filltable_user_X_project_id()
    filltable_user_X_department_id()
    filltable_todo()


if __name__ == '__main__':
    main()
    # data_generator()