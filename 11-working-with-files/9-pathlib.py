import pathlib

path = pathlib.Path(
    '/Users/pascallaurent/Data/Dev/python/python-for-devops/11-working-with-files/example.txt')
path.write_text("Another cool day.")
path.read_text()


