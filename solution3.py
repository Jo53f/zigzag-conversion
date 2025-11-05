class Solution():
	def convert(self, s: str, numRows: int) -> str:
		if numRows < 2 or numRows > len(s):
			return s

		ans_array = [''] * numRows
		column = 0
		step = 1
		for letter in s:
			ans_array[column] += letter

			if column == 0:
				step = 1
			elif column == numRows - 1:
				step = -1

			column += step
		return "".join(ans_array)


sol = Solution()
print(sol.convert("PAYPALISHIRING", 2))