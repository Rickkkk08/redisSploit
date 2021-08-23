from optparse import OptionParser


class Parser:
    def __init__(self):
        optParser = OptionParser()
        optParser.add_option('-u', '--url', help='target ip', action='store', type="string", dest='url')
        optParser.add_option('-p', '--port', help='target port', action='store', type="int", dest='port')
        optParser.add_option('-a', '--auth', help='Authentication', action='store', type="string", dest='auth')
        optParser.add_option('-d', '--disflush', help='disable flushall', action='store_false', dest='flush')
        optParser.add_option('--rsa', help='use pub key writing module', action='store_true', dest='rsa')
        optParser.add_option('--shell', help='use shell writing module', action='store_true', dest='shell')
        optParser.add_option('--cron', help='use cron writing module[ubuntu is not applicable]', action='store_true', dest='cron')
        optParser.add_option('--slave', help='use redis-rce module[Redis4.x-5.x]', action='store_true', dest='slave')

        self.options, self.args = optParser.parse_args()
        if not self.options.url or not self.options.port:
            exit("Invalid arguments, -u or -p is in need")
