# -*- coding: utf-8 -*-
import time
import threading
from evaluation.oracle import TraceabilityOracle
from features_extraction.extractor import FeatureExtractor
from information_retrieval_methods.algebraic.classic_vector import *
from information_retrieval_methods.algebraic.latent_semantic_indexing import *
from information_retrieval_methods.algebraic.neural_networks import *
from information_retrieval_methods.pre_processor import SPLProjectPreProcessor
from information_retrieval_methods.probabilistic.bm25 import *
from information_retrieval_methods.set_theoretic.extended_boolean import *

"""SPLTrac: SPL Traceability Experimental Suite

Author: Tassio Vale
Website: www.tassiovale.com
Contact: tassio.vale@ufrb.edu.br
"""


class ProjectAnalysisThread(threading.Thread):

    def __init__(self, project, language, variability_impl_technology, loc, evaluation_results):
        threading.Thread.__init__(self)
        self.project = project
        self.language = language
        self.variability_impl_technology = variability_impl_technology
        self.loc = loc
        self.evaluation_results = evaluation_results

    def run(self):

        # EXECUTION OF THE INFORMATION RETRIEVAL ALGORITHMS
        print('\nProject: ' + self.project)
        print('Language: ' + self.language.upper())
        print('Variability realization technology: ' + self.variability_impl_technology.upper())

        print('Step 1: extracting features...')
        feature_extractor = FeatureExtractor(self.project, self.variability_impl_technology)
        feature_extractor.analyze_project()
        features_dictionary = feature_extractor.get_features_dictionary()

        print('Step 2: processing project...')
        # Preprocessor and CIDE projects are the ones which implement ifdef conditional compilation directives
        remove_ifdefs = False
        if self.variability_impl_technology == 'preprocessor' or self.variability_impl_technology == 'cide':
           remove_ifdefs = True
        pre_processor = SPLProjectPreProcessor(self.project, self.language, features_dictionary, remove_ifdefs)

        # Algebraic - classic vector model
        print('Step 3.1: running classic vector model algorithm...')
        classic_vector_performance = time.time()
        classic_vector_traces = classic_vector_run(features_dictionary, pre_processor)
        classic_vector_performance = time.time() - classic_vector_performance

        # Algebraic - neural networks model
        print('Step 3.2: running neural networks algorithm...')
        neural_network_performance = time.time()
        neural_network_traces = neural_network_run(features_dictionary, pre_processor)
        neural_network_performance = time.time() - neural_network_performance

        # Set theoretic - extended boolean model
        print('Step 3.3: running extended boolean model algorithm...')
        extended_boolean_performance = time.time()
        extended_boolean_traces = extended_boolean_run(features_dictionary, pre_processor)
        extended_boolean_performance = time.time() - extended_boolean_performance

        # Probabilistic - BM25 model
        print('Step 3.4: running BM25 algorithm...')
        bm25_performance = time.time()
        bm25_traces = bm25_run(features_dictionary, pre_processor)
        bm25_performance = time.time() - bm25_performance

        # Algebraic - classic vector model
        # print('Step 3.5: running latent semantic index algorithm...')
        # lsi_performance = time.time()
        # lsi_traces = latent_semantic_indexing_run(features_dictionary, pre_processor)
        # lsi_performance = time.time() - lsi_performance

        # print('classic_vector ' + str(classic_vector_traces))
        # print('neural_network ' + str(neural_network_traces))
        # print('extended_boolean ' + str(extended_boolean_traces))
        # print('bm25 ' + str(bm25_traces))

        print('Step 4: collecting results...')
        project_oracle = TraceabilityOracle(self.project)
        true_traces = project_oracle.extract_true_traces()
        self.evaluation_results.add_project_input_data(
            self.project, self.variability_impl_technology, self.language, self.loc, true_traces
        )

        self.evaluation_results.add_method_results(
            self.project, 'Classic vector model', classic_vector_traces, classic_vector_performance
        )
        self.evaluation_results.add_method_results(
            self.project, 'Neural networks', neural_network_traces, neural_network_performance
        )
        self.evaluation_results.add_method_results(
            self.project, 'Extended boolean', extended_boolean_traces, extended_boolean_performance
        )
        self.evaluation_results.add_method_results(
            self.project, 'BM25', bm25_traces, bm25_performance
        )
        # evaluation_results.add_method_results(project, 'Latent semantic indexing', lsi_traces, lsi_performance)
        # self.evaluation_results.add_method_results(
        #     self.project, 'Latent semantic indexing', lsi_traces, lsi_performance
        # )
