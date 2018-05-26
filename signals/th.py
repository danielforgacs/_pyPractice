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

        with open('watchdir/watchfile.txt', 'r') as targetfile:
            self.target0 = targetfile.read()


    def run(self):
        k = 0

        while k < 150:
            k += 1

            with open('watchdir/watchfile.txt', 'r') as targetfile:
                self.target = targetfile.read()

            if self.target != self.target0:
                print('.CHANGED.')
                self.target0 = self.target

            time.sleep(0.3)


def main():
    w = Watcher()
    w.start()

    for k in range(10):
        print('running...:', k)
        time.sleep(0.8)



if __name__ == '__main__':
    main()
