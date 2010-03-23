from restkit import Resource
import json

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


class TwitterUsers(Resource):


    def __init__(self,  pool_instance=None, **kwargs):
        url = "http://api.twitter.com/1/users/"
        super(TwitterUsers, self).__init__(url, follow_redirect=True,
                                            max_follow_redirect=10,
                                            pool_instance=pool_instance,
                                            **kwargs)
    def Lookup(self, ids):
        def chunks(l, n):
            """ Yield successive n-sized chunks from l."""
            for i in xrange(0, len(l), n):
                yield l[i:i+n]

        #need to break up the requests in to groups of 20 ids
        id_chunks = list(chunks(ids, 20))

        people = []
        for ids in id_chunks:
            people += (self.get('lookup.json', user_id=','.join(map(str,ids))))
        return people

    def request(self, *args, **kwargs):
        resp = super(TwitterUsers, self).request(*args, **kwargs)
        return json.loads(resp.body)

class TwitterRateLimit(Resource):
    

    def __init__(self, pool_instance=None, **kwargs):
        url = "http://api.twitter.com/1/account/rate_limit_status.json"
        super(TwitterRateLimit, self).__init__(url, follow_redirect=True,
                                            max_follow_redirect=10,
                                            pool_instance=pool_instance,
                                            **kwargs)
    
    def request(self, *args, **kwargs):
        resp = super(TwitterRateLimit, self).request(*args, **kwargs)
        return json.loads(resp.body)
