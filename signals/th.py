"""
threading example module.

it needs a file called: "watchdir/watchfile.txt".
run this in a terminal then start modifying the file
and check for the thread to react when it's saved.
"""


import threading
import time

class Watcher(threading.Thread):
    def __init__(self, sleep, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('\t--INIT--')
        self.is_active = True
        self.sleep = sleep

        with open('watchdir/watchfile.txt', 'r') as targetfile:
            self.target0 = targetfile.read()


    def run(self):
        print('\t--RUN--')
        k = 0
        # loopmax = 50

        # while k < loopmax and self.is_active:
        while self.is_active:
            print('\t\t-- thread loop --')
            k += 1

            with open('watchdir/watchfile.txt', 'r') as targetfile:
                self.target = targetfile.read()

            if self.target != self.target0:
                print('.CHANGED.')
                self.target0 = self.target

            time.sleep(self.sleep)


    def deactivate(self):
        self.is_active = False


# class SafeWatcher(Watcher):
#     def __enter__(self):
#         return self

#     def __exit__(self, *args, **kwargs):
#         self.deactivate()



def main():
    MAX_MAIN_LOOP = 30
    MAIN_SLEEP = 1
    THREAD_SLEEP = 1

    w = Watcher(sleep=THREAD_SLEEP)
    w.start()

    # with SafeWatcher() as w:
    #     w.start()

    for k in range(MAX_MAIN_LOOP):
        print('\trunning...:', k)
        time.sleep(MAIN_SLEEP)

    w.deactivate()



if __name__ == '__main__':
    main()
