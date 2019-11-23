# Find polindrome dates (MMDDYYYY) in centry (1000 - 9999)

class PolindromeDateGenerator:

	def __init__(self, start, end):

		self.minYear = start
		self.maxYear = end

	def setYearRange(self, start, end):
		self.minYear = start
		self.maxYear = end

	def find(self):
		res =[]
		for year in range(self.minYear, self.maxYear+1):
			yearStr = str(year)
			monthStr, dateStr = yearStr[-2:][::-1], yearStr[0:2][::-1]
			if self._checkDate(dateStr, monthStr, yearStr):
				res.append(monthStr + dateStr + yearStr)

		return res

	# check if given string month 'MM' is valid
	def _checkMonth(self, month):
		if int(month) in range(1, 13):
			return  True
		else:
			return False
			# raise ValueError('Month can only between 1 to 12')

	# check if given string date 'DD' is valid given corresponding string month 'MM'
	def _checkDate(self, date, belongMonth, belongYear):
		dateInt = int(date)
		monthInt = int(belongMonth)
		yearInt = int(belongYear)

		if not self._checkMonth(belongMonth):
			return False
			# raise ValueError('Month can only between 1 to 12')

		# Leap year February check
		if yearInt % 1000  == 0:
			if yearInt % 400 == 0:
				febMax = 29
			else:
				febMax = 28
		elif yearInt % 4 == 0:
			febMax = 29
		else:
			febMax = 28

		# month date corresponding check
		if monthInt in [1, 3, 5, 7, 8, 10, 12]:
			if dateInt in range(1, 32):
				return True
			else:
				return False
				# raise ValueError('Date in month {} should in 1-31'.format(monthInt))

		elif monthInt in [4, 6, 9, 11]:
			if dateInt in range(0, 30+1):
				return True
			else:
				return False
				# raise ValueError('Data in month {} should in 1-30'.format(monthInt))

		else: # February
			if dateInt in range(0, febMax+1):
				return True
			else:
				return False
				# raise ValueError('Data in month {} should in 1-{}'.format(monthInt, febMax))


if __name__ == "__main__":

	finder = PolindromeDateGenerator(2010, 2019)
	finder.setYearRange(1000, 9999)
	res = finder.find()

	for date in res:
		print(date)
		print()














