from bs4 import BeautifulSoup

from vxml.error import VXML_Error


class VXML_ReportIterator:
	def __init__(self, report):
		self._report = report
		self._index = 0
	def __next__(self):
		if self._index < len(self._report):
			result = self._report.errors[self._index]
			self._index += 1
			return result
		raise StopIteration
		

class VXML_Report:
	def __init__(self):
		self.file_path = ''
		self.command = ''
		self._soup = None
		self._kinds = []
		self.errors = []
	
	def __len__(self):
		return len(self.errors)	

	def load(self, file_path):
		self.file_path = file_path
		with open(self.file_path) as ff:
			content = ff.read()
		self._soup = BeautifulSoup(content, 'xml')
		self.command = [ line.text
				 for line in self._soup.find_all('line')
				 if 'Command' in line.text ][0][9:] 
		errors = self._soup.find_all('error')
		for error in errors:
			err = VXML_Error(error.kind.text)
			self.errors.append(err)
			if not error.kind.text in self._kinds:
				self._kinds.append(error.kind.text) 

	def count(self, var):
		cnt = 0
		for err in self.errors:
			if var == err.kind:
				cnt = cnt + 1
		return cnt	
	
	def get_kinds(self):
		return self._kinds	

	def get_file_path(self, complete=False):
		if complete:
			return self.file_path
		else:
			return self.file_path.split('/')[-1]
	def get_errors(self):
		return self.errors

	def __str__(self):
		ret = '\n{}\n'.format('-'*100)
		ret += 'File: {}\n'.format(self.file_path)
		ret += 'Number of errors: {}\n'.format(len(self))
		ret += 'Command: {}\n'.format(self.command[:100])
		ret += '{}\n'.format('-'*100)
		_kinds = self.get_kinds()
		for _k in _kinds:
			ret += '{}:\t{}\n'.format(_k, self.count(_k))
		ret += '{}\n'.format('-'*100)
		return ret

	def __iter__(self):
		return VXML_ReportIterator(self)
			
