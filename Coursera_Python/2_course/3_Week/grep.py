import re
log = 'July 21 05:24:43 mycomputer bad_process[12345]: ERROR Performing package update'
regex = r'\[(\d+)\]'
result = re.search(regex, log)
print(result[1])

