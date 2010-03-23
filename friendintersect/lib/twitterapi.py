from restkit import ConnectionPool, BasicAuth
from friendintersect.model.twitter import *
from pylons import config


pool = ConnectionPool(max_connections=5)
auth = BasicAuth(config.get('twitter.username'), config.get('twitter.password'))

peeps = TwitterUsers(pool, filters=[auth])
thesocial = TwitterSocialGraph(pool)
nolimits = TwitterRateLimit(pool)
