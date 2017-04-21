import numpy

class ClassicVectorModel:

    def __init__(self, features_dictionary, pre_processor):

        self.features_dictionary = features_dictionary
        self.pre_processor = pre_processor

    def calculate_similarities(self, feature_name):

        features = self.features_dictionary[feature_name]
        similarities = {}

        for document in self.pre_processor.get_documents():
            sum_weights = 0.0
            document_norm = 0.0

            for (term, index_by_term) in self.pre_processor.get_inverted_index().items():
                if document in index_by_term:
                    document_norm += numpy.square(index_by_term[document].weight)
                if term in features:
                    index_by_term = self.pre_processor.get_inverted_index()[term]
                    if document in index_by_term:
                        term_document_ocurrences = self.pre_processor.get_term_document_frequency(term)
                        idf = numpy.math.log((self.pre_processor.get_num_files() / term_document_ocurrences), 2)
                        tf = index_by_term[document].weight
                        sum_weights += tf * idf

            if document_norm != 0:
                similarities[document] = sum_weights / numpy.sqrt(document_norm)
            else:
                similarities[document] = 0

        return similarities

    def print_similarity_results(self, feature_name, query_similarities):
        if feature_name not in self.pre_processor.get_stop_words():
            try:
                print('\n' + repr('FEATURE: ' + feature_name).ljust(10))
                print(repr('DOCUMENT').ljust(50), repr('IDF').ljust(10))
                for (document, similarity) in query_similarities.items():
                    print(repr(document).ljust(50), repr(str(similarity)).ljust(10))
            except KeyError:
                print('WARNING: feature not traced')
        else:
            print('ERROR: *' + feature_name + '* is a stopword')
