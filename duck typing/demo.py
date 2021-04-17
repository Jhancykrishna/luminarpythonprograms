class Pycharm:
    def open(self):
        print("open in pycharm")
    def run(self):
        print("run functionality in pycharm")
    def debug(self):
        print("debugging using pycharm")
class Vscode:
    def open(self):
        print("open in Vscode")
    def run(self):
        print("run functionality in Vscode")
    def debug(self):
        print("debugging using Vscode")

class Programmer:
    def coding(self,ide):
        self.ide=ide

py=Pycharm()
pg=Programmer()
pg.coding(py)
