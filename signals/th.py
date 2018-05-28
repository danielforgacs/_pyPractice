"""
threading example module.

it needs a file called: "watchdir/watchfile.txt".
run this in a terminal then start modifying the file
and check for the thread to react when it's saved.
"""


import threading
import time

class Watcher(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('\t--INIT--')
        self.is_active = True

        with open('watchdir/watchfile.txt', 'r') as targetfile:
            self.target0 = targetfile.read()


    def run(self):
        print('\t--RUN--')
        k = 0
        loopmax = 50

        while k < loopmax and self.is_active:
            print('\t-- THREAD LOOP:', loopmax-k, '--')
            k += 1

            with open('watchdir/watchfile.txt', 'r') as targetfile:
                self.target = targetfile.read()

            if self.target != self.target0:
                print('.CHANGED.')
                self.target0 = self.target

            time.sleep(1)


    def deactivate(self):
        self.is_active = False


class SafeWatcher(Watcher):
    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.deactivate()



def main():
    w = Watcher()
    w.start()

    # with SafeWatcher() as w:
    #     w.start()

    for k in range(30):
        print('\trunning...:', k)
        time.sleep(0.8)

    w.deactivate()



if __name__ == '__main__':
    main()
