
class TwitterMock(object):
    ME = '1'
    THEM = '2'

    my_friends = [4, 5, 6, 400]
    my_followers = [3, 401]

    their_friends = [5, 3, 402]
    their_followers = []

    def __init__(*args, **kwargs):
        pass

    def GetFriends(self, id):
        if id == self.ME:
            return self.my_friends

        if id == self.THEM:
            return self.their_friends

    def GetFollowers(self, id):
        if id == self.ME:
            return self.my_followers

        if id == self.THEM:
            return self.their_followers
