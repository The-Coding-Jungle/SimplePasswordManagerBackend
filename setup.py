from distutils.core import setup
setup(
  name = 'SimplePasswordManagerBackend',
  packages = ['SimplePasswordManagerBackend'], # this must be the same as the name above
  version = '0.5',
  description = 'Simple Password Manager Backend Module',
  long_description="./README.md",
  long_description_content_type='text/markdown',
  author = 'HetDaftary',
  author_email = 'codingjungle1729@gmail.com',
  url = 'https://github.com/The-Coding-Jungle/SimplePasswordManagerBackend',
  keywords = ['add', 'sub', 'tests', 'password', 'password-manager'], 
  classifiers = [],
  dependencies = ['pyperclip', 'pybase64', 'pycryptodome', 'pysqlite3', 'clipboard'],
)
