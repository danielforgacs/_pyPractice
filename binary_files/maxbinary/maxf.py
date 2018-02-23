import re

for ch in 'layer_a':
    hexch = hex(ord(ch))
    print(hexch, type(hexch))

layer_a = bytes('layer_a'.encode('utf8'))
print(layer_a)
for ch in layer_a:
    print(ch, type(ch), hex(ch))

layhex = 'layer_a'.encode('utf8').hex()
print(layhex, type(layhex))


with open('maxscene_4_layer.max', 'rb') as fil:
    # res = fil.read(1)
    res = fil.read()

print(type(res))

print('\n')

print(res.find(layer_a))
print(re.findall(layer_a, res))
print(re.match(layer_a, res))
print(re.fullmatch(layer_a, res))
print(re.search(layer_a, res))

print(type(re.search(layer_a, res)))
print(dir(re.search(layer_a, res)))

# for match in re.search(layer_a, res):
#     print(match)

# print(b'', type(b''), b''.__sizeof__())
# print(res, type(res), res.__sizeof__())
# print(int.from_bytes(res, 'big'))
# print(ord(res))
# print(chr(ord(res)))

# # print(dir(res))
# # print(res.hex())


# hres = res.hex()

# print(type(hres))
# print(dir(hres))
# # print(res.hex())
