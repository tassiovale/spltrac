from nltk.tokenize import RegexpTokenizer
from collections import Counter
import glob


class DocumentDataByTerm:  # Objects from this class stores the frequency and weight of a term-document pair
    pass


class SPLProjectPreProcessor:

    def __init__(self, project, language):

        self.num_files = 0
        self.stop_words = []
        self.inverted_index = {}
        self.index_terms = set()
        self.documents = set()
        self.generate_index(project, language)

    def generate_index(self, project, language):
        """It builds the index for the SPL project files (documents).

           The method identifies all valid files to be processed and requests the
           processing of all term frequencies per document.
        """

        if language == 'c':
            self.count_term_document_frequency(project, '.c')
            self.count_term_document_frequency(project, '.h')
        elif language == 'java':
            self.count_term_document_frequency(project, '.java')

        stop_word_file = open('../files/stopwords_' + language + '.dat', "r")
        self.stop_words = [line.strip() for line in stop_word_file]
        stop_word_file.close()

    def count_term_document_frequency(self, project, file_extension):
        """This method builds the inverted index for terms and related documents.

           It is responsible for creating the data structure to store term-document data
           and count the frequencies of terms per document.
        """
        for file_name in glob.iglob(project + '/**/*' + file_extension, recursive=True):
            self.num_files += 1
            self.documents.add(file_name)

            # reading file
            source_file = open(file_name, 'r')
            file_content = source_file.read()
            source_file.close()

            tokenizer = RegexpTokenizer(r'[\w\']+')  # get tokens, removing punctuation and other single characters
            tokens = tokenizer.tokenize(file_content.lower())  # get tokens in lower case

            # counting frequencies for a specific file
            file_counter = Counter(tokens)

            for (term, frequency) in file_counter.most_common():
                self.index_terms.add(term)
                if frequency > 0:
                    aux_index = {}
                    document_data_by_term = DocumentDataByTerm()
                    document_data_by_term.frequency = frequency
                    document_data_by_term.weight = 0
                    aux_index[file_name] = document_data_by_term
                    try:
                        self.inverted_index[term].update(aux_index)
                    except KeyError:
                        self.inverted_index[term] = aux_index

    def get_term_document_frequency(self, term):
        doc_term_dictionary = self.inverted_index[term]
        return len(doc_term_dictionary.keys())

    def get_inverted_index(self):
        return self.inverted_index

    def get_num_files(self):
        return self.num_files

    def get_stop_words(self):
        return self.stop_words

    def get_index_terms(self):
        return self.index_terms

    def get_documents(self):
        return self.documents