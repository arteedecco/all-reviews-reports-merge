from setuptools import setup

setup(
    name='yourscript',
    version='0.1',
    py_modules=['yourscript'],
    install_requires=[
        'Click', 'openpyxl',
    ],
    entry_points='''
        [console_scripts]
        merge=merge:cli
    ''',
)