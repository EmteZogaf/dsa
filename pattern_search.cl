__kernel void pattern_search(__global const uchar *txt, __global uchar *res) {
	int offset = get_global_id(0) * :PATTERN_SIZE:;
	uint i = gid * 1024;
	
	
	if (gid < :SIZE:) {
:GET_CHAR_LINES:
	}
}
