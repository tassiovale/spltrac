
class FeatureExtractor:
    """Title.

        Body.
    """

    def __init__(self, project):
        """Title.

           Body.
        """
        self.features_dictionary = {}
        self.features_dictionary['floor'] = ['floor', 'floor1', 'floor2', 'floor3']
        self.features_dictionary['empty'] = ['empty', 'empty1', 'empty2', 'empty3']
        self.features_dictionary['to'] = ['to', 'to1', 'to2', 'to3']
        self.features_dictionary['da'] = ['da', 'da1', 'da2', 'da3']


    def get_features_dictionary(self):
        return self.features_dictionary