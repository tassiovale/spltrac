from evaluation.oracle import TraceabilityOracle
from features_extraction.extractor import FeatureExtractor
from information_retrieval_methods.algebraic.classic_vector import *
from information_retrieval_methods.algebraic.neural_networks import *
from information_retrieval_methods.pre_processor import SPLProjectPreProcessor
from information_retrieval_methods.probabilistic.bm25 import *
from information_retrieval_methods.set_theoretic.extended_boolean import *
from information_retrieval_methods.tfidf import *
from evaluation.evaluator import EvaluationResults

# START READING THE PROJECTS METADATA
config_file_name='../files/spl_projects.dat'

config_file = open(config_file_name, 'r')
projects_base_path = config_file.readline()

evaluation_results = EvaluationResults()

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
    inverted_index = calculate_tfidf_weights(pre_processor)  # calculating weight through TF-IDF for each feature

    print('Step 2: extracting features...')
    feature_extractor = FeatureExtractor(project, method)
    feature_extractor.analyze_project()
    features_dictionary = feature_extractor.get_features_dictionary()

    # Algebraic - classic vector model
    print('Step 3.1: running classic vector model algorithm...')
    classic_vector_traces = classic_vector_run(features_dictionary, pre_processor)

    # Algebraic - neural networks model
    print('Step 3.2: running neural networks algorithm...')
    neural_network_traces = neural_network_run(features_dictionary, pre_processor)

    # Set theoretic - extended boolean model
    print('Step 3.3: running extended boolean model algorithm...')
    extended_boolean_traces = extended_boolean_run(features_dictionary, pre_processor)

    # Probabilistic - BM25 model
    print('Step 3.4: running BM25 algorithm...')
    bm25_traces = bm25_run(features_dictionary, pre_processor)

    # print('classic_vector ' + str(classic_vector_traces))
    # print('neural_network ' + str(neural_network_traces))
    # print('extended_boolean ' + str(extended_boolean_traces))
    # print('bm25 ' + str(bm25_traces))

    print('Step 4: collecting results...')
    project_oracle = TraceabilityOracle(project)
    true_traces = project_oracle.extract_true_traces()
    evaluation_results.add_project_input_data(project, true_traces)

    evaluation_results.add_method_results(project, 'Classic vector model', classic_vector_traces)
    evaluation_results.add_method_results(project, 'Neural networks', neural_network_traces)
    evaluation_results.add_method_results(project, 'Extended boolean', extended_boolean_traces)
    evaluation_results.add_method_results(project, 'BM25', bm25_traces)

# consolidating results
print('Step 5: consolidating project results...')
evaluation_results.consolidate_results()

print('Step 6: generating output charts...')
evaluation_results.export_results()

config_file.close()

print('DONE\n\n')
