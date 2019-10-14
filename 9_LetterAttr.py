class LetterAttr:
	def __getattr__(self, name):
		super().__setattr__(name, name)
		return name

	def __setattr__(self, name, val):
		if hasattr(self, name):
			s=''.join([l for l in val if l in name])
			super().__setattr__(name, s)




        
# A = LetterAttr()
# print("1", A.letter)
# print("2", A.digit)
# A.letter = "teller"
# print("3", A.letter)
# A.letter = "fortune teller"
# print("4", A.letter)