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
                print('changed')
                self.target0 = self.target

            time.sleep(0.3)


w = Watcher()
w.start()
