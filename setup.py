from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='hebrewtools',
    version='0.0.1',
    description='Useful tools for working with vocalized Hebrew text in Python',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Aren Wilson-Wright',
    author_email='wilsonwright.a@gmail.com',
    keywords=['Biblical Hebrew', 'vocalization', 'normalization],
    url='https://github.com/gngpostalsrvc/hebrewtools',
    download_url='https://pypi.org/project/hebrewtools/'
)

install_requires = []

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
