
class VXMLReportTool:
    def __init__(self):
        self.path = ''

    def setup(self, path):
        self.path = path
        self._xml_files = ['{}/{}'.format(path, i) for i in os.listdir(path) if i.endswith(".xml")]
        for xml in self._xml_files:
                xml_valgrind = VXMLReport()
                xml_valgrind.load(xml)
