
class IRMethodRunner:
    """Title.

        Body.
    """

    def __init__(self, config_file_name):
        """Title.

           Body.
        """
        self.projects_base_path = ''
        self.config_file_name = config_file_name
        self.spl_projects = {}

    def get_projects_dictionary(self):
        """Title.

           Body.
        """
        config_file = open(self.config_file_name, 'r')

        self.projects_base_path = config_file.readline()

        for line in config_file:
            (project, language) = line.split()
            path = self.projects_base_path.replace('\n', '')  # it removes the newline character ('\n') from the path
            self.spl_projects[path + project] = language

        config_file.close()
        return self.spl_projects.items()

    def get_features_list(self, project):
        """Title.

           Body.
        """
        return ['floor', 'empty', 'to', 'da']

