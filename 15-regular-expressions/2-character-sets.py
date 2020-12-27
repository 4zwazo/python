# python package for regular expression
import re

# cc email list
cc_list = '''Ezra Koenig <ekoenig@vpwk.com>,
              Rostam Batmanglij <rostam@vpwk.com>,
              Chris Tomson <ctomson@vpwk.com,
              Bobbi Baio <bbaio@vpwk.com
              Eliza Juste <ejuste@vpwk.com
              Done Lakay <dlakay@vpwk.com'''

# The + after an item in a regular expression matches one or more of that item. Meaning as in pa+ in pascal, the + will be scal

# search for Bobbi, Bobby, Robbi, or Robby
the_name = re.search(r'[R,B]obb[i,y]', cc_list)
print(the_name)

# Search for Chris
the_name = re.search(r'Chr[a-z][a-z] Tom[a-z]+', cc_list)
print(the_name)

# Search for the name that starts with D
the_name = re.search(r'D[A-Za-z]+', cc_list)
print(the_name)

# Search for the name that starts with any letters but has 10 characters
the_name = re.search(r'[A-Za-z]{10}', cc_list)
print(the_name)

# search for an email address naively
the_email = re.search(r'[A-Za-z]+@[a-z]+\.[a-z]+', cc_list)
print(the_email)

