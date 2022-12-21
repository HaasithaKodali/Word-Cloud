from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
dirname = path.dirname('C:/Users/DELL/AppData/Local/Programs/Python/Python36')
text = open(path.join(dirname, 'sample.txt')).read()
def calculate(text):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    remove_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "we", "our", "ours", "you", "your", "yours", "he", "she", "him",
                       "his", "her", "hers", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "have", "has", "had",
                       "do", "does", "did", "but", "at", "by", "with", "from", "here", "all", "any", "both", "each", "few", "more", "some", "such", "no",
                       "nor", "too", "very","in","its"]
    result ={}
    a=text.split()
    for w in a:
        if w.lower() in remove_words:
            pass
        else:
            for l in w:
                if l in punctuations:
                    l.replace(punctuations,"")
            if w not in result.keys():
                result[w]=0
            else:
                result[w]+=1
    wc = WordCloud().generate_from_frequencies(result)
    return wc.to_array()
myimage = calculate(text)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
