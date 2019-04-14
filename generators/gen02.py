import time
from datetime import datetime

def tim():
    starttime = datetime.now()
    total = starttime

    while True:
        yield
        print(':: elapsed: %s' % (datetime.now()-starttime))
        print(':: total: %s' % (datetime.now()-total))
        print()
        starttime = datetime.now()


def func():
        print('func')
        time.sleep(0.5)
        next(timer)



timer = tim()
next(timer)
next(timer)
next(timer)
time.sleep(1)
next(timer)
next(timer)
time.sleep(3)
next(timer)
next(timer)

for k in list('ABCDE'):
    next(timer)

func()
func()


for k in list('ABCDE'):
    next(timer)
    time.sleep(0.25)
    func()