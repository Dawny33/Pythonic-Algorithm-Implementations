class LogicGate:

	def __init__(self,n):
		self.label = n
		self.output = None

	def getLabel(self):
		return self.label

	def getOutput(self):
		self.output = self.performGateLogic()
		return self.output


#As both the Binary and Unary gates are sub-classes of Logic Gate, we call the
#Constructor instance of the super class.

class BinaryGate(LogicGate):

	def __init__(self,n):
		LogicGate.__init__(self,n)

		self.pinA = None
		self.pinB = None

	def getPinA(self):
		return int(input("Enter Pin A " + self.getLabel() + ":"))

	def getPinB(self):
		return int(input("Enter Pin B " + self.getLabel() + ":"))


class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getLabel()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

	def __init__(self,n):
		BinaryGate.__init__(self,n)

	def performGateLogic(self):
		a = self.getPinA()
		b = self.getPinB()

		if a==1 and b==1:
			return 1
		else:
			return 0

class ORGate(BinaryGate):

	def __init__(self,n):
		BinaryGate.__init__(self,n)

	def performGateLogic(self):
		a = self.getPinA()
		b = self.getPinB()

		if a==1 or b==1:
			return 1
		else:
			return 0

class NOTGate(UnaryGate):

	def __init__(self,n):
		UnaryGate.__init__(self,n)

	def performGateLogic(self):
		a = self.getPin()

		if a == 1:
			return 0
		else:
			return 1


#g1 = AndGate("G1")
#g2 = ORGate("G2")
g3 = NOTGate("G3")
#print(g1.getOutput())
#print(g2.getOutput())
print(g3.getOutput())