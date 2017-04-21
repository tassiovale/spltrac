import numpy

class ExtendedBooleanModel:

    def __init__(self, features_dictionary, pre_processor):

        self.features_dictionary = features_dictionary
        self.pre_processor = pre_processor

    def calculate_similarities(self, feature_name):

        features = self.features_dictionary[feature_name]
        weights = {}
        similarities = {}

        #reading p-norm value
        p_norm_file = open('../files/p_norm_value.dat', "r")
        p_norm = int(p_norm_file.readline())
        p_norm_file.close()

        for document in self.pre_processor.get_documents():
            sum_query_document_weights = 0.0
            maximum_idf = self.get_maximum_idf()

            for (term, index_by_term) in self.pre_processor.get_inverted_index().items():
                if term in features:
                    if document in index_by_term:
                        maximum_tf = self.get_maximum_tf(document, features)
                        document_weight = (1 + numpy.math.log(index_by_term[document].frequency, 2)) / maximum_tf
                        document_term_frequency = self.pre_processor.get_term_document_frequency(term)
                        query_weight = numpy.math.log((self.pre_processor.get_num_files() / document_term_frequency), 2) / maximum_idf
                        sum_query_document_weights += numpy.power(document_weight, p_norm) * numpy.power(query_weight, p_norm)

            if len(features) != 0:
                similarities[document] = numpy.power(sum_query_document_weights / len(features), 1 / p_norm)
            else:
                similarities[document] = 0

        return similarities

    def get_maximum_tf(self, document, features):
        maximum_tf = 0.0
        for (term, index_by_term) in self.pre_processor.get_inverted_index().items():
            if term in features and document in index_by_term:
                tf = 1 + numpy.math.log(index_by_term[document].frequency, 2)
                if maximum_tf < tf:
                    maximum_tf = tf
        return maximum_tf

    def get_maximum_idf(self):
        maximum_idf = 0.0
        for (term, index_by_term) in self.pre_processor.get_inverted_index().items():
            number_of_documents_for_a_term = len(index_by_term.keys())
            idf = numpy.math.log((self.pre_processor.get_num_files() / number_of_documents_for_a_term), 2)
            if maximum_idf < idf:
                maximum_idf = idf
        return maximum_idf

    def print_similarity_results(self, feature_name, query_similarities):
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
