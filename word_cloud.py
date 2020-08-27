""" import wordcloud """
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
from PIL import Image


# file contents from 'text.txt' into string
""" file_contents = open('text.txt', 'r').read() """
file_contents = 'text.txt'
# file name from user input
""" file_contents = input('Enter file name: ') """




text = ""
with open(file_contents, encoding='utf-8') as f:
    text = ''.join(f.readlines())

""" 
    Most common parameters accepted by WordCloud:
        font_path — font path to the font that’ll be used (OTF or TTF). Defaults to the DroidSansMono path on a Linux machine. If you’re on another OS or don’t have this font, you need to adjust this path.
        width — width of the canvas. The default value is 400.
        height — height of the canvas. The default value is 200.
        max_words — the maximum words allowed. The default is 200.
        background_color — background color for the word-cloud image. The default is black.
        mask — input an image to be used as a mask 
"""
custom_mask = np.array(Image.open("car.png"))
wc = WordCloud(max_font_size=40, background_color="white", mask=custom_mask, contour_width=5, contour_color='steelblue').generate(text)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()

""" def calculate_frequencies(file_contents):
''' to remove uninteresting words and puntuations '''

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", 
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", 
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", 
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", 
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    # LEARNER CODE START HERE     
    frequencies = {}
    
    # string to lower case
    file_contents = file_contents.lower()

    # remove punctuations from string
    for char in punctuations:
        file_contents = file_contents.replace(char, "")

    # remove uninteresting words from string
           
    for word in file_contents.split():
        if word not in uninteresting_words:
            if word in frequencies.keys():
                frequencies[word] += 1
            else:
                frequencies[word] = 1
    
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show() """