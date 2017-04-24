from evaluation.metrics import ProjectMethodMetricsResult


class ProjectEvaluationResult:

    def __init__(self, project, true_traces):
        self.project = project
        self.true_traces = true_traces
        # print('True traces: ' + str(self.true_traces))
        self.method_results = {}

    def add_method_results(self, method_name, method_traces):
        # print('\nMethod traces - ' + method_name + ': ' + str(method_traces))
        method_result = ProjectMethodMetricsResult(self.true_traces, method_traces)
        self.method_results[method_name] = method_result

    def get_project(self):
        return self.project
