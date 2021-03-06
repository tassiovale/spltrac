# -*- coding: utf-8 -*-
import numpy
import threading
import time

"""SPLTrac: SPL Traceability Experimental Suite

Author: Tassio Vale
Website: www.tassiovale.com
Contact: tassio.vale@ufrb.edu.br
"""


class ExtendedBooleanThread(threading.Thread):

    def __init__(self, features_dictionary, pre_processor, project, evaluation_results):
        threading.Thread.__init__(self)
        self.features_dictionary = features_dictionary
        self.pre_processor = pre_processor
        self.project = project
        self.evaluation_results = evaluation_results

    def run(self):
        """It runs the extended boolean algorithm and generating the resulting feature-to-code traces."""
        performance = time.time()
        # print('--------------------------------------------')
        # print('             EXTENDED BOOLEAN')
        # print('--------------------------------------------')
        traces = {}
        for feature_name in self.features_dictionary.keys():
            similarities = self.calculate_similarities(feature_name)
            temp_traces = self.get_extended_boolean_traces(similarities, feature_name)
            if traces:
                traces.update(temp_traces)
            else:
                traces = temp_traces
            # print(print_similarity_results(pre_processor, feature_name, query_similarities))
        performance = time.time() - performance
        self.evaluation_results.add_method_results(
            self.project, 'Extended boolean',
            traces, performance
        )

    def calculate_similarities(self, feature_name):
        """This variability_impl_technology calculates the similarity of every document
        for a given feature (and related synonyms)."""

        features = self.features_dictionary[feature_name]
        similarities = {}

        # reading p-norm value
        p_norm_file = open('../files/p_norm_value.dat', "r")
        p_norm = int(p_norm_file.readline())
        p_norm_file.close()

        maximum_idf = self.get_maximum_idf()

        for document in self.pre_processor.get_documents().keys():
            sum_query_document_weights = 0.0
            maximum_frequency = self.get_maximum_frequency(document, features)

            for (term, index_by_term) in self.pre_processor.get_inverted_index().items():
                if term in features and document in index_by_term:
                    document_weight = index_by_term[document].frequency / maximum_frequency
                    document_term_frequency = self.pre_processor.get_docs_per_term(term)
                    query_weight = \
                        numpy.math.log((self.pre_processor.get_num_files() / document_term_frequency), 2) / maximum_idf
                    sum_query_document_weights += numpy.power(document_weight, p_norm) * \
                                                  numpy.power(query_weight, p_norm)

            numerator = sum_query_document_weights / len(features)
            if len(features) != 0 and p_norm != 0 and numerator > 0:
                similarities[document] = numpy.power(numerator, 1 / p_norm)
            else:
                similarities[document] = 0

        return similarities

    def get_maximum_frequency(self, document, features):
        """This variability_impl_technology identifies the maximum TF value for a given document."""
        maximum_frequency = 0.0
        for (term, index_by_term) in self.pre_processor.get_inverted_index().items():
            if term in features and document in index_by_term:
                frequency = index_by_term[document].frequency
                if maximum_frequency < frequency:
                    maximum_frequency = frequency
        return maximum_frequency

    def get_maximum_idf(self):
        """This variability_impl_technology identifies the maximum IDF value for the project."""
        maximum_idf = 0.0
        for (term, index_by_term) in self.pre_processor.get_inverted_index().items():
            number_of_documents_for_a_term = len(index_by_term.keys())
            idf = numpy.math.log((self.pre_processor.get_num_files() / number_of_documents_for_a_term), 2)
            if maximum_idf < idf:
                maximum_idf = idf
        return maximum_idf

    def get_extended_boolean_traces(self, similarities, feature_name):
        """It generated the traced documents for each feature."""
        traces = {}
        threshold = self.pre_processor.get_method_threshold('extended_boolean')
        for (document, value) in similarities.items():
            if value > threshold:
                if feature_name in traces:
                    traces[feature_name] += (document,)
                else:
                    traces[feature_name] = (document,)
        return traces

    def print_similarity_results(self, feature_name, query_similarities):
        """Method used for tests to check the similarity value of documents to the respective features."""
        if feature_name not in self.pre_processor.get_stop_words():
            try:
                print('\n' + repr('FEATURE: ' + feature_name).ljust(10))
                print(repr('DOCUMENT').ljust(50), repr('IDF').ljust(10))
                for (document, similarity) in query_similarities.items():
                    print(repr(document).ljust(50), repr(str(similarity)).ljust(10))
            except KeyError:
                print('WARNING: feature *' + feature_name + '* not traced')
        else:
            print('ERROR: *' + feature_name + '* is a stopword')
