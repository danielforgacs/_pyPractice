import os

root = os.path.dirname(__file__)

os.sys.path.insert(0, os.path.join(root, 'location_aaa'))
data = __import__('data')
aaa = data.datadict
os.sys.path.pop(0)

os.sys.path.insert(0, os.path.join(root, 'location_bbb'))
del os.sys.modules['data']
data = __import__('data')
bbb = data.datadict
os.sys.path.pop(0)

print aaa
print bbb