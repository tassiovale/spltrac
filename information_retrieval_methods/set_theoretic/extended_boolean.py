import numpy


def extended_boolean_run(features_dictionary, pre_processor):
    """Executes the term weighting calculation.

       Body.
    """

    # print('--------------------------------------------')
    # print('             EXTENDED BOOLEAN')
    # print('--------------------------------------------')
    traces = {}
    for feature_name in features_dictionary.keys():
        similarities = calculate_similarities(features_dictionary, pre_processor, feature_name)
        temp_traces = get_extended_boolean_traces(similarities, pre_processor, feature_name)
        if traces:
            traces.update(temp_traces)
        else:
            traces = temp_traces
        # print(print_similarity_results(pre_processor, feature_name, query_similarities))
    return traces


def calculate_similarities(features_dictionary, pre_processor, feature_name):

    features = features_dictionary[feature_name]
    similarities = {}

    # reading p-norm value
    p_norm_file = open('../files/p_norm_value.dat', "r")
    p_norm = int(p_norm_file.readline())
    p_norm_file.close()

    for document in pre_processor.get_documents().keys():
        sum_query_document_weights = 0.0
        maximum_idf = get_maximum_idf(pre_processor)

        for (term, index_by_term) in pre_processor.get_inverted_index().items():
            if term in features and document in index_by_term:
                maximum_tf = get_maximum_tf(pre_processor, document, features)
                document_weight = (1 + numpy.math.log(index_by_term[document].frequency, 2)) / maximum_tf
                document_term_frequency = pre_processor.get_docs_per_term(term)
                query_weight = numpy.math.log((pre_processor.get_num_files() / document_term_frequency), 2) / maximum_idf
                sum_query_document_weights += numpy.power(document_weight, p_norm) * numpy.power(query_weight, p_norm)

        if len(features) != 0:
            similarities[document] = numpy.power(sum_query_document_weights / len(features), 1 / p_norm)
        else:
            similarities[document] = 0

    return similarities


def get_extended_boolean_traces(similarities, pre_processor, feature_name):
    traces = {}
    threshold = pre_processor.get_method_threshold('extended_boolean')
    for (document, value) in similarities.items():
        if value > threshold:
            if feature_name in traces:
                traces[feature_name] += (document,)
            else:
                traces[feature_name] = (document,)
    return traces


def get_maximum_tf(pre_processor, document, features):
    maximum_tf = 0.0
    for (term, index_by_term) in pre_processor.get_inverted_index().items():
        if term in features and document in index_by_term:
            tf = 1 + numpy.math.log(index_by_term[document].frequency, 2)
            if maximum_tf < tf:
                maximum_tf = tf
    return maximum_tf


def get_maximum_idf(pre_processor):
    maximum_idf = 0.0
    for (term, index_by_term) in pre_processor.get_inverted_index().items():
        number_of_documents_for_a_term = len(index_by_term.keys())
        idf = numpy.math.log((pre_processor.get_num_files() / number_of_documents_for_a_term), 2)
        if maximum_idf < idf:
            maximum_idf = idf
    return maximum_idf


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
