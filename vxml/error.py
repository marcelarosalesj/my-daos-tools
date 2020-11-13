

class VXML_Error:
	def __init__(self, kind):
		self.kind = kind
	def get_kind(self):
		return self.kind
	def __str__(self):
		return self.kind



