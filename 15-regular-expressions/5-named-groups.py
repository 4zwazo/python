# python package for regular expression
import re

# cc email list
cc_list = '''Ezra Koenig <ekoenig@vpwk.com>,
              Rostam Batmanglij <rostam@vpwk.com>,
              Chris Tomson <ctomson@vpwk.com,
              Bobbi Baio <bbaio@vpwk.com
              Eliza Juste <ejuste@vpwk.com
              Done Lakay <dlakay@vpwk.com'''

# assign name to the group using ?P<name>

the_email = re.search(r'(?P<username>\w+)\@(?P<domain_name>\w+)\.(?P<company>\w+)', cc_list)

print(the_email)
print(the_email.group('username'))
print(the_email.group('domain_name'))
print(the_email.group('company'))
