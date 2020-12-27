# python package for regular expression
import re

# cc email list
cc_list = '''Ezra Koenig <ekoenig@vpwk.com>,
              Rostam Batmanglij <rostam@vpwk.com>,
              Chris Tomson <ctomson@vpwk.com,
              Bobbi Baio <bbaio@vpwk.com
              Eliza Juste <ejuste@vpwk.com
              Done Lakay <dlakay@vpwk.com'''

all_emails = re.findall(r'\w+\@\w+\.\w+', cc_list)
print(all_emails)

all_emails = re.findall(r'(\w+)\@(\w+)\.(\w+)', cc_list)
print(all_emails)