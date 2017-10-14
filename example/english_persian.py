# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Minimal Example
===============

Generating a square wordcloud from the US constitution using default arguments.
"""
from os import path
from persian_wordcloud import PersianWordCloud, add_stop_words
from wordcloud import STOPWORDS as EN_STOPWORDS

d = path.dirname(__file__)

text_fa = open(path.join(d, 'persian.txt'), encoding='utf-8').read()
text_en = open(path.join(d, 'english.txt'), encoding='utf-8').read()

text = text_en + text_fa
# Add another stopword

stopwords = add_stop_words(['کاسپین'])
stopwords |= EN_STOPWORDS

# Generate a word cloud image

wordcloud = PersianWordCloud(
    only_persian=True,
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
image.save('en-fa-result.png')
