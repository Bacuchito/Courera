import os
os.chdir(r'C:\Users\Bacuchito\Documents\Markdown\Python\Coursera\Curso_Python\1_Curse\6_Week')
import PIL.Image
image = PIL.Image.open('output_10_0.png')
print(image.size)
print(image.format)

import pandas
visitors = [1287, 1298, 8764, 9466, 1635]
errors = [ 32, 84, 36, 65, 12]

df = pandas.DataFrame({'visitors': visitors, 'errors': errors}, index = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
print(df)
df2 = df['errors'].mean()
print(df2)