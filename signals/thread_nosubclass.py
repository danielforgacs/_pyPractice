"""
threading example module.

it needs a file called: "watchdir/watchfile.txt".
run this in a terminal then start modifying the file
and check for the thread to react when it's saved.
"""


import threading
import time



def runtime(sleep):
    print('\t--RUN--')
    k = 0

    with open('watchdir/watchfile.txt', 'r') as targetfile:
        target0 = targetfile.read()

    while True:
        print('\t\t-- thread loop --')
        k += 1

        with open('watchdir/watchfile.txt', 'r') as targetfile:
            target = targetfile.read()

        if target != target0:
            print('.CHANGED.')
            target0 = target

        time.sleep(sleep)



def main():
    MAX_MAIN_LOOP = 30
    MAIN_SLEEP = 1
    THREAD_SLEEP = 1

    w = threading.Thread(target=runtime, kwargs={'sleep': THREAD_SLEEP})
    w.start()

    for k in range(MAX_MAIN_LOOP):
        print('\trunning...:', k)
        time.sleep(MAIN_SLEEP)




if __name__ == '__main__':
    main()
