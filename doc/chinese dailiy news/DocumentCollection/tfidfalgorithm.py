from math import log10 as log


def tfidf(appear_time_in_document = 3,the_number_of_words_in_document = 56,the_number_of_document_in_collection = 17,appear_time_in_collection = 10):

  tf = appear_time_in_document/the_number_of_words_in_document
  idf = log(the_number_of_document_in_collection/appear_time_in_collection)
  value_tfidf = tf * idf 
  
  return value_tfidf
  
def idf(the_number_of_document_in_collection = 17,appear_time_in_collection = 10):

  value_idf = log(the_number_of_document_in_collection/appear_time_in_collection)
  return value_idf