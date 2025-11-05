class Solution:
	def convert(self, s:str, numRows: int) -> str:
		diagonal = False

		answer_array = []
		for x in range(numRows):
			answer_array += [[None] * len(s)]

		index = [0,0]
		for letter in s:
			answer_array[index[0]][index[1]] = letter

			if index[0] == numRows-1 and diagonal == False:
				diagonal = True
			elif index[0] == 0 and diagonal == True:
				diagonal = False

			if diagonal == False:
				index[0] += 1
			else:
				index[0] -= 1
				index[1] += 1

		result  = ''
		for l in answer_array:
			for e in l:
				if e is not None:
					result += e

		return result

sol = Solution()
an1 = sol.convert("PAYPALISHIRING", 2)

print(an1)