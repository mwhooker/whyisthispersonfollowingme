from restkit import Resource, ConnectionPool, BasicAuth
import json

pool = ConnectionPool(max_connections=5)
#auth = BasicAuth("username", "password")

class TwitterSocialGraph(Resource):

    def __init__(self,  pool_instance=None, **kwargs):
        friends_url = "http://api.twitter.com/1/"
        super(TwitterSocialGraph, self).__init__(friends_url, follow_redirect=True,
                                            max_follow_redirect=10,
                                            pool_instance=pool_instance,
                                            **kwargs)

    def GetFollowers(self, id):
        """TODO: if followers > 5000, this won't work"""
        followers = self.get('followers/ids/%s.json' % id, cursor=-1)
        return followers['ids']

    def GetFriends(self, id):
        """TODO: if friends > 5000, this won't work"""
        friends = self.get('friends/ids/%s.json' % id, cursor=-1)
        return friends['ids']

    def request(self, *args, **kwargs):
        resp = super(TwitterSocialGraph, self).request(*args, **kwargs)
        return json.loads(resp.body)


thesocial = TwitterSocialGraph(pool)
