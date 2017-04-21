from information_retrieval_methods.algebraic.classic_vector import ClassicVectorModel

class ClassicVectorRunner:

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
        print('            CLASSIC VECTOR MODEL')
        print('--------------------------------------------')

        runner = ClassicVectorModel(self.features_dictionary, self.pre_processor)
        for feature_name in self.features_dictionary.keys():
            query_similarities = runner.calculate_similarities(feature_name)
            print(runner.print_similarity_results(feature_name, query_similarities))