import math

def calculate_similarities(pre_processor):

    for (term, documents_dictionary) in pre_processor.get_inverted_index().items():
        term_document_ocurrences = pre_processor.get_term_document_frequency(term)

        for document_data in documents_dictionary.values():
            tfidf_weight = (1 + math.log(document_data.frequency, 2)) \
                                  * math.log((pre_processor.get_num_files() / term_document_ocurrences), 2)
            document_data.weight = tfidf_weight

def print_similarity_results(feature_name, pre_processor):
    if feature_name not in pre_processor.get_stop_words():
        try:
            print('\n' + repr('FEATURE: ' + feature_name).ljust(10))
            print(repr('DOCUMENT').ljust(50), repr('IDF').ljust(10))

            inverted_index = pre_processor.get_inverted_index()
            for (document, doc_term_dictionary) in inverted_index[feature_name].items():
                print(repr(document).ljust(50), repr(str(doc_term_dictionary.weight)).ljust(10))
        except KeyError:
            print('WARNING: feature not traced')
    else:
        print('ERROR: the feature_name is a stopword')