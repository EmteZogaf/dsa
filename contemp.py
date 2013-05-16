import pyopencl as cl, numpy as ny, os

ctx = cl.create_some_context()
filename = 'dna.seq'
f = open(filename)
fSize = os.path.getsize(filename)

for i in range(fSize):
	c = f.read(1)

