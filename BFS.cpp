/*

One directional BFS & two directional BFS

*/

// 127. Word Ladder
// Ref: https://www.youtube.com/watch?v=vWPCm69MSfs
// Note: 
// 1. upper & two triangles in the video
// 2. swap set

// One Directional pseudo code 
q.push(start)
step = 0

while not q.empty():
	++step;
	size = q.size();
	whiile size-- > 0:
		node = q.pop()
		new_nodes = expand(node)
		if goad in new_nodes: return step + 1
		q.append(new_nodes)

return NOT_FOUND

// Two Directional pseudo code
s1.insert(start)
s2.insert(end)
step = 0

while not ( s1.empty() || s2.empty() ):
	++step
	swap*(s1, s2)
	s = {}

	for node in s1:
		new_nodes = expand(node)
		if any(new_nodes) in s2: return step + 1
		s.append(new_nodes)
	s1 = s

return NOT_FOUND


/*


*/


