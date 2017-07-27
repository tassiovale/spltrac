# -*- coding: utf-8 -*-
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import threading
from experiment.projects_multiprocessing import ProjectAnalysisThread
from evaluation.evaluator import EvaluationResults

"""SPLTrac: SPL Traceability Experimental Suite

Author: Tassio Vale
Website: www.tassiovale.com
Contact: tassio.vale@ufrb.edu.br
"""

# START READING THE PROJECTS METADATA
projects_config_path = '../files/projects_spl.dat'
with open('../files/projects_config.dat', 'r') as projects_config_file:
    projects_config_path = projects_config_file.readline()

config_file = open(projects_config_path, 'r')
projects_base_path = config_file.readline()

evaluation_results = EvaluationResults()
threads = []

for line in config_file:
    (project, language, variability_impl_technology, loc) = line.split()
    path = projects_base_path.replace('\n', '')  # it removes the newline character ('\n') from the path
    project = path + project

    # experiment.projects_multiprocessing.execute_processes(project, language, variability_impl_technology, loc, evaluation_results)

    thread = ProjectAnalysisThread(project, language, variability_impl_technology, loc, evaluation_results,)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

# consolidating results
print('Step 5: consolidating project results...')
evaluation_results.export_results()

config_file.close()

print('DONE\n\n')
