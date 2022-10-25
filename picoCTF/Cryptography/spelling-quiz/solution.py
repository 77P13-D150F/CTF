#!/usr/bin/env python3


from zipfile import ZipFile


with ZipFile('public.zip', 'r') as zip:
  zip.extractall()

with open('public/study-guide.txt', 'r') as file:
  words = file.read().split('\n')

# The idea is to use few encrypted words from the file study-guide.txt,
# for which we can guess the plaintext, to extract the encryption key.
# I searched for long words, for which there are less possible plainttext.
# Here I group first all the words by their lengths in a dictionary.

ordered_words = dict()
for word in words:
  if len(word) in ordered_words.keys():
    values = ordered_words[len(word)]
    values.append(word)
    ordered_words[len(word)] = values
  elif len(word) > 0:
    ordered_words[len(word)] = [word]

for key in ordered_words.keys():
  if len(ordered_words[key]) < 2:
    print('These words are {0} letter long: {1}\n'.format(key, ordered_words[key]))


# There is only one word in the list with 31 letters.
# In the English vocabulary here are only few words that are 31 letter long, we can test them all.

c = ordered_words[31][0]
possible_decryptions = """acetylgalactosaminyltransferase
acylglycerophosphoethanolamines
benzyldimethylhexadecylammonium
dichlorodiphenyltrichloroethane
dipalmitoylphosphatidylcholines
esophagogastroduodenoscopically
ethanolaminephosphotransferases
ethylbutylacetylaminopropionate
methylenedioxybenzylpiperazines
sulphoquinovosyldiacylglycerols
tetramethylenedisulphotetramine
trifluoromethylphenylpiperazine""".split('\n')

with open('public/flag.txt', 'r') as file:
  enc_flag = file.read().strip()

for m in possible_decryptions:
  dictionary = dict(zip(list(c), list(m)))
  possible_flag = ''.join([dictionary[i] if i in dictionary.keys() else i for i in enc_flag])
  print('{0} <-- {1}'.format(possible_flag, m))

# When translating into dichlorodiphenyltrichloroethane, we can read partial english
dictionary = dict(zip(list(c), list('dichlorodiphenyltrichloroethane')))

# Few letters are missing, we can deduct them manually:
dictionary['a'] = 's'
dictionary['d'] = 'g'
dictionary['p'] = 'v'
dictionary['h'] = 'j'
dictionary['o'] = 'u'
dictionary['s'] = 'm'
dictionary['e'] = 'w'

flag = ''.join([dictionary[i] if i in dictionary.keys() else i for i in enc_flag])
#print(enc_flag)
#print(flag)

print(''.join(['\npicoCTF{', flag, '}']))
