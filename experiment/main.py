from information_retrieval_methods.pre_processor import SPLProjectPreProcessor
from features_extraction.extractor import FeatureExtractor
from information_retrieval_methods.term_weigthing.tfidf import *
from information_retrieval_methods.algebraic.classic_vector import classic_vector_run
from information_retrieval_methods.set_theoretic.extended_boolean import extended_boolean_run
from information_retrieval_methods.probabilistic.bm25 import bm25_run


def get_projects_dictionary(config_file_name='../files/config_file.dat'):
    """Title.

       Body.
    """

    spl_projects = {}
    config_file = open(config_file_name, 'r')

    projects_base_path = config_file.readline()

    for line in config_file:
        (project, language) = line.split()
        path = projects_base_path.replace('\n', '')  # it removes the newline character ('\n') from the path
        spl_projects[path + project] = language

    config_file.close()
    return spl_projects.items()


# EXECUTION OF THE INFORMATION RETRIEVAL ALGORITHMS

for (project, language) in get_projects_dictionary():
    print('\n\nProject: ' + project)
    print('Language: ' + language.upper())

    pre_processor = SPLProjectPreProcessor(project, language)
    calculate_weights(pre_processor)  # calculating weight through TF-IDF for each feature

    feature_extractor = FeatureExtractor(project)
    features_dictionary = feature_extractor.get_features_dictionary()

    # Term weighting algorithm
    tfidf_run(features_dictionary, pre_processor)

    # Algebraic - classic vector model
    classic_vector_run(features_dictionary, pre_processor)

    # Algebraic - neural networks model

    # Set theoretic - extended boolean model
    extended_boolean_run(features_dictionary, pre_processor)

    # Probabilistic - BM25 model
    bm25_run(features_dictionary, pre_processor)
