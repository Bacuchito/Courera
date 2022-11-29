#Fill in the blanks to print a line for each item of clothing with each color, for example: "red shirt", "blue shirt", and so on.
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for clothes, colors in wardrobe.items():
	for color in colors:
		print("{} {}".format(color, clothes))