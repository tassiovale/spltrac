import glob
import os
from xml.dom import minidom


class FeatureExtractor:
    """Title.

        Body.
    """

    def __init__(self, project, method):
        """Title.

           Body.
        """
        self.project = project
        self.method = method
        self.features_dictionary = {}

    def analyze_project(self):
        if self.method == 'featurehouse':
            self.extract_feature_house_features()
        elif self.method == 'cide':
            self.extract_cide_features()
        elif self.method == 'antenna':
            self.extract_antenna_features()
        elif self.method == 'ahead':
            self.extract_ahead_features()
        elif self.method == 'hyperj':
            self.extract_hyper_j_features()
        else:  # features for the test project called Test-project
            self.features_dictionary['to'] = ('to',)
            self.features_dictionary['da'] = ('da',)

        self.extract_thesaurus()
        print(self.features_dictionary)

    def extract_feature_house_features(self):
        exp_files_list = glob.glob(self.project + '/**/*.exp', recursive=True)
        if exp_files_list:
            self.read_features_plain_list_file(exp_files_list[0])
        else:
            features_files_list = glob.glob(self.project + '/**/*All.features', recursive=True)
            if features_files_list:
                self.read_features_plain_list_file(features_files_list[0])
            else:
                self.read_model_xml()

    def extract_cide_features(self):
        model_m_list = glob.glob(self.project + '/model.m', recursive=True)
        if model_m_list:
            model_m_file = open(model_m_list[0], "r")
            for line in model_m_file:
                elements = line.split(' ')
                if ':' in line and elements[0]:
                    self.features_dictionary[elements[0].lower()] = (elements[0].lower(),)
                for element in elements:
                    if '[' in element:
                        feature = element.replace('[', '')
                        feature = feature.replace(']', '')
                        self.features_dictionary[feature.lower()] = (feature.lower(),)

    def extract_ahead_features(self):
        self.read_model_xml()

    def extract_antenna_features(self):
        self.read_model_xml()

    def extract_hyper_j_features(self):
        feature_folder_list = glob.glob(self.project + '/**/src/feature', recursive=True)
        if feature_folder_list:
            for folder_name in os.walk(feature_folder_list[0]):
                if folder_name:
                    feature_name = folder_name[0].split('/')[-1]
                    self.features_dictionary[feature_name.lower()] = (feature_name.lower(),)

    def read_features_plain_list_file(self, file_name):
        features_file = open(file_name, "r")
        for feature in [line.strip() for line in features_file]:
            if feature:
                self.features_dictionary[feature.lower()] = (feature.lower(),)
        features_file.close()

    def read_model_xml(self):
        xml_files_list = glob.glob(self.project + '/**/*model.xml', recursive=True)
        if xml_files_list:
            self.extract_features_into_xml(xml_files_list[0])

    def extract_features_into_xml(self, file_name):
        document = minidom.parse(file_name)
        feature_list = document.getElementsByTagName('feature')
        and_list = document.getElementsByTagName('and')
        or_list = document.getElementsByTagName('or')
        alt_list = document.getElementsByTagName('alt')
        full_list = feature_list + and_list + or_list + alt_list
        for element in full_list:
            if 'abstract' not in element.attributes:
                feature = element.attributes['name'].value
                self.features_dictionary[feature.lower()] = (feature.lower(),)
        print(self.features_dictionary)

    def extract_thesaurus(self):
        try:
            thesaurus_file = open(self.project + '/thesaurus.dat', "r")
            for line in thesaurus_file:
                terms = line.strip().split(':')
                if terms:
                    key_feature = terms[0]
                    synonyms = terms[-1].split(',')
                    for feature in synonyms:
                        if key_feature in self.features_dictionary:
                            self.features_dictionary[key_feature.lower()] += (feature.lower(),)
            thesaurus_file.close()
        except FileNotFoundError:
            print('No thesaurus available')

    def get_features_dictionary(self):
        return self.features_dictionary
