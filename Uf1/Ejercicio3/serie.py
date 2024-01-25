numero = 1
positiu = True
while numero !=0:
    numero = int(input('numero'))
    if numero <0:
        positiu = False
if positiu== False:
    print('no son tots positius')
else:
    print('tots son positius')