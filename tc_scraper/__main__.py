from .topcoder_scraper import analysis
import argparse 
import sys
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("contest_name", help = "Contest name to analyse", type = str)
	parser.add_argument("-o", "--output", help = "Output result to txt file", action = "store_true")
	parser.add_argument("-l", "--problemlinks", help = "Prints the links to problems", action = "store_true")
	args = parser.parse_args()

	if args.problemlinks:
		st = 1
	else:
		st = 0
	if args.output:
		original_stdout = sys.stdout
		with open('analysis.txt', 'w') as f:
			sys.stdout = f
			analysis(args.contest_name, st)
			sys.stdout = original_stdout
	else:
		analysis(args.contest_name, st)


if __name__ == "__main__":
	main()