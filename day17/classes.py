
class User:

    def __init__(self, userId, username):
        self.id = userId
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User("0001", "matze")
user2 = User("0002", "jack")
#user1.id = "0001"
#user1.username = "matze"

print(user1.username)

