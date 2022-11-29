import os
import datetime
os.path.getsize('text.txt')

os.path.getmtime('text.txt')
timestamp = os.path.getmtime('text.txt')

datetime.datetime.fromtimestamp(timestamp).date()

