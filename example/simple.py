#!/usr/bin/env python
"""
Minimal Example
===============

Generating a square wordcloud from the US constitution using default arguments.
"""
from os import path
from persian_wordcloud.wordcloud import STOPWORDS, PersianWordCloud


d = path.dirname(__file__)

text = open(path.join(d, 'persian.txt'), encoding='utf-8').read()

# Add another stopword

STOPWORDS.add('اینکه')
stopwords = set(STOPWORDS)

# Generate a word cloud image

wordcloud = PersianWordCloud(
    max_words=100,
    stopwords=stopwords,
    margin=0,
    width=800,
    height=800,
    min_font_size=1,
    max_font_size=500,
    background_color="black"
).generate(text)

image = wordcloud.to_image()
image.show()
image.save('result.png')