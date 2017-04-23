from information_retrieval_methods.pre_processor import SPLProjectPreProcessor
from features_extraction.extractor import FeatureExtractor
from information_retrieval_methods.term_weigthing.tfidf import *
from information_retrieval_methods.algebraic.classic_vector import classic_vector_run
from information_retrieval_methods.set_theoretic.extended_boolean import extended_boolean_run
from information_retrieval_methods.probabilistic.bm25 import bm25_run
from information_retrieval_methods.algebraic.neural_networks import neural_network_run
from evaluation.oracle import TraceabilityOracle

# START READING THE PROJECTS METADATA
config_file_name='../files/config_file.dat'

config_file = open(config_file_name, 'r')
projects_base_path = config_file.readline()

for line in config_file:
    (project, language, method) = line.split()
    path = projects_base_path.replace('\n', '')  # it removes the newline character ('\n') from the path
    project = path + project

    # EXECUTION OF THE INFORMATION RETRIEVAL ALGORITHMS
    print('Project: ' + project)
    print('Language: ' + language.upper())
    print('Variability realization method: ' + method.upper())

    print('Step 1: processing project...')
    pre_processor = SPLProjectPreProcessor(project, language)
    calculate_ifidf_weights(pre_processor)  # calculating weight through TF-IDF for each feature

    print('Step 2: extracting features...')
    feature_extractor = FeatureExtractor(project, method)
    feature_extractor.analyze_project()
    features_dictionary = feature_extractor.get_features_dictionary()

    # Term weighting algorithm
    print('Step 3.1: running TF-IDF algorithm...')
    tfidf_run(features_dictionary, pre_processor)

    # Algebraic - classic vector model
    print('Step 3.2: running classic vector model algorithm...')
    classic_vector_run(features_dictionary, pre_processor)

    # Algebraic - neural networks model
    print('Step 3.3: running neural networks algorithm...')
    neural_network_run(features_dictionary, pre_processor)

    # Set theoretic - extended boolean model
    print('Step 3.4: running extended boolean model algorithm...')
    extended_boolean_run(features_dictionary, pre_processor)

    # Probabilistic - BM25 model
    print('Step 3.5: running BM25 algorithm...')
    bm25_run(features_dictionary, pre_processor)

    project_oracle = TraceabilityOracle(project)
    project_oracle.extract_true_traces()

    print('DONE\n\n')

config_file.close()
