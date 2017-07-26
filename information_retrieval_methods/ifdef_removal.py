# -*- coding: utf-8 -*-
"""SPLTrac: SPL Traceability Experimental Suite

Author: Tassio Vale
Website: www.tassiovale.com
Contact: tassio.vale@ufrb.edu.br

This code tests the procedure for removing all ifdef directives from the IR analysis.
"""

file_name = '../files/ifdef_test.txt'

# reading file
try:
    source_file = open(file_name, 'r')
    file_content = source_file.read()
    source_file.close()
except UnicodeDecodeError:
    source_file = open(file_name, 'r', encoding="ISO-8859-1")
    file_content = source_file.read()
source_file.close()

print('\n--- OLD ---')
print(file_content)

lines = file_content.splitlines()
for line in lines:
    if '#if' in line:
        lines.remove(line)

file_content = '\n'.join(lines)
print('\n--- NEW ---')
print(file_content)