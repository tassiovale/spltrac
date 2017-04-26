from evaluation.metrics import ProjectMethodMetricsResult
import datetime
import csv
import os


class ProjectResults:
    pass


class EvaluationResults:

    def __init__(self, ):
        self.project_results = {}

    def add_project_input_data(self, project, language, loc, true_traces):
        project_result = ProjectResults()
        project_result.language = language
        project_result.loc = loc
        project_result.true_traces = true_traces
        # print('True traces: ' + str(self.true_traces))
        project_result.method_results = {}
        self.project_results[project] = project_result

    def add_method_results(self, project, method_name, method_traces):
        # print('\nMethod traces - ' + method_name + ': ' + str(method_traces))
        method_result = ProjectMethodMetricsResult(self.project_results[project].true_traces, method_traces)
        self.project_results[project].method_results[method_name] = method_result

    def consolidate_results(self):
        pass

    def export_results(self):
        date_time_str = datetime.datetime.now().strftime('%Y-%m-%d_%Hh%Mm')
        output_file_str = date_time_str + '_output.csv'
        with open('results/' + output_file_str, 'w') as csv_file:
            output_data_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
            output_data_writer.writerow(['project', 'language', 'loc', 'features', 'method', 'recall', 'precision', 'fmeasure'])
            for (project, project_result) in self.project_results.items():
                for (method, method_result) in project_result.method_results.items():
                    output_data_writer.writerow([project.split('/')[-1], project_result.language, project_result.loc, len(project_result.true_traces.keys()), method, method_result.recall, method_result.precision, method_result.f_measure])

            with open("results/script_template.R", "r") as template_script_file:
                script_data = template_script_file.read()
                # print(script_data)
                script_data = script_data.replace('<directory>', os.getcwd() + '/results/')
                script_data = script_data.replace('<output_file_name>', output_file_str)
                script_data = script_data.replace('<pdf_image_file_name>', date_time_str + '_chart')

                resulting_script_file = open('../experiment/results/' + date_time_str + '_script.R', "w")
                resulting_script_file.write(script_data)
                resulting_script_file.close()

