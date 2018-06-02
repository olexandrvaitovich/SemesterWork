class User:
	'''Abstract class user which
	 controls the program'''
    def __init__(self):
    	'''Initialize class instance'''
        pass
    def check_screen(self):
    	'''Checking which screen is current'''
        return sm.current
    def change screen(self):
    	'''Change screen on another'''
        pass
    def change_login(self):
    	'''Change your login'''
        pass
    def change_password(self):
    	'''Change your password'''
        pass
    def change_recipient(self):
    	'''Change the recipient of your location'''
        pass

class ScreenChecker(User):
	def check_screen(self):
		return super().check_screen()