try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = {
    'version': '0.01',
    'name': 'first-best-worst-fit',
    'description': 'The demo of three contiguous memory allocation algorithm: First fit, Best fit and Worst fit',
    'author': 'yuanhang zheng',
    'author_email': 'zhengyhn@gmail.com',
    'url': 'https://github.com/itlodge/first-best-worst-fit',
    'download_url': 'https://github.com/itlodge/first-best-worst-fit',
    'install_requires': ['nose'],
    'packages': ['first-best-worst-fit'],
    'scripts': []
}

setup(**config)
