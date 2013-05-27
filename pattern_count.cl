__kernel void count(__global const uchar *txt, __global uchar *res) {
	int gid = get_global_id(0);
	uchar cur[:PATTER_SIZE:];
	
	if (gid < :SIZE:) {
:CHAR_GET_LINES:
	}
}
