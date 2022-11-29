import os
os.listdir('juegos')
dir = 'juegos'
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print('{} is a directory'.format(fullname))
    else:
        print('{} is not a directory'.format(fullname))

