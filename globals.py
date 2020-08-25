from person import Person
from party import Party

global users, parties, user1, user2, user3, user4, party1, party2, party3, party4

user1 = Person("John Peterson", "123")
user2 = Person("Peter Johnson", "321")
user3 = Person("Eva Jackson", "456")
user4 = Person("Jackie Evans", "654")

party1 = Party("Oaks", 0)
party2 = Party("Lakes", 0)
party3 = Party("Foxes", 0)
party4 = Party("Stars", 0)

users = [user1, user2, user3, user4]
parties = [party1, party2, party3, party4]
