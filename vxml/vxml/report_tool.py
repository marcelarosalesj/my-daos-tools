import os
from vxml import VXMLReport

class VXMLReportTool:
    def __init__(self):
        self.path = ''
        self.reports = []

    def setup(self, path):
        self.path = path
        if os.path.isfile(path):
            xml_valgrind = VXMLReport()
            xml_valgrind.load(path)
            self.reports.append(xml_valgrind)
        elif os.path.isdir(path):
            self._xml_files = ['{}/{}'.format(path, i)
                               for i in os.listdir(path) if i.endswith(".xml")]
            if not self._xml_files:
                print('Empty directory - no XMLs')
            else:
                for xml in self._xml_files:
                        xml_valgrind = VXMLReport()
                        xml_valgrind.load(xml)
                        self.reports.append(xml_valgrind)
        else:
            print('Wrong input')
