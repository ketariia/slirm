class CPU:
    def check(self):
        print("Checking CPU")


class Memory:
    def check(self):
        print("Checking memory")


class HardDrive:
    def check(self):
        print("Checking hard drive")


class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self):
        self.cpu.check()
        self.memory.check()
        self.hard_drive.check()
        print("Computer started successfully")
computer = ComputerFacade()
computer.start()
