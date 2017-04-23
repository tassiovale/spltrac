import numpy


def neural_network_run(features_dictionary, pre_processor):
    """Executes the term weighting calculation.

       Body.
    """

    print('--------------------------------------------')
    print('               NEURAL NETWORK')
    print('--------------------------------------------')

    for feature_name in features_dictionary.keys():
        neural_network = calculate_activation_levels(features_dictionary, pre_processor, feature_name)
        print(print_similarity_results(pre_processor, feature_name, neural_network))


def calculate_activation_levels(features_dictionary, pre_processor, feature_name):

    features = features_dictionary[feature_name]
    neural_network = Graph()
    sum_query_weights = 0.0
    sum_document_term_weights = {}

    # calculating norm of query and document vectors
    for document in pre_processor.get_documents().keys():
        document_term_weight = 0.0
        for (term_node_object, index_by_term) in pre_processor.get_inverted_index().items():
            if term_node_object in features and document in index_by_term:
                index_by_term = pre_processor.get_inverted_index()[term_node_object]
                term_document_ocurrences = pre_processor.get_docs_per_term(term_node_object)
                sum_query_weights += numpy.square(numpy.math.log((pre_processor.get_num_files() / term_document_ocurrences), 2))
                document_term_weight += numpy.square(1 + numpy.math.log(index_by_term[document].frequency, 2))
        if document_term_weight != 0.0:
            sum_document_term_weights[document] = numpy.sqrt(document_term_weight)
    sum_query_weights = numpy.sqrt(sum_query_weights)

    # initial activations
    for document in pre_processor.get_documents().keys():
        for (term_node_object, index_by_term) in pre_processor.get_inverted_index().items():
            if term_node_object in features and document in index_by_term:
                index_by_term = pre_processor.get_inverted_index()[term_node_object]
                term_document_ocurrences = pre_processor.get_docs_per_term(term_node_object)
                idf = numpy.math.log((pre_processor.get_num_files() / term_document_ocurrences), 2)
                tf = 1 + numpy.math.log(index_by_term[document].frequency, 2)

                wiq = idf / sum_query_weights
                wij = tf / sum_document_term_weights[document]

                neural_network.add_node(term_node_object, wiq)
                neural_network.add_node(document, 0.0)
                neural_network.update_edge(term_node_object, document, wiq * wij, wij)

    iterations_file = open('../files/neural_network_iterations.dat', "r")
    iterations = int(iterations_file.readline())
    iterations_file.close()

    # performing automatic iterations
    for i in range(1, iterations+1):
        for node_id in neural_network.get_nodes():
            if node_id in pre_processor.get_documents():
                document_node = neural_network.get_node(node_id)
                for term_node in document_node.get_connections():
                    if term_node.get_id() in features:
                        edge_weight = document_node.get_neighbor_edge_weight(term_node.get_id())
                        if edge_weight is not None:
                            term_node.update_activation_level(document_node.get_activation_level() * edge_weight)
                            document_node.update_activation_level(term_node.get_activation_level() * edge_weight)

    return neural_network


def print_similarity_results(pre_processor, feature_name, neural_network):
    if feature_name not in pre_processor.get_stop_words():
        print('\n' + repr('FEATURE: ' + feature_name).ljust(10))
        print(repr('DOCUMENT').ljust(50), repr('IDF').ljust(10))
        for document in pre_processor.get_documents().keys():
            document_node = neural_network.get_node(document)
            if document_node is not None:
                print(repr(document).ljust(50), repr(str(document_node.get_activation_level())).ljust(10))
            else:
                print('WARNING: feature *' + feature_name + '* not traced')
    else:
        print('ERROR: *' + feature_name + '* is a stopword')


class Node:
    def __init__(self, node_id, act_level=0.0):
        self.id = node_id
        self.activation_level = act_level
        self.adjacent = {}

    def update_neighbor(self, neighbor, weight=0.0):
        if neighbor in self.adjacent:
            self.adjacent[neighbor] += weight
        else:
            self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_neighbor_edge_weight(self, neighbor):
        if neighbor in self.adjacent:
            return self.adjacent[neighbor]
        else:
            return None

    def get_activation_level(self):
        return self.activation_level

    def update_activation_level(self, act_level):
        self.activation_level += act_level


class Graph:
    def __init__(self):
        self.node_dict = {}
        self.num_nodes = 0

    def __iter__(self):
        return iter(self.node_dict.values())

    def add_node(self, node_id, activation_level=0.0):
        self.num_nodes += 1
        new_node = Node(node_id, activation_level)
        self.node_dict[node_id] = new_node
        return new_node

    def get_node(self, node_id):
        if node_id in self.node_dict:
            return self.node_dict[node_id]
        else:
            return None

    def update_edge(self, source_node, dest_node, new_dest_act_level, weight=0.0):
        if source_node not in self.node_dict:
            self.add_node(source_node)
        if dest_node not in self.node_dict:
            self.add_node(dest_node)
        self.node_dict[dest_node].update_activation_level(new_dest_act_level)
        self.node_dict[source_node].update_neighbor(self.node_dict[dest_node], weight)
        self.node_dict[dest_node].update_neighbor(self.node_dict[source_node], weight)

    def get_nodes(self):
        return self.node_dict.keys()