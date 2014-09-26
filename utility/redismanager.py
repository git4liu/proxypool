import redis
from config import config


class RedisManager(object):

    rdb = None

    @staticmethod
    def get_instance():
        conf = config.redis_conf()
        if not RedisManager.rdb:
            RedisManager.rdb = redis.StrictRedis(
                host=conf['host'],
                port=conf['port'],
                db=conf['db']
            )
        return RedisManager.rdb




if __name__ == '__main__':
    rdb = RedisManager.get_instance()
    rdb.set('liujie', 'liujie1212')
    print(rdb.get('liujie'))
