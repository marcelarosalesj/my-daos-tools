''' Module that contains report class for Valgrind XMLs '''

from bs4 import BeautifulSoup
from vxml.error import VXMLError


class VXMLReportIterator:
    '''
    VXMLReportIterator let VXMLReport iterate
    '''
    def __init__(self, report):
        '''
        Constructor for VXMLReportIterator
        '''
        self._report = report
        self._index = 0
    def __next__(self):
        '''
        next
        '''
        if self._index < len(self._report):
            result = self._report.errors[self._index]
            self._index += 1
            return result
        raise StopIteration


class VXMLReport:
    '''
    VXMLReport class that represents Valgrind VXMLs
    '''
    def __init__(self, verbose=0):
        '''
        Constructor for VXMLReport class
        '''
        self.file_path = ''
        self.command = ''
        self._soup = None
        self._kinds = []
        self.errors = []
        self.verbose = verbose

    def __len__(self):
        return len(self.errors)

    def __str__(self):
        header = '\n{}\n'.format('-'*100)
        header += 'File: {}\n'.format(self.file_path)
        header += 'Number of errors: {}\n'.format(len(self))
        header += 'Command: {}\n'.format(self.command[:100])
        header += '{}\n'.format('-'*100)
        ret = ''

        if self.verbose == 0 and len(self._kinds) == 1:
            if self._kinds[0] == 'Leak_StillReachable':
                return ret

        for _kind in self._kinds:
            if self.verbose == 0 and _kind == 'Leak_StillReachable':
                pass
            else:
                ret += '{}:\t{}\n'.format(_kind, self.count(_kind))
        ret += '{}\n'.format('-'*100)
        ret = header + ret
        return ret

    def __iter__(self):
        return VXMLReportIterator(self)

    def load(self, file_path):
        '''
        load an xml file to fill this report
        '''
        self.file_path = file_path
        with open(self.file_path) as xml_file:
            content = xml_file.read()
        self._soup = BeautifulSoup(content, 'xml')
        """
        self.command = [line.text for line in self._soup.find_all('line')
                        if 'Command' in line.text][0][9:]
        """
        for line in self._soup.find_all('line'):
            if 'Command' in line.text:
                self.command = line.text[0][9:]

        errors = self._soup.find_all('error')
        for error in errors:
            err = VXMLError(error.kind.text)
            self.errors.append(err)
            if not error.kind.text in self._kinds:
                self._kinds.append(error.kind.text)

    def count(self, var):
        '''
        Return how many errors are in this report
        '''
        cnt = 0
        for err in self.errors:
            if var == err.kind:
                cnt = cnt + 1
        return cnt

    def get_kinds(self):
        '''
        Return the report's kinds of errors
        '''
        return self._kinds

    def get_file_path(self, complete=False):
        '''
        Return the report's path
        '''
        if complete:
            return self.file_path
        else:
            return self.file_path.split('/')[-1]
    def get_errors(self):
        '''
        Return the report's errors
        '''
        return self.errors
