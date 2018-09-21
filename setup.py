
from distutils.core import setup

setup(
    name='mkdocs-fastsearch',
    version='0.1.0',
    author='Andy Oakley',
    author_email='ao@ao.vc',
    packages=['mkdocs_fastsearch'],
    license='LICENSE.txt',
    description='Mkdocs plugin for faster search. Based on stock search plugin.',
    install_requires=[
    ],

    entry_points={
        'mkdocs.plugins': [
            'fastsearch = mkdocs_fastsearch:SearchPlugin',
        ]
    }
)

