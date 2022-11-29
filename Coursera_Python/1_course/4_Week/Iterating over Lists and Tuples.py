winners = ('Sergio', 'Sebastian', 'Anuel')
for index, person in enumerate(winners):
    print('{} - {}'.format(index + 1, person))

#############################################

animals = ('cat', 'dog', 'zebra', 'elephant', 'cow')
chars = 0
for animal in animals:
    chars += len(animal)

print('total character: {}, Average length: {}'.format(chars, chars/len(animals)))

#################################################
def full_email(people):
    result = []
    for email, name in people:
        result.append('{} <{}>'.format(name, email))
    return result
print(full_email([('DiegoM@gmail.com', 'Diego Maradona'), ('CristianoR@gmail.com', 'Cristiano Ronaldo'), ('LeoMessi@gmail.com', 'Leo Messi')]))
