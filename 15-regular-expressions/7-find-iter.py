# python package for regular expression
import re

# cc email list
cc_list = '''Ezra Koenig <ekoenig@vpwk.com>,
              Rostam Batmanglij <rostam@vpwk.com>,
              Chris Tomson <ctomson@vpwk.com,
              Bobbi Baio <bbaio@vpwk.com
              Eliza Juste <ejuste@vpwk.com
              Done Lakay <dlakay@vpwk.com'''

all_emails = re.finditer(r'(\w+)\@(\w+)\.(\w+)', cc_list)
print(all_emails)

print(next(all_emails))
print(next(all_emails))
print(next(all_emails))
print(next(all_emails))
print(next(all_emails))
print(next(all_emails))

print('')

all_emails = re.finditer(r'(\w+)\@(\w+)\.(\w+)', cc_list)

for email in all_emails:
  print(email.group(1))

print('')

all_emails = re.finditer(r'(?P<username>\w+)\@(?P<company>\w+)\.(?P<top_level>\w+)', cc_list)

for email in all_emails:
  print(email.groupdict())