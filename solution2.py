class Solution:
	def convert(self, s: str, numRows: int) -> str:
		if numRows == 1 or numRows >= len(s):
			return s

		diagonal = True
		ans_array = [''] * numRows

		column = 0
		for letter in s:
			ans_array[column] += letter

			if 0 == column or column == numRows - 1:
				diagonal = not diagonal

			column -= 1 if diagonal else -1

		return "".join(ans_array)

sol = Solution()
print(sol.convert("PAYPALISHIRING", 2))