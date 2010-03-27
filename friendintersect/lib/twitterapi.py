from restkit import ConnectionPool, BasicAuth
from friendintersect.model.twitter import *
from restkit.http_cache import HttpCache
from pylons import config


pool = ConnectionPool(max_connections=5)
auth = BasicAuth(config.get('twitter.username'), config.get('twitter.password'))
cache = HttpCache()

peeps = TwitterUsers(pool, filters=[auth, cache])
thesocial = TwitterSocialGraph(pool, filters=[cache])
nolimits = TwitterRateLimit(pool)
