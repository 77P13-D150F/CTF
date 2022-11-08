#!/usr/bin/env python3

# Open the audio file with audacity. By zooming and changing the view to spectrum, the morse code elements become well visible.
# The challenge says that all the translated letters are lower case, and the pauses are replaced by underscores '_'.

code = """
. _ _
. . . .
. . . . _
_ _ . . .

. . . .
. . . . _
_ _ . . .
. . . .

_ _ _ _ .
_ _ _ _ _
_ . .

. _ _
. . _ _ _
_ _ _ _ _
. . _
_ _ _ _ .
. . . .
_ _ . . .
""".split('\n')

# Creating a dictionary of morse code mapped into ascii
morse_dict = dict()
morse_dict['. _'] = 'a'
morse_dict['_ . . .'] = 'b'
morse_dict['_ . _ .'] = 'c'
morse_dict['_ . .'] = 'd'
morse_dict['.'] = 'e'
morse_dict['. . _ .'] = 'f'
morse_dict['_ _ .'] = 'g'
morse_dict['. . . .'] = 'h'
morse_dict['. .'] = 'i'
morse_dict['. _ _ _'] = 'j'
morse_dict['_ . _'] = 'k'
morse_dict['. _ . .'] = 'l'
morse_dict['_ _'] = 'm'
morse_dict['_ .'] = 'n'
morse_dict['_ _ _'] = 'o'
morse_dict['. _ _ .'] = 'p'
morse_dict['_ _ . _'] = 'q'
morse_dict['. _ .'] = 'r'
morse_dict['. . .'] = 's'
morse_dict['_'] = 't'
morse_dict['. . _'] = 'u'
morse_dict['. . . _'] = 'v'
morse_dict['. _ _'] = 'w'
morse_dict['_ . . _'] = 'x'
morse_dict['_ . _ _'] = 'y'
morse_dict['_ _ . .'] = 'z'
morse_dict['. _ _ _ _'] = '1'
morse_dict['. . _ _ _'] = '2'
morse_dict['. . . _ _'] = '3'
morse_dict['. . . . _'] = '4'
morse_dict['. . . . .'] = '5'
morse_dict['_ . . . .'] = '6'
morse_dict['_ _ . . .'] = '7'
morse_dict['_ _ _ . .'] = '8'
morse_dict['_ _ _ _ .'] = '9'
morse_dict['_ _ _ _ _'] = '0'
morse_dict['. _ . _ . _'] = '.'
morse_dict['_ _ . . _ _'] = ','
morse_dict['. . _ _ . .'] = '?'
morse_dict['_ . . _ .'] = '/'
morse_dict[''] = '_'


# Translate and display
morse = ''.join([morse_dict[i] for i in code[1:-1]])
print(''.join(['picoCTF{', morse, '}']))
