from information_retrieval_methods.pre_processor import SPLProjectPreProcessor
from features_extraction.extractor import FeatureExtractor
from information_retrieval_methods.term_weigthing.tfidf import calculate_weights
from information_retrieval_methods.term_weigthing.runner import TfIdfRunner
from information_retrieval_methods.algebraic.classic_vector_runner import ClassicVectorRunner
from information_retrieval_methods.set_theoretic.runner import ExtendedBooleanRunner


def get_projects_dictionary(config_file_name='../files/config_file.dat'):
    """Title.

       Body.
    """

    spl_projects = {}
    config_file = open(config_file_name, 'r')

    projects_base_path = config_file.readline()

    for line in config_file:
        (project, language) = line.split()
        path = projects_base_path.replace('\n', '')  # it removes the newline character ('\n') from the path
        spl_projects[path + project] = language

    config_file.close()
    return spl_projects.items()


# EXECUTION OF THE INFORMATION RETRIEVAL ALGORITHMS

for (project, language) in get_projects_dictionary():
    print('\n\nProject: ' + project)
    print('Language: ' + language.upper())

    pre_processor = SPLProjectPreProcessor(project, language)
    calculate_weights(pre_processor)  # calculating weight through TF-IDF for each feature

    feature_extractor = FeatureExtractor(project)
    features_dictionary = feature_extractor.get_features_dictionary()

    # Term weighting algorithm
    tfidf = TfIdfRunner(pre_processor, features_dictionary)
    tfidf.run()

    # Algebraic - classic vector model
    classic_vector = ClassicVectorRunner(pre_processor, features_dictionary)
    classic_vector.run()

    # Algebraic - neural networks model

    # Set theoretic - extended boolean model
    extended_boolean = ExtendedBooleanRunner(pre_processor, features_dictionary)
    extended_boolean.run()

    # Probabilistic - BM25 model

