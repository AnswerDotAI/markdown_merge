from setuptools import setup, find_packages
import os

owner,name = 'jph00','markdownmail'
exec(open(os.path.join(name, 'version.py')).read())
readme = open('README.md').read()

setup(description='Send templated emails in markdown',
      author='Jeremy Howard', author_email='info@fast.ai', license='Apache 2.0',
      url='http://github.com/'+owner+'/'+name,
      python_requires  = '>=3.6', install_requires = ['django', 'markdown'],
      long_description = readme, long_description_content_type = 'text/markdown',
      name=name, version=__version__, packages=find_packages(), zip_safe=False)

