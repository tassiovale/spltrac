import math
from nltk.tokenize import RegexpTokenizer
from collections import Counter
import glob

__author__ = "Tassio Vale"
__email__ = "tassio dot vale at ufrb dot edu dot br"

class DocumentTermFrequency:
    pass

class TfIdf:
    """Tf-idf class implementing http://en.wikipedia.org/wiki/Tf-idf.

        The library constructs an IDF corpus and stopword list either from
        documents specified by the client, or by reading from input files.  It
        computes IDF for a specified term based on the corpus, or generates
        keywords ordered by tf-idf for a specified document.
    """

    def __init__(self, project, language):

        self.num_files = 0
        self.stopwords = []
        self.tfidf_results = {}
        self.generate_results(project, language)

    def generate_results(self, project, language):
        """Title.

           Body.
        """

        if language == 'c':
            self.process_files_per_term(project, '.c')
            self.process_files_per_term(project, '.h')
        elif language == 'java':
            self.process_files_per_term(project, '.java')

        stopword_file = open('files/stopwords_' + language + '.dat', "r")
        self.stopwords = [line.strip() for line in stopword_file]
        stopword_file.close()

    def process_files_per_term(self, project, file_extension):
        """Title.

           Body.
        """
        for file_name in glob.iglob(project + '/**/*' + file_extension, recursive=True):
            self.num_files += 1

            # reading file
            source_file = open(file_name, 'r')
            file_content = source_file.read()
            source_file.close()

            tokenizer = RegexpTokenizer(r'[\w\']+')  # get tokens, removing punctuation and other single characters
            tokens = tokenizer.tokenize(file_content.lower())  # get tokens in lower case

            # counting frequencies for a specific file
            file_counter = Counter(tokens)

            for (term, frequency) in file_counter.most_common():
                if frequency > 0:
                    doc_term_dictionary = {}
                    doc_term_frequency = DocumentTermFrequency()
                    doc_term_frequency.frequency = frequency
                    doc_term_frequency.tf_idf = 0
                    doc_term_dictionary[file_name] = doc_term_frequency
                    try:
                        self.tfidf_results[term].update(doc_term_dictionary)
                    except KeyError:
                        self.tfidf_results[term] = doc_term_dictionary

    def calculate_weights(self):
        """Retrieve the IDF for the specified term.
    
           This is computed by taking the logarithm of (
           (number of documents in corpus) divided by (number of documents
            containing this term) ).
         """

        for (term, doc_term_dictionary) in self.tfidf_results.items():
            larger_term_frequency = self.get_highest_document_frequency(term)
            for doc_term_frequency in doc_term_dictionary.values():
                tfidf_term_document = (1 + math.log(doc_term_frequency.frequency)) \
                                      * math.log(self.num_files / larger_term_frequency)
                doc_term_frequency.tf_idf = tfidf_term_document

    def get_highest_document_frequency(self, term):
        doc_term_dictionary = self.tfidf_results[term]
        highest_termfrequency = 0
        for (document, doc_term_frequency) in doc_term_dictionary.items():
            if doc_term_frequency.frequency > highest_termfrequency:
                highest_termfrequency = doc_term_frequency.frequency
        return highest_termfrequency

    def print_term_results(self, term):
        if term not in self.stopwords:
            try:
                print('\n' + repr('FEATURE: ' + term).ljust(10))
                print(repr('DOCUMENT').ljust(50), repr('IDF').ljust(10))
                for (document, doc_term_dictionary) in self.tfidf_results[term].items():
                    print(repr(document).ljust(50), repr(str(doc_term_dictionary.tf_idf)).ljust(10))
            except KeyError:
                print('WARNING: feature not traced')
        else:
            print('ERROR: the term is a stopword')
