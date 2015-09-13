import csv


def count_records(csv_file):
	count = 0
	reader = csv.reader(csv_file)
	for row in reader:
		if "SINGLE MALT SCOTCH" in map(lambda val: val.upper(), row):
			 count += 1
	return count

if __name__ == "__main__":
	file_path = "iowa-liquor-sample.csv"
	with open(file_path) as csv_file:
		malt_liquor_count = count_records(csv_file)
		print(malt_liquor_count)
