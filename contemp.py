import pyopencl as cl, numpy as ny

ctx = cl.create_some_context()
fil = open('dna.seq')

if not fil:
	exit(1)
