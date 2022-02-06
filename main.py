class User:
  def __init__(self, name):
    self.name = name
    self.age = None
    self.gender = "Rather Not Say"
    self.phone = None
    self.email = None


class UserBuilder:
  def __init__(self, name):
    self.user = User(name)

  def set_age(self, value):
    self.user.age = value
    return self  #Returning self in these set functions helps to chain these functions

  def set_gender(self, value):
    self.user.gender = value
    return self

  def set_phone(self, value):
    self.user.phone = value
    return self

  def set_email(self, value):
    self.user.email = value
    return self

  def build(self):
    return {
		"Name": self.user.name,
		"Age": self.user.age if self.user.age is not None else "-",
		"Gender": self.user.gender,
		"Phone": self.user.phone if self.user.phone is not None else "-",
		"Email": self.user.email if self.user.email is not None else "-",
	}


user1 = UserBuilder("John")
user1.set_age(21).set_gender("Male")

print("User1 => ", user1.build())


user2 = UserBuilder("Jane")
user2.set_gender("Femail").set_email("jane@gmail.com")

print("User2 => ", user2.build())
