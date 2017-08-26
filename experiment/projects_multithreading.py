# -*- coding: utf-8 -*-
import time
import threading
from evaluation.oracle import TraceabilityOracle
from features_extraction.extractor import FeatureExtractor
from information_retrieval_methods.pre_processor import SPLProjectPreProcessor
from information_retrieval_methods.algebraic.classic_vector import ClassicVectorThread
from information_retrieval_methods.algebraic.latent_semantic_indexing import LSIThread
from information_retrieval_methods.algebraic.neural_networks import NeuralNetworksThread
from information_retrieval_methods.probabilistic.bm25 import BM25Thread
from information_retrieval_methods.set_theoretic.extended_boolean import ExtendedBooleanThread

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

        print('Step 3: preparing data collection...')
        project_oracle = TraceabilityOracle(self.project)
        true_traces = project_oracle.extract_true_traces()
        self.evaluation_results.add_project_input_data(
            self.project,
            self.variability_impl_technology,
            self.language,
            self.loc,
            pre_processor.get_num_files(),
            true_traces
        )

        # Algebraic - classic vector model
        print('Step 4.1: running classic vector model algorithm...')
        classic_vector_thread = ClassicVectorThread(features_dictionary, pre_processor,
                                                    self.project, self.evaluation_results)
        classic_vector_thread.start()

        # Algebraic - neural networks model
        print('Step 4.2: running neural networks algorithm...')
        neural_network_thread = NeuralNetworksThread(features_dictionary, pre_processor,
                                                    self.project, self.evaluation_results)
        neural_network_thread.start()

        # Set theoretic - extended boolean model
        print('Step 4.3: running extended boolean model algorithm...')
        extended_boolean_thread = ExtendedBooleanThread(features_dictionary, pre_processor,
                                                    self.project, self.evaluation_results)
        extended_boolean_thread.start()

        # Probabilistic - BM25 model
        print('Step 4.4: running BM25 algorithm...')
        bm25_thread = BM25Thread(features_dictionary, pre_processor, self.project, self.evaluation_results)
        bm25_thread.start()

        # Algebraic - classic vector model
        # print('Step 4.4: running latent semantic index algorithm...')
        # lsi_thread = LSIThread(features_dictionary, pre_processor, self.project, self.evaluation_results)
        # lsi_thread.start()

        classic_vector_thread.join()
        neural_network_thread.join()
        extended_boolean_thread.join()
        bm25_thread.join()
        # lsi_thread.join()

        # print('classic_vector ' + str(classic_vector_traces))
        # print('neural_network ' + str(neural_network_traces))
        # print('extended_boolean ' + str(extended_boolean_traces))
        # print('bm25 ' + str(bm25_traces))
