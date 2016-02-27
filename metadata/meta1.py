exr = 'd:/Azure/fsb_jtj_0190_plates_main/v001/2048x1080/fsb_jtj_0190_plates_main_v001.1007.exr'

with open(exr, 'r') as f:
    image = f.read()


print(image.decode())