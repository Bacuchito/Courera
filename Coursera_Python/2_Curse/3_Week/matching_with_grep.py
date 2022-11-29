import re
# put this in bash of ubuntu
'''grep thon /usr/share/dict/words'''
print(re.search(r'aza', 'plaza'))
# These words, all contain the string thon somewhere inside of them, which is why they appear in our results. 

'''grep -i python /usr/share/dict/words'''
# So we now know that any basic string is already a regular expression which will match a line that contains that string.

#########################################################
# Reserved characters

# a dot matches any character.
'''grep l.rts /usr/share/dict/words'''
print(re.search(r'p.ng', 'penguin'))
# With them, we can find portions of texts that match a given pattern even when the pattern isn't a whole word.

# The circumflex indicates the beginning
'''grep ^fruit /usr/share/dict/words'''
print(re.search(r'^e', 'enterprise'))

# the dollar sign indicates the end of the line.
'''grep cat$ /usr/share/dict/words'''
print(re.search(r'cat$', 'blackcat'))