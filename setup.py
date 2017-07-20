"""
See:
https://github.com/Mehotkhan/persian-word-cloud
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

setup(
    name='persian_wordcloud',
    version='1.3.0',
    description='Persian Word Cloud Generator',
    long_description='Persian Word Cloud Generator',
    url='https://github.com/Mehotkhan/persian-word-cloud',
    author='Ali Zemani , Javad Bahoosh',
    author_email='mehot1@gmail.coom , j.bahoosh@mail.sbu.ac.ir',
    license='MIT',
    packages=['persian_wordcloud'],
    package_data={'persian_wordcloud': ['stopwords', 'fonts/Vazir-Light.ttf']},
    # What does your project relate to?
    keywords='persian  wordcloud',
    install_requires=['arabic_reshaper', 'python-bidi', 'wordcloud'],
)
