from distutils.core import setup
setup(
  name = 'SimplePasswordManagerBackend',         # How you named your package folder (MyLib)
  packages = ['SimplePasswordManagerBackend'],   # Chose the same as "name"
  version = '1.0.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Simple password manager backend',   # Give a short description about your library
  author = 'Het Daftary',                   # Type in your name
  author_email = 'hetdaftary@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/The-Coding-Jungle',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'clipboard',
          'pysqlite3',
          'pycryptodome',
          'typing',
          'pybase64'
      ],
  classifiers=[
    'Intended Audience :: Developers',      # Define that your audience are developers
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)