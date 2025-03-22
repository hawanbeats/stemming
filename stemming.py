from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
text = input("Kelime(ler) girin: ")
words = text.split()

stemmed_words = [stemmer.stem(word) for word in words]
print("Stemmed Words:", stemmed_words)
