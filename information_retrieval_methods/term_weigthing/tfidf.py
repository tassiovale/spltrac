import numpy

# Foundations of the most popular term weighting scheme in IR
# tf-idf method with log normalization and inverse frequency
# One of the recommended tf-idf weighting schemes
# (1 + log fi,j) ∗ log N / ni


def calculate_weights(pre_processor):
    """Calculate the TF-IDF for the specified term.

        This is computed by taking the logarithm of
        (number of documents in corpus) divided by (number of documents containing this term).
     """

    for (term, documents_dictionary) in pre_processor.get_inverted_index().items():
        term_document_ocurrences = pre_processor.get_term_document_frequency(term)

        for document_data in documents_dictionary.values():
            tfidf_weight = (1 + numpy.math.log(document_data.frequency, 2)) \
                                  * numpy.math.log((pre_processor.get_num_files() / term_document_ocurrences), 2)
            document_data.weight = tfidf_weight


def print_tfidf_results(features_dictionary, pre_processor):
    inverted_index = pre_processor.get_inverted_index()
    for feature_name in features_dictionary.keys():
        if feature_name not in pre_processor.get_stop_words():
            try:
                print('\n' + repr('FEATURE: ' + feature_name).ljust(10))
                print(repr('DOCUMENT').ljust(50), repr('IDF').ljust(10))

                for (document, doc_term_dictionary) in inverted_index[feature_name].items():
                    print(repr(document).ljust(50), repr(str(doc_term_dictionary.weight)).ljust(10))
            except KeyError:
                print('WARNING: feature *' + feature_name + '* not traced')
        else:
            print('ERROR: *' + feature_name + '* is a stopword')
