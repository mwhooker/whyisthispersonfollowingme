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


def patch_user():
    import twitter
    twitter.User.__hash__ = fhash
    twitter.User.__cmp__ = fcmp
