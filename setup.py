# setup/install file

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description'       :   'A discord bot',
    'author'            :   'Paul Rafferty',
    'url'               :   'URL to get it.',
    'download_url'      :   'Where to download it.',
    'author_email'      :   'paul_raffo@hotmail.com',
    'version'           :   '0.1',
    'install_requires'  :   ['discord'],
    'packages'          :   ['dustybot'],
    'scripts'           :   [],
    'name'              :   'DustyBot'
}

setup(**config)
