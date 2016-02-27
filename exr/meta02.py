exr = 'd:/fsb_jtj_0190_plates_main_v001.1007.exr'

with open(exr, 'rb') as f:
	content = f.read()

print(type(content))
print(content.decode('utf-64'))
# print(bytes('lalal', 'utf-8'))