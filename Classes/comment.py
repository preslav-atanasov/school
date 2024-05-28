class Comment:
    def __init__(self, username, content, likes = 0):
        self.username = username
        self.content = content
        self.likes = likes


comment1 = Comment("user1", "I like this book")
comment2 = Comment("user2", "nigger", 569)

print(comment1.username)
print(comment1.content)
print(comment1.likes)

print(comment2.username)
print(comment2.content)
print(comment2.likes)
