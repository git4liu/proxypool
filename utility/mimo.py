from config import config
from utility.redismanager import RedisManager

def send_job(job_name, value):
    jobs = config.redis_jobs()
    job = jobs.get(job_name)
    if not job:
        return None
    rdb = RedisManager.get_instance()
    return rdb.lpush(job, value)


def receive_job(job_name):
    jobs = config.redis_jobs()
    job = jobs.get(job_name)
    if not job:
        return None
    rdb = RedisManager.get_instance()
    return rdb.rpop(job)


def add_service(service_name, value, score):
    if not score:
        score = 0
    service = config.redis_services().get(service_name)
    if not service:
        return None
    return RedisManager.get_instance().zadd(service, score, value)


def get_service(service_name, score_max, score_min=0, withscores=False):
    service = config.redis_services().get(service_name)
    if not service:
        return None
    return RedisManager.get_instance().zrangebyscore(
        name=service, min=score_min, max=score_max, withscores=withscores
    )

if __name__ == '__main__':
    add_service('58', 'http://fit58.com', 9)
    add_service('58', 'http://fit5d.com', 9)
    add_service('58', 'http://fids5d.com', 2)
    link = get_service('58', 4)
    print(link)
