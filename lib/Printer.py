class Printer:
    def __init__(self):
        self.name = """  
 ┬─┐┌─┐┌┬┐┬┌─┐╔═╗┌─┐┬  ┌─┐┬┌┬┐
├┬┘├┤  │││└─┐╚═╗├─┘│  │ ││ │ 
┴└─└─┘─┴┘┴└─┘╚═╝┴  ┴─┘└─┘┴ ┴ """
        self.banner()

    def banner(self):
        print(self.name)
