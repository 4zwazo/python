# python package for regular expression
import re

# cc email list
cc_list = '''Ezra Koenig <ekoenig@vpwk.com>,
              Rostam Batmanglij <rostam@vpwk.com>,
              Chris Tomson <ctomson@vpwk.com,
              Bobbi Baio <bbaio@vpwk.com
              Eliza Juste <ejuste@vpwk.com
              Done Lakay <dlakay@vpwk.com'''

# \w is equivalent to [A-Za-z0-9_]
# \d is equivalent to [0-9]
# use + for to match multiple characters

the_name = re.search(r'\w+', cc_list)
print(the_name)

the_email = re.search(r'\w+\@\w+\.\w+', cc_list)
print(the_email)
