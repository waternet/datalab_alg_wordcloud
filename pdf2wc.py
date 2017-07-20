import glob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import subprocess
import nltk
nltk.data.path.append("/home/waternet/programmeren/python/nltk_data")
from nltk.corpus import stopwords

stop_word_list = stopwords.words('dutch')
stop_word_set = set(stop_word_list)

pdffiles = glob.glob("data/*.pdf")

for pdffile in pdffiles:
    print "Converting %s to textfile" % pdffile
    command = "pdftotext '%s'" % pdffile
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()

txtfiles = glob.glob("data/*.txt")

ftxt = ""
for fillename in txtfiles:
    text = open(txtfiles[0]).read()
    for word in text.split():
        word = word.strip()
        if word.lower() not in stop_word_set:
            ftxt = ftxt + " " + word

wordcloud = WordCloud(max_font_size=40).generate(ftxt)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
