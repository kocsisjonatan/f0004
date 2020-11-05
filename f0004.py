név = input('Mi a te neved?')
sz_é = input('hány éves vagy?')
sz_é = int(sz_é)
év = input('miéyen évet írunk')
év = int(év)
x = év - sz_é
y = x + 18
          
print(név, 'maga' , x, '- ban született és ennyi éves' , sz_é)

if sz_é >= 18:
    print(y, "-ban éretségiztél")