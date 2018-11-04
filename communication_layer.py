class ApplicationLayer:
	def __init__(self,data):
		self.data = data
	def printdata(self):
		print(self.data,end='')
		
class PresentationLayer:
	def __init__(self,applayer):
		self.data = "h1"
		self.applayer = applayer
	def printdata(self):
		print(self.data,end='')
		self.applayer.printdata()

class SessionLayer:
	def __init__(self,presentationlayer):
		self.data = "h2"
		self.presentationlayer = presentationlayer
	def printdata(self):
		print(self.data,end='')
		self.presentationlayer.printdata()
		
class TransportLayer:
	def __init__(self,sessionlayer):
		self.data = "h3"
		self.sessionlayer = sessionlayer
	def printdata(self):
		print(self.data,end='')
		self.sessionlayer.printdata()

class NetworkLayer:
	def __init__(self,transportlayer):
		self.data = "h4"
		self.transportlayer = transportlayer
	def printdata(self):
		print(self.data,end='')
		self.transportlayer.printdata()
class DatalinkLayer:
	def __init__(self,networklayer):
		self.data = "h5"
		self.networklayer = networklayer
	def printdata(self):
		print(self.data,end='')
		self.networklayer.printdata()
class PhysicalLayer:
	def __init__(self,datalinklayer):
		self.data = "h6"
		self.datalinklayer = datalinklayer
	def printdata(self):
		print(self.data,end='')
		self.datalinklayer.printdata()

message = input("Enter the message: ")
a = ApplicationLayer(message)
b = PresentationLayer(a)
c = SessionLayer(b)
d = TransportLayer(c)
e = NetworkLayer(d)
f = DatalinkLayer(e)
g = PhysicalLayer(f)


#Transmission
print("TRANSMITTER\n")

print("\nAPPLICATION LAYER: ",end="")
a.printdata()
print("\nPRESENTATION LAYER: ",end="")
b.printdata()
print("\nSESSION LAYER: ",end="")
c.printdata()
print("\nTRANSPORT LAYER: ",end="")
d.printdata()
print("\nNETWORK LAYER: ",end="")
e.printdata()
print("\nDATALINK LAYER: ",end="")
f.printdata()
print("\n\nMESSAGE ENTERED INTO PHYSICAL LAYER AND TRANSMITTED.")
#RECEIVER:

print("RECEIVER\n")
print("\nDATALINK LAYER: ",end="")
f.printdata()
print("\nNETWORK LAYER: ",end="")
f.networklayer.printdata()
print("\nTRANSPORT LAYER: ",end="")
f.networklayer.transportlayer.printdata()
print("\nSESSION LAYER: ",end="")
f.networklayer.transportlayer.sessionlayer.printdata()
print("\nPRESENTATION LAYER: ",end="")
f.networklayer.transportlayer.sessionlayer.presentationlayer.printdata()
print("\nAPPLICATION LAYER: ",end="")
f.networklayer.transportlayer.sessionlayer.presentationlayer.applayer.printdata()
print("\n\n")
