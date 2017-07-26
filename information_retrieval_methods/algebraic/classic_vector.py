# -*- coding: utf-8 -*-
import numpy

"""SPLTrac: SPL Traceability Experimental Suite

Author: Tassio Vale
Website: www.tassiovale.com
Contact: tassio.vale@ufrb.edu.br
"""


def classic_vector_run(features_dictionary, pre_processor):
    """It runs the classic vector algorithm and generating the resulting feature-to-code traces."""

    # print('--------------------------------------------')
    # print('            CLASSIC VECTOR MODEL')
    # print('--------------------------------------------')
    traces = {}
    for feature_name in features_dictionary.keys():
        similarities = calculate_similarities(features_dictionary, pre_processor, feature_name)
        temp_traces = get_classic_vector_traces(similarities, pre_processor, feature_name)
        if traces:
            traces.update(temp_traces)
        else:
            traces = temp_traces
        # print(print_similarity_results(pre_processor, feature_name, query_similarities))
    return traces


def calculate_similarities(features_dictionary, pre_processor, feature_name):
    """This variability_impl_technology calculates the similarity of every document for a given feature (and related synonyms)."""

    features = features_dictionary[feature_name]
    similarities = {}

    for document in pre_processor.get_documents().keys():
        sum_query_document_weights = 0.0
        # pre_vector_norm = 0.0
        sum_tf = 0.0
        sum_idf = 0.0

        for (term, index_by_term) in pre_processor.get_inverted_index().items():
            # if document in index_by_term:
                # pre_vector_norm += numpy.square(index_by_term[document].weight)
            if term in features and document in index_by_term:
                index_by_term = pre_processor.get_inverted_index()[term]
                term_document_ocurrences = pre_processor.get_docs_per_term(term)
                idf = numpy.math.log((pre_processor.get_num_files() / term_document_ocurrences), 2)
                sum_idf += numpy.square(idf)
                tf = 1 + numpy.math.log(index_by_term[document].frequency, 2)
                sum_tf += numpy.square(tf)
                sum_query_document_weights += tf * idf

        if sum_tf != 0 and sum_idf != 0:
            similarities[document] = sum_query_document_weights / (numpy.sqrt(sum_idf) * numpy.sqrt(sum_tf))
        else:
            similarities[document] = 0

    return similarities


def get_classic_vector_traces(similarities, pre_processor, feature_name):
    """It generated the traced documents for each feature."""
    traces = {}
    threshold = pre_processor.get_method_threshold('classic_vector')
    for (document, value) in similarities.items():
        if value > threshold:
            if feature_name in traces:
                traces[feature_name] += (document,)
            else:
                traces[feature_name] = (document,)
    return traces


def print_similarity_results(pre_processor, feature_name, query_similarities):
    """Method used for tests to check the similarity value of documents to the respective features."""
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
