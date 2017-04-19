from information_retrieval_methods.algebraic.classic_vector import *

class ClassicVectorRunner:

    def __init__(self, pre_processor, features_list):
        """Title.

           Body.
        """
        self.pre_processor = pre_processor
        self.features_list = features_list

    def run(self):
        """Executes the term weighting calculation.

           Body.
        """

        print('--------------------------------------------')
        print('            CLASSIC VECTOR MODEL')
        print('--------------------------------------------')

        for feature in self.features_list:
            print(print_feature_results(feature, self.pre_processor))