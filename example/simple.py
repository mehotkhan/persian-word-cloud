# #!/usr/bin/env python
# """
# Minimal Example
# ===============
#
# Generating a square wordcloud from the US constitution using default arguments.
# """
# # from os import path
# # from persian_wordcloud.persian_wordcloud import STOPWORDS, PersianWordCloud
# from persian_wordcloud import
#
#
# d = path.dirname(__file__)
#
# text = open(path.join(d, 'persian.txt'), encoding='utf-8').read()
#
# # Generate a word cloud image
#
# stopwords = set(STOPWORDS)
# # print(stopwords)
# # exit()
# wordcloud = PersianWordCloud(
#     max_words=100,
#     stopwords=stopwords,
#     # mask=mask,
#     margin=0,
#     width=800,
#     height=800,
#     min_font_size=1,
#     max_font_size=500,
#     background_color="white"
#     # random_state=1
# ).generate(text)
#
# image = wordcloud.to_image()
# image.show()
