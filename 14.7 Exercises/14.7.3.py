class Password_manager:
	def __init__(self):
		self.old_passwords = [] 
		
	def get_password(self):
		return self.old_passwords[-1]

	def set_passwords(self,new_pass):
		if new_pass in self.old_passwords:
			return f"The password is in the list. Enter a new password."
		else:
			self.old_passwords.append(new_pass)
			return f"The password has been set."
		
	def is_correct(self, your_password):
		if your_password == self.old_passwords[-1]:
			return True
		else:
			return False

a = Password_manager()
print(a.set_passwords("password123")) #Output - The password has been set.
print(a.set_passwords("password123")) #Output - The password is in the list. 
                                      #Enter a new password.
print(a.get_password()) #Output - password123
print(a.is_correct("password123")) #Output - True
print(a.is_correct("password")) #Output - False 