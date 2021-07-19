from .topcoder_scraper import analysis
import argparse 
import sys
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("contest_name", help = "contest name to be analysed", type = str)
	parser.add_argument("div", help = "division to be analysed", type = int)
	parser.add_argument("-o", "--output", help = "output result to txt file", action = "store_true")
	parser.add_argument("-l", "--problemlinks", help = "prints the links to problems", action = "store_true")

	args = parser.parse_args()

	if args.problemlinks:
		st = 1
	else:
		st = 0
	
	if args.output:
		original_stdout = sys.stdout
		with open('analysis.txt', 'w') as f:
			sys.stdout = f
			analysis(args.contest_name, st, args.div)
			sys.stdout = original_stdout
	else:
		analysis(args.contest_name, st, args.div)


if __name__ == "__main__":
	main()