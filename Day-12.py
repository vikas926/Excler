# -*- coding: utf-8 -*-
"""Day-12

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IrkUjGuncSe_svuBi_TZlkuR67kP170V
"""

##Write a Python script to generate a WordCloud from the text: 'data science machine learning artificial intelligence'. Save the WordCloud as an image.
from wordcloud import WordCloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(text, output_file):
    """
    Generates a WordCloud from the given text and saves it as an image.

    Args:
        text (str): The input text for the WordCloud.
        output_file (str): The file name for saving the WordCloud image.

    Returns:
        None
    """
    # Create a WordCloud object without specifying a font path (uses default font)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    # Display the WordCloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

    # Save the WordCloud image
    wordcloud.to_file(output_file)
    print(f"WordCloud saved as '{output_file}'")

# Input text
text = 'data science machine learning artificial intelligence'

# Generate and save the WordCloud
generate_wordcloud(text, 'wordcloud.png')

