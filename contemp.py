# coding: utf8
import pyopencl as cl, numpy as np, os, time
from functools import reduce

class ListCounter(dict):
	def __missing__(self, key):
		self[key] = []
		return self[key]

def get_device():
	devs = []
	for pf in cl.get_platforms():
		for dev in pf.get_devices():
			devs.append(dev)

	if len(devs) == 0:
		sys.exit(1)
	
	devs = sorted(devs, key = lambda dev: repr(dev.get_info(di.TYPE))
			+ repr(dev.get_info(di.LOCAL_MEM_TYPE) % 2) 
			+ repr(dev.get_info(di.MAX_COMPUTE_UNITS))
			+ repr(dev.get_info(di.LOCAL_MEM_SIZE)), reverse=True)
	return devs[0]

def count_vars_ocl(f, f_size, pattern_size_min, pattern_size_max):
	di = cl.device_info
	mf = cl.mem_flags
	dt = np.dtype('u1')
	fArr = np.fromfile(f, dt, f_size)
	charGetTpl = open('char_get.cl.tpl').readline()
	countTpl = open('pattern_count.cl').read
	
	dev = get_device()
	ctx = cl.Context(devices=[dev])
	fBuf = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf = fArr)
	
	for i in range(pattern_size_min, pattern_size_max + 1):
		charGetLines = ''
		for j in range(f_size):
			charGetLines += charGetTpl
		resArr = np.zeros([, ])

	return counts

def count_vars(f, f_size, pattern_size_min, pattern_size_max):
	counts = ListCounter()
	for i in range(pattern_size_min, pattern_size_max + 1):
		f.seek(0)
		a = f.read(i)
		counts[a].append(0)
	
		for j in range(1, f_size - i + 1):
			a = a[1:] + f.read(1)
			counts[a].append(j)
	return counts

if __name__ == '__main__':
	fn = 'dna.seq'
	f = open(fn)
	f_size = 10000#os.path.getsize(fn)
	pattern_size_min = 50
	pattern_size_max = 50
	variations = reduce(lambda x,y: x + 4**y, [0] + list(range(pattern_size_min, pattern_size_max + 1)))
	start = time.time()
	counts = count_vars(f, f_size, pattern_size_min, pattern_size_max)
	end = time.time()
	#for k in sorted(counts.keys(), key = lambda key: repr(len(key)) + key):
	#	print(k + ':' + repr(len(counts[k])))
	print('Variations: ' + repr(len(counts)) + ' out of ' + repr(variations))
	print('Elapsed time: {0}µs.'.format(int((end-start)*10**6)))
