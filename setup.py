from distutils.core import setup
setup(
  name = 'SimplePasswordManagerBackend',
  packages = ['SimplePasswordManagerBackend'], # this must be the same as the name above
  version = '0.3',
  description = 'Simple Password Manager Backend Module',
  author = 'HetDaftary',
  author_email = 'codingjungle1729@gmail.com',
  url = 'https://github.com/The-Coding-Jungle/SimplePasswordManagerBackend',
  download_url = 'https://github.com/The-Coding-Jungle/SimplePasswordManagerBackend/releases/tag/0.3',
  keywords = ['add', 'sub', 'tests', 'password', 'password-manager'], 
  classifiers = [],
  dependencies = ['pyperclip', 'pybase64', 'pycryptodome', 'pysqlite3', 'clipboard'],
)
