from distutils.core import setup

setup(
  name = 'SimplePasswordManagerBackend',        
  packages = ['SimplePasswordManagerBackend'],  
  version = '1.5',      
  license='MIT',      
  description = 'Simple password manager backend',
  long_description=open('README.md').read(),
  author = 'Het Daftary',                  
  author_email = 'hetdaftary@gmail.com',    
  url = 'https://github.com/The-Coding-Jungle/SimplePasswordManagerBackend',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/The-Coding-Jungle/SimplePasswordManagerBackend/archive/refs/tags/1.5.tar.gz',    # I explain this later on
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