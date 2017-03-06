from experiment.ir_method_runner import IRMethodRunner
from information_retrieval_methods.tfidf.tfidf import TfIdf


class TfIdfRunner(IRMethodRunner):

    def __init__(self, config_file_name='files/config_file.dat'):
        """Title.

           Body.
        """
        super(TfIdfRunner, self).__init__(config_file_name)

    def run(self):
        """Title.

           Body.
        """

        print('--------------------------------------------')
        print('   TF-IDF (TERM WEIGHTING ALGORITHM)')
        print('--------------------------------------------')

        for (project, language) in self.get_projects_dictionary():
            print('\n\nProject: ' + project)
            print('Language: ' + language.upper())

            # getting IDF for each feature
            tfidf = TfIdf(project, language)
            for feature in self.get_features_list(project):
                tfidf.calculate_weights()
                print(tfidf.print_term_results(feature))
