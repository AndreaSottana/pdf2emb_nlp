from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='NLP tool for scraping text from a corpus of PDF files, embedding the sentences in the text and '
                'finding semantically similar sentences to a given search query.',
    author='AndreaSottana',
    license='MIT',
)
