# python package for regular expression
import re

# cc email list
cc_list = '''Ezra Koenig <ekoenig@vpwk.com>,
              Rostam Batmanglij <rostam@vpwk.com>,
              Chris Tomson <ctomson@vpwk.com,
              Bobbi Baio <bbaio@vpwk.com
              Eliza Juste <ejuste@vpwk.com
              Done Lakay <dlakay@vpwk.com'''

# () is used to define groups

the_email = re.search(r'(\w+)\@(\w+)\.(\w+)', cc_list)

print(the_email) # <re.Match object; span=(13, 29), match='ekoenig@vpwk.com'>
print(the_email.group(0)) # ekoenig@vpwk.com
print(the_email.group(1)) # ekoenig
print(the_email.group(2)) # vpwk
print(the_email.group(3)) # com



