# python package for regular expression
import re

# cc email list
cc_list = '''Ezra Koenig <ekoenig@vpwk.com>,
              Rostam Batmanglij <rostam@vpwk.com>,
              Chris Tomson <ctomson@vpwk.com,
              Bobbi Baio <bbaio@vpwk.com
              Eliza Juste <ejuste@vpwk.com
              Done Lakay <dlakay@vpwk.com'''

regex = re.compile(r'\w+\@\w+\.\w+')
the_email = regex.search(cc_list)
print(the_email)

the_emails = regex.findall(cc_list)
print(the_emails)

the_emails = regex.finditer(cc_list)

for email in the_emails:
  print(email.group(0))