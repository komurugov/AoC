import sys

Pulses = []
LowCnt = 0
HighCnt = 0

class Module:
    def __init__(self, name):
        self.name = name
        self.rcvs = []
    def AddRcv(self, rcv):
        self.rcvs.append(rcv)
        
class Button(Module):
    def Push(self):
        for rcv in self.rcvs:
            Pulses.append((self, rcv, False))
            
class Broadcaster(Module)
    def Process(self, trnsmtr, pulse):
        for r in self.rcvs:
            Pulses.append((self, r, pulse))
            
class Flipflop(Module):
    on = False
    def Process(self, trnsmtr, pulse):
        if not pulse:
            self.on = not self.on
            for rcv in self.rcvs:
                Pulses.append((self, rcv, self.on))

class Conjunction(Module):
    transmitters = {}
    def AddTransmitter(self, transmitter):
        self.transmitters[transmitter] = False
    def Process(self, trnsmtr, pulse):
        self.transmitters[trnsmtr] = pulse
        for rcv in self.rcvs:
            Pulses.append((self, rcv, not all(self.transmitters[t] for t in self.transmitters)))
            
lines = {}
modules = { 'button': Button('button'), 'broadcaster': Broadcaster('broadcaster') }
for line in sys.stdin:
    if line.find('broadcaster') == 0:
        name = 'broadcaster'
    else:
        name = line[1:line.find(' ')]
        if line[0] == '%':
            modules[name] = Flipflop(name)
        elif line[0] == '&':
            modules[name] = Conjunction(name)
    lines[name] = line[line.find('->') + 3:].split(', ')
modules['button'].AddRcv(modules['broadcaster'])    
for name in lines:
    for r in lines[name]:
        trn = modules[name]
        rcv = modules[r]
        trn.AddRcv(rcv)
        if type(rcv) is Conjunction:
            rcv.AddTransmitter(trn)
            
for i in range(1000):
    modules['button'].Push()
    while len(pulses) > 0:
        pulse = pulses.pop(0)
        if pulse[2]:
            HighCnt += 1
        else:
            LowCnt += 1
        pulse[1].Process(pulse[0], pulse[2])

print(LowCnt * HighCnt)        
