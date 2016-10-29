import sys
import inspect
import logging

log = logging.getLogger(name=__name__)
loghandle = logging.StreamHandler()
logformat = logging.Formatter('%(funcName)s : %(lineno)d --> %(message)s')

loghandle.setFormatter(logformat)
log.setLevel(logging.INFO)
# log.setLevel(logging.DEBUG)
log.addHandler(loghandle)

log.info('PySide test')

from PySide import QtGui
log.info('QtGui imported')


icon = 'd://dev//_pyPractice-env//mintty.png'


class Button(QtGui.QPushButton):
    def __init__(self):
        log.info('button init')
        log.debug('\n\n... Button widget init stack:\n {0}\n'.format(str(inspect.stack())))

        super(Button, self).__init__()
        log.info('button super init')

        # self.setText('fasza button')
        self.setIcon(QtGui.QPixmap(icon))

    def MouseMoveEvent(self):
        log.info('MouseMoveEvent')

    def MousePressEvent(self):
        log.info('MousePressEvent')



def main():
    log.info('main start')
    
    app = QtGui.QApplication([])
    log.info('app start')

    mainwidget = Button()
    mainwidget.show()
    log.info('main show')

    sys.exit(app.exec_())
    log.info('sys exit')


if __name__ == '__main__':
    log.info('module start')
    main()