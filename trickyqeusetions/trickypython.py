import sys

score = 0

try:
    # Add one line to make this work.
    def init(arg, k):
        print k*2
    class K(object):
        pass
    K(2)
except Exception as error:
    print 'line: %s - error: %s' % (sys.exc_info()[2].tb_lineno, error)
    print '\n--> Failed. score:', score
else:
    score += 1
    print '\n--> Passed. score:', score





























































try:
    # Add a line to make it work without writing "class"
    KK()
except Exception as error:
    print 'line: %s - error: %s' % (sys.exc_info()[2].tb_lineno, error)
    print '\n--> Failed. score:', score
else:
    score += 1
    print '\n--> Passed. score:', score

























































try:
    # Add a line to make it work.
    class C(object):
        pass
    KC()
except Exception as error:
    print 'line: %s - error: %s' % (sys.exc_info()[2].tb_lineno, error)
    print '\n--> Failed. score:', score
else:
    score += 1
    print '\n--> Passed. score:', score














































try:
    # Modify one line to make it work.
    Element = type('Element', (object,), {})
    e = Element()
    print e.value
except Exception as error:
    print 'line: %s - error: %s' % (sys.exc_info()[2].tb_lineno, error)
    print '\n--> Failed. score:', score
else:
    score += 1
    print '\n--> Passed. score:', score































































try:
    # Modify a line to make this work.
    c = ['Alpha', 'Beta', 'Gamma']

    for k in c:
        type(k, (object,), {k: 1})

    print Alpha.Alpha
    print Beta.Beta
    print Gamma.Gamma
except Exception as error:
    print 'line: %s - error: %s' % (sys.exc_info()[2].tb_lineno, error)
    print '\n--> Failed. score:', score
else:
    score += 1
    print '\n--> Passed. score:', score
