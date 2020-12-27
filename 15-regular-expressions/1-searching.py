# python package for regular expression
import re

# cc email list
cc_list = '''Ezra Koenig <ekoenig@vpwk.com>,
              Rostam Batmanglij <rostam@vpwk.com>,
              Chris Tomson <ctomson@vpwk.com,
              Bobbi Baio <bbaio@vpwk.com'''

# search for Rostam in the cc list
rostam = re.search(r'Rostam', cc_list)
print(rostam) #//=> <re.Match object; span=(46, 52), match='Rostam'>

if rostam:
  print('Found Rostam')

