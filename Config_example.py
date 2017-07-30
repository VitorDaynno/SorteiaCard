class Config:
	
	api_Key = '' #Sua api_key
        token = '' # Seu token

	def __init__(self):
	    pass

	def get_Api_Key(self):
		return self.__class__.api_Key

	def get_Token(self):
		return self.__class__.token
