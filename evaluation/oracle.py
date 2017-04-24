

class TraceabilityOracle:
    """Title.

        Body.
    """

    def __init__(self, project):
        """Title.

           Body.
        """
        self.project = project
        self.true_traces = {}

    def extract_true_traces(self):
        try:
            oracle_file = open(self.project + '/traceability_oracle.dat', "r")
            for line in oracle_file:
                terms = line.strip().split(':')
                if terms:
                    key_feature = terms[0]
                    synonyms = terms[-1].split(',')
                    for document in synonyms:
                        document = self.project + '/' + document
                        if key_feature in self.true_traces:
                            self.true_traces[key_feature] += (document,)
                        else:
                            self.true_traces[key_feature] = (document,)
            oracle_file.close()
            # print(self.true_traces)
        except FileNotFoundError:
            print('No oracle available')

        return self.true_traces