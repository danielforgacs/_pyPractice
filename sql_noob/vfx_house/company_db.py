artist_list = ['Abel', 'Ace', 'Amy', 'Ana', 'Angel', 'Ann', 'Anna', 'Arthur',
        'Bea', 'Ben', 'Bennett', 'Bob', 'Bruce', 'Bud', 'Carey', 'Chase',
        'Conrad', 'Cyrus', 'Daisey', 'Dan', 'Dana', 'Daniel', 'Daron', 'Debby',
        'Dessie', 'Doc', 'Don', 'Doug', 'Duane', 'Eddie', 'Elliott', 'Erick',
        'Ernesto', 'Eve', 'Fay', 'Franklyn', 'Garrett', 'Garry', 'Gary', 'Gus',
        'Hal', 'Hubert', 'Jame', 'Jarvis', 'Jillian', 'Jon', 'Kareem', 'Karl',
        'Kim', 'Lee', 'Leo', 'Lou', 'Luc', 'Marcelo', 'Marion', 'Mathew', 'Max',
        'Maynard', 'Meg', 'Mel', 'Mervin', 'Mia', 'Milo', 'Mitchel', 'Moe',
        'Nickolas', 'Noble', 'Norris', 'Osvaldo', 'Pearl', 'Perry', 'Ray', 'Reed',
        'Reena', 'Rob', 'Roderick', 'Ron', 'Roy', 'Rudolph', 'Sal', 'Sam', 'Scotty',
        'Sid', 'Ted', 'Terrance', 'Tim', 'Tod', 'Tom', 'Travis', 'Tyron', 'Vanessa',
        'Vera', 'Vic', 'Von', 'Walton', 'Wilford', 'Willis', 'Willy', 'Wilton',
        'Winston', 'Woodrow', 'Zed', 'Zoe'
]

project_list = ['Alien', 'Avatar', 'Batman', 'Brazil', 'Chinatown', 'Crash',
        'Dredd', 'Fargo', 'Goodfellas', 'Hamlet', 'Jaws', 'Leon', 'Lockout',
        'Lolita', 'Looper', 'Manhattan', 'Memento', 'Metropolis', 'Misery',
        'Network', 'Oldboy', 'Prometheus', 'Psycho', 'Rocky', 'Superman',
        'Thor', 'Titanic', 'Trainspotting', 'Tron', 'Twins', 'Vertigo',
        'Videodrom', 'Watchmen', 'Zombieland'
]

department_list = ['anim', 'comp', 'dev', 'fx', 'lighting', 'mm', 'model', 'roto']

task_list = ['anim', 'cleanup', 'cloth', 'cloud', 'comp', 'dust', 'fluid',
        'grade', 'hair', 'light', 'lookdev', 'particles', 'render', 'rgb',
        'rig', 'roto', 'sim', 'techanim', 'track', 'water'
]

assert len(artist_list) == len(set(artist_list))
assert len(project_list) == len(set(project_list))
assert len(department_list) == len(set(department_list))
assert len(task_list) == len(set(task_list))