import numpy

def bm25_run(features_dictionary, pre_processor):
    """Executes the term weighting calculation.

       Body.
    """

    print('--------------------------------------------')
    print('                   BM25')
    print('--------------------------------------------')

    # reading k1 and b constant values
    bm25_constants_file = open('../files/bm25_constants.dat', "r")
    k1_const = int(bm25_constants_file.readline())
    b_const = float(bm25_constants_file.readline())
    bm25_constants_file.close()

    for feature_name in features_dictionary.keys():
        query_similarities = calculate_similarities(features_dictionary, pre_processor, feature_name, k1_const, b_const)
        print(print_similarity_results(pre_processor, feature_name, query_similarities))


def calculate_similarities(features_dictionary, pre_processor, feature_name, k1_const, b_const):

    features = features_dictionary[feature_name]
    weights = {}
    similarities = {}


    avg_document_length = get_avg_document_len(pre_processor)

    for document in pre_processor.get_documents().keys():
        similarity_value = 0.0
        for (term, index_by_term) in pre_processor.get_inverted_index().items():
            if term in features:
                if document in index_by_term:
                    document_term_frequency = index_by_term[document].frequency
                    bm25_num = (k1_const + 1) * document_term_frequency
                    bm25_den = k1_const * ((1 - b_const) + b_const * (pre_processor.get_document_length(document) / avg_document_length)) + document_term_frequency
                    bm25_value = bm25_num / bm25_den
                    similarity_value += bm25_value *  numpy.math.log((pre_processor.get_num_files()) / (pre_processor.get_docs_per_term(term)), 2)
        similarities[document] = similarity_value

    return similarities


def get_avg_document_len(pre_processor):
    acum = 0
    for (doc, length) in pre_processor.get_documents().items():
        acum += length
    if pre_processor.get_num_files() != 0:
        return acum / pre_processor.get_num_files()
    else:
        return 0


def print_similarity_results(pre_processor, feature_name, query_similarities):
    if feature_name not in pre_processor.get_stop_words():
        try:
            print('\n' + repr('FEATURE: ' + feature_name).ljust(10))
            print(repr('DOCUMENT').ljust(50), repr('IDF').ljust(10))
            for (document, similarity) in query_similarities.items():
                print(repr(document).ljust(50), repr(str(similarity)).ljust(10))
        except KeyError:
            print('WARNING: feature *' + feature_name + '* not traced')
    else:
        print('ERROR: *' + feature_name + '* is a stopword')
