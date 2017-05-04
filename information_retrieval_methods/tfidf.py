import numpy

"""SPLTrac: SPL Traceability Experimental Suite

Author: Tassio Vale
Website: www.tassiovale.com
Contact: tassio.vale@ufrb.edu.br
"""


def calculate_tfidf_weights(pre_processor):
    """Calculate the TF-IDF for all the features (and related synonyms).
    
    Foundations of the most popular term weighting scheme in IR tf-idf variability_impl_technology with log normalization 
    and inverse frequency. The tf-idf weighting scheme used is (1 + log fi,j) ∗ log N / ni
    """

    for (term, documents_dictionary) in pre_processor.get_inverted_index().items():
        term_document_ocurrences = pre_processor.get_docs_per_term(term)

        for document_data in documents_dictionary.values():
            tfidf_weight = (1 + numpy.math.log(document_data.frequency, 2)) \
                                  * numpy.math.log((pre_processor.get_num_files() / term_document_ocurrences), 2)
            document_data.weight = tfidf_weight

    return pre_processor.get_inverted_index()


def print_tfidf_results(features_dictionary, pre_processor):
    """Method used for tests to check the similarity value of documents to the respective features."""
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
