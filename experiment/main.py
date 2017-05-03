import time
from evaluation.oracle import TraceabilityOracle
from features_extraction.extractor import FeatureExtractor
from information_retrieval_methods.algebraic.classic_vector import *
from information_retrieval_methods.algebraic.latent_semantic_indexing import *
from information_retrieval_methods.algebraic.neural_networks import *
from information_retrieval_methods.pre_processor import SPLProjectPreProcessor
from information_retrieval_methods.probabilistic.bm25 import *
from information_retrieval_methods.set_theoretic.extended_boolean import *
from evaluation.evaluator import EvaluationResults

"""SPLTrac: SPL Traceability Experimental Suite

Author: Tassio Vale
Website: www.tassiovale.com
Contact: tassio.vale@ufrb.edu.br
"""

# START READING THE PROJECTS METADATA
config_file_name='../files/spl_projects.dat'

config_file = open(config_file_name, 'r')
projects_base_path = config_file.readline()

evaluation_results = EvaluationResults()

for line in config_file:
    (project, language, method, loc) = line.split()
    path = projects_base_path.replace('\n', '')  # it removes the newline character ('\n') from the path
    project = path + project

    # EXECUTION OF THE INFORMATION RETRIEVAL ALGORITHMS
    print('\nProject: ' + project)
    print('Language: ' + language.upper())
    print('Variability realization method: ' + method.upper())

    print('Step 1: extracting features...')
    feature_extractor = FeatureExtractor(project, method)
    feature_extractor.analyze_project()
    features_dictionary = feature_extractor.get_features_dictionary()

    print('Step 2: processing project...')
    pre_processor = SPLProjectPreProcessor(project, language, features_dictionary)

    # Algebraic - classic vector model
    print('Step 3.1: running classic vector model algorithm...')
    classic_vector_performance = time.time()
    classic_vector_traces = classic_vector_run(features_dictionary, pre_processor)
    classic_vector_performance = time.time() - classic_vector_performance

    # Algebraic - classic vector model
    print('Step 3.2: running latent semantic index algorithm...')
    lsi_performance = time.time()
    lsi_traces = latent_semantic_indexing_run(features_dictionary, pre_processor)
    lsi_performance = time.time() - lsi_performance

    # Algebraic - neural networks model
    print('Step 3.3: running neural networks algorithm...')
    neural_network_performance = time.time()
    neural_network_traces = neural_network_run(features_dictionary, pre_processor)
    neural_network_performance = time.time() - neural_network_performance

    # Set theoretic - extended boolean model
    print('Step 3.4: running extended boolean model algorithm...')
    extended_boolean_performance = time.time()
    extended_boolean_traces = extended_boolean_run(features_dictionary, pre_processor)
    extended_boolean_performance = time.time() - extended_boolean_performance

    # Probabilistic - BM25 model
    print('Step 3.5: running BM25 algorithm...')
    bm25_performance = time.time()
    bm25_traces = bm25_run(features_dictionary, pre_processor)
    bm25_performance = time.time() - bm25_performance

    # print('classic_vector ' + str(classic_vector_traces))
    # print('neural_network ' + str(neural_network_traces))
    # print('extended_boolean ' + str(extended_boolean_traces))
    # print('bm25 ' + str(bm25_traces))

    print('Step 4: collecting results...')
    project_oracle = TraceabilityOracle(project)
    true_traces = project_oracle.extract_true_traces()
    evaluation_results.add_project_input_data(project, language, loc, true_traces)

    evaluation_results.add_method_results(project, 'Classic vector model', classic_vector_traces, classic_vector_performance)
    evaluation_results.add_method_results(project, 'Latent semantic indexing', lsi_traces, lsi_performance)
    evaluation_results.add_method_results(project, 'Neural networks', neural_network_traces, neural_network_performance)
    evaluation_results.add_method_results(project, 'Extended boolean', extended_boolean_traces, extended_boolean_performance)
    evaluation_results.add_method_results(project, 'BM25', bm25_traces, bm25_performance)

# consolidating results
print('Step 5: consolidating project results...')
evaluation_results.export_results()

config_file.close()

print('DONE\n\n')
