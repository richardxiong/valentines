# valentines
A WordCloud generated from chat history as a Valentine's Day gift or Christmas gift for your GF/BF.

This python code works for 40 different languages. Below is the procedure that you can get the code to work:

![alt tag](http://github.com/richardxiong/valentines/sunrise.png)

1 Install dependencies

$ pip install numpy,pandas,jieba,wordcloud

2 Fetch the chat history between you and your significant other and export to .txt file

Here as an example, I use the scripts from the movie "Before Sunrise" and "Before Midnight", which could be regarded as the chat history between Celene and Jessie.

3 Build a word filter, and save to file "stopwords.txt"

To filter some irrelevant words, like dates, times, and the chatters' names.

4 Choose a shape of word cloud

Here as an example, I use the figure "heart2.png" in the code. You are more than welcome to choose and download any other fancy shapes you like

5 Run the code and play around on your own!!! (You probably need to tune the parameters a little bit)

$ python valentines.py

6 Save the figures

Here as an example, I save the generated two WordCloud figures "sunrise.png" and "midnight.png" to this directory, for your reference.
