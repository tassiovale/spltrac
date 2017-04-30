"""SPLTrac: SPL Traceability Experimental Suite

Author: Tassio Vale
Website: www.tassiovale.com
Contact: tassio.vale@ufrb.edu.br
"""


class TraceabilityOracle:
    """The provided SPL projects already have the mapped feature-to-code traces.
    This class is provides data structure and algorithm to extract such traces called 'true traces'.
    """

    def __init__(self, project):
        self.project = project
        self.true_traces = {}

    def extract_true_traces(self):
        """It extracts the true traces from the traceability_oracle.dat file."""
        try:
            oracle_file = open(self.project + '/traceability_oracle.dat', "r")
            for line in oracle_file:
                if ':' in line:
                    terms = line.strip().split(':')
                    if terms[-1] is 'none':
                        self.true_traces[key_feature] += ()
                    else:
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
