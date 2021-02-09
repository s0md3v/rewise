import io
from setuptools import setup, find_packages
from os import path
this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    desc = f.read()

setup(
    name='rewise',
    version=__import__('rewise').__version__,
    description='Google auto-complete wrapper',
    long_description=desc,
    long_description_content_type='text/markdown',
    author='Somdev Sangwan',
    author_email='s0md3v@gmail.com',
    license='MIT License',
    url='https://github.com/s0md3v/rewise',
    download_url='https://github.com/s0md3v/rewise/archive/v%s.zip' % __import__(
        'rewise').__version__,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Text Processing',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
    keywords=['google', 'spell', 'spell-check', 'autocorrect', 'autocomplete']
)
