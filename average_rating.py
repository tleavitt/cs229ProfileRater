import csv, sys

csvname = "Ratings_of_all_raters.csv"

ratings = np.zeros(500)
counts = np.zeros(500)
with open(csvname, 'rU') as csvfile:
	data = csv.reader(csvfile, dialect=csv.excel_tab, delimiter=',')
	i = 0
	for row in data:
		pic_num = int(row[1].strip())
		ratings[pic_num] += int(row[2].strip())
		counts[pic_num] += 1

print np.divide(ratings, counts)