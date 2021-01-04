import os
from vxml import VXMLReport

class VXMLReportTool:
    def __init__(self):
        self.path = ''
        self.reports = []

    def setup(self, path, verbose = 1):
        self.path = path
        self.verbose = verbose
        if os.path.isfile(path):
            xml_valgrind = VXMLReport(verbose)
            xml_valgrind.load(path)
            self.reports.append(xml_valgrind)
        elif os.path.isdir(path):
            self._xml_files = ['{}/{}'.format(path, i)
                               for i in os.listdir(path)
                               if i.endswith(".xml")]
            if not self._xml_files:
                print('Empty directory - no XMLs')
            else:
                for xml in self._xml_files:
                        xml_valgrind = VXMLReport(verbose)
                        xml_valgrind.load(xml)
                        self.reports.append(xml_valgrind)
        else:
            print('Wrong input')

    def print_reports(self, reverse = False):
        if len(self.reports) > 0:
            if not reverse:
                for report in self.reports:
                    if report:
                        print(report, end='')
            else:
                reverse_summary = {}
                for report in self.reports:
                    kinds = report.get_kinds()
                    for kind in kinds:
                        if not kind in reverse_summary:
                            reverse_summary[kind] = [report]
                        else:
                            reverse_summary[kind].append(report)
                for key, value in reverse_summary.items():
                    if key == 'Leak_StillReachable' and self.verbose == 0:
                        pass
                    else:
                        print('\n'+'-'*100)
                        print(key)
                        print('-'*100)
                        for val in value:
                            print('{}\t\t\t{}'.format(val.get_file_path(),
                                                      val.count(key)))
                        print('-'*100+'\n')

