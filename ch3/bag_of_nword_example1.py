from sklearn.feature_extraction.text import CountVectorizer

#Convert a collection of text documents to a matrix of token counts

#This implementation produces a sparse representation of the counts using scipy.sparse.csr_matrix.

#If you do not provide an a-priori dictionary and you do not use an analyzer
#that does some kind of feature selection then the number of features will be
#equal to the vocabulary size found by analyzing the data.
count_vect = CountVectorizer(ngram_range=(1,3))

processed_docs = [
'Dog bites man',
'Man bites dog',
'Dog eats meat',
'Man eats food',
]

bow_rep = count_vect.fit_transform(processed_docs)

print("Our vocabulary: ", count_vect.vocabulary_)

temp = count_vect.transform(["dog and dog are friends"])

print("Bow representation for 'dog and dog are friends':", temp.toarray())
