import scipy
from information_retrieval_methods.tfidf import *
from information_retrieval_methods.pre_processor import DocumentDataByTerm

"""SPLTrac: SPL Traceability Experimental Suite

Author: Tassio Vale
Website: www.tassiovale.com
Contact: tassio.vale@ufrb.edu.br
"""


def latent_semantic_indexing_run(features_dictionary, pre_processor):
    """It runs the LSI algorithm and generating the resulting feature-to-code traces."""

    # print('--------------------------------------------')
    # print('       LATENT SEMANTIC INDEXING MODEL')
    # print('--------------------------------------------')
    traces = {}
    for feature_name in features_dictionary.keys():
        similarities = calculate_similarities(features_dictionary, pre_processor, feature_name)
        temp_traces = get_latent_semantic_indexing_traces(similarities, pre_processor, feature_name)
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

    # adding query as a document in the inverted index
    inverted_index = pre_processor.get_inverted_index().copy()  # copying the inverted index
    for feature in features:
        aux_index = {}
        document_data_by_term = DocumentDataByTerm()
        document_data_by_term.frequency = 1
        document_data_by_term.weight = 0
        aux_index['query_document'] = document_data_by_term
        try:
            inverted_index[feature].update(aux_index)
        except KeyError:
            inverted_index[feature] = aux_index

    calculate_tfidf_weights(pre_processor)  # calculating weight through TF-IDF for each feature

    documents = list(pre_processor.get_documents().keys())
    documents.append('query_document')
    terms = pre_processor.get_inverted_index().keys()
    M_matrix = scipy.zeros(shape=(len(terms), len(documents)))

    for (term_index, term) in enumerate(terms):
        list_term_document_weights = []
        for document in documents:
            matrix_cell_value = 0
            if term in inverted_index and document in inverted_index[term]:
                index_by_term = inverted_index[term]
                matrix_cell_value = index_by_term[document].weight
            list_term_document_weights.append(matrix_cell_value)
        M_matrix[term_index] = list_term_document_weights

    rows, cols = M_matrix.shape

    if cols >= 2:  # number of dimensions

        # Sigma comes out as a list rather than a matrix
        u, sigma, vt = scipy.linalg.svd(M_matrix)

        # Dimension reduction, build SIGMA'
        for index in range(cols - 2, cols):
            sigma[index] = 0

        # Reconstruct MATRIX'
        M_matrix_s = scipy.dot(scipy.dot(u, scipy.linalg.diagsvd(sigma, len(M_matrix), len(vt))), vt)

        document_relationship_matrix = scipy.dot(M_matrix_s.transpose(), M_matrix_s)

    # print(document_relationship_matrix.shape)
    # print(documents)

    documents_ranking = document_relationship_matrix[:,documents.index('query_document')]
    for (document_index, ranking) in enumerate(documents_ranking):
        # print(documents[document_index])
        similarities[documents[document_index]] = ranking

    del similarities['query_document']

    return similarities


def get_latent_semantic_indexing_traces(similarities, pre_processor, feature_name):
    """It generated the traced documents for each feature."""
    traces = {}
    threshold = pre_processor.get_method_threshold('latent_semantic_indexing')
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
