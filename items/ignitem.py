from gamedescription import GameDescription
from review import Review

class IgnItem(GameDescription, Review):
	def __init__(self):
		super(IgnItem, self).__init__()
		self._site = 'ign'

	@property 
	def site(self):
		return self._site