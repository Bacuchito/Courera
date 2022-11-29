# Object Inheritance

In object-oriented programming, the concept of inheritance allows you to build relationships between objects, grouping together similar concepts and reducing code duplication. Let's create a custom Fruit class with color and flavor attributes:

``` 
class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

class Apple(Fruit):
    pass
class Grape(Fruit):
    pass

granny_smith = Apple("green", "tart")
carnelian = Grape("purple", "sweet")
print(granny_smith.flavor)
--- output tart ---
print(carnelian.color)
--- ouput purple ---
``` 
