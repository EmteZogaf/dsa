__kernel void count(__global const uchar *txt, __global uchar *res) {
	uint gid = get_global_id(0) *1024;
	uchar cur[:PATTER_SIZE:];a
	
	if (gid  < :SIZE:) {
		uint size = :SIZE: - gid * 1024 < 1024 ? :SIZE: - gid * 1024 : 1024;
		for (int i=0; i<:SIZE:; 
:CHAR_GET_LINES:
	}
}
