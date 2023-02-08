from distutils.core import setup
import py2exe

setup(
    console=['main.py'],
    options={ 
        'py2exe': {
            'packages': ['pytimedinput'],
            'dist_dir': 'dist'
        }
    },
    py_modules = ['beep', 'constants', 'introduction', 'loading', 'mechanics', 'modules', 'shared']
    )