from pylons import config
from twitter import Api

def fhash(self):
    return self.id

def fcmp(self, other):
    """self < other, zero if self == other, a positive integer if self >
    other. """
    if self.id < other.id:
        return -1
    if self.id == other.id:
        return 0
    if self.id > other.id:
        return 1


api = Api(username=config.get('twitter.username'),
                  password=config.get('twitter.password'))

api.__hash__ = fhash
api.__fcmp__ = fcmp
