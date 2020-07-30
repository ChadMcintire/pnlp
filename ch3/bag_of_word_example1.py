from sklearn.feature_extraction.text import CountVectorizer

#Convert a collection of text documents to a matrix of token counts

#This implementation produces a sparse representation of the counts using scipy.sparse.csr_matrix.

#If you do not provide an a-priori dictionary and you do not use an analyzer
#that does some kind of feature selection then the number of features will be
#equal to the vocabulary size found by analyzing the data.
count_vect = CountVectorizer()

processed_docs = [
'Dog bites man',
'Man bites dog',
'Dog eats meat',
'Man eats food',
]

bow_rep = count_vect.fit_transform(processed_docs)

print("Our vocabulary: ", count_vect.vocabulary_)

print("BoW representation for 'dog bites man': ", bow_rep[0].toarray())

print("BoW representation for 'man bites dog': ", bow_rep[1].toarray())

temp = count_vect.transform(["dog and dog are friends"])

print("Bow representation for 'dog and dog are friends':", temp.toarray())

count_vect = CountVectorizer(binary=True)
bow_rep_bin = count_vect.fit_transform(processed_docs)
temp = count_vect.transform(["dog and dog are friends"])
print("Bow representation for 'dog and dog are friends':", temp.toarray())

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer()
bow_rep_tfidf = tfidf.fit_transform(processed_docs)

print("tfidf.idf  ", tfidf.idf_)
print("tfidf feature names", tfidf.get_feature_names())

temp = tfidf.transform(["dog and man are friends"])
print("Tfidf representation for 'dog and man are friends':\n", temp.toarray())

#Formula for Term Frequency
#TF(t,d)=(Number of occurrences of term t in document d)(Total number of terms in the document d)

#inverse document frequency
#IDF(t)=loge(Total number of documents in the corpus)(Number of documents with term t in them )
