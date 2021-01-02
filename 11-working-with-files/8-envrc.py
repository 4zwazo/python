text = '''export STAGE=PROD
export TABLE_ID=trodent-cat-89090
  '''

with open('.envrc', 'w') as opened_file:
  opened_file.write(text)
