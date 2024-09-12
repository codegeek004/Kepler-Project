class MockGPIO:
    OUT = 'OUT'
    IN = 'IN'
    HIGH = 'HIGH'
    LOW = 'LOW'
    BCM = 'BCM'
    BOARD = 'BOARD'
    
    def __init__(self):
        self.pins = {}
        self.mode = None
    
    def setmode(self, mode):
        self.mode = mode
    
    def setup(self, pin, mode):
        self.pins[pin] = mode
    
    def output(self, pin, state):
        if pin in self.pins and self.pins[pin] == self.OUT:
            pass
    
    def input(self, pin):
        return 0
    
    def cleanup(self):
        self.pins.clear()

GPIO = MockGPIO()

