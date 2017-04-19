from information_retrieval_methods.term_weigthing.tfidf import *

class TfIdfRunner:

    def __init__(self, pre_processor, features_dictionary):
        """Title.

           Body.
        """
        self.pre_processor = pre_processor
        self.features_dictionary = features_dictionary

    def run(self):
        """Executes the term weighting calculation.

           Body.
        """

        print('--------------------------------------------')
        print('              TERM WEIGHTING')
        print('--------------------------------------------')

        print(print_tfidf_results(self.features_dictionary, self.pre_processor))
