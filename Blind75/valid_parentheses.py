def valid_brackets(s):
	if len(s) % 2 != 0: return False
		
	brackets = {")":"(", "]": "[", "}":"{"}
	stack = []
	
	for char in s:
		if char not in brackets:
			stack.append(char)
			
	else:
		if stack == []:
			return False
		
		else:
			if stack[-1] == brackets[char]:
				stack.pop(-1)
			else:
				return False

	if stack == []: return True