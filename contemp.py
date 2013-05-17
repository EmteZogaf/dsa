# coding: utf8
import pyopencl as cl, numpy as np, os, time

class ListCounter(dict):
	def __missing__(self, key):
		self[key] = []
		return self[key]

fn = 'dna.seq'
f = open(fn)
f_size = os.path.getsize(fn)
counts = ListCounter()
pattern_size_min = 2
pattern_size_max = 2
start = time.time()

for i in range(pattern_size_min, pattern_size_max + 1):
	f.seek(0)
	a = f.read(i)
	counts[a].append(0)

	for j in range(1, f_size - i + 1):
		a = a[1:] + f.read(1)
		counts[a].append(j)
end = time.time()
print(len(counts))
print('Elapsed time: {0}µs.'.format(int((end-start)*10**6)))
