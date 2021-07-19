# tc_scraper

Python script to analyse Competitive Programming matches from site https://www.topcoder.com/ using BeautifulSoup4. Features available: Problem Ratings (feature not availabe in topcoder), Links to problems, Problemwise analysis!!

## How to install
## beta version(Problem ratings are calculated as avg of PerfAs Ratings of coders, high execution time)
### Open a new terminal
1. Create a new enlistment for the project:
```console
foo@bar:~$ git clone https://github.com/y0g38h-kum4r/tc_scraper
foo@bar:~$ cd tc_scraper
```

2. Create a new virtual environment
```console
foo@bar:~$ python -m venv env
foo@bar:~$ source env/bin/activate
```

3. Upgrade pip installer
```console
foo@bar:~$ python -m pip install --upgrade pip
```

4.Install the project
```console
foo@bar:~$ pip setup.py install
foo@bar:~$ pip install -e .
```

5. Example 
```console
foo@bar:~$ tc_scraper -h
foo@bar:~$usage: tc_scraper [-h] [-o] [-l] contest_name

positional arguments:
  contest_name        contest name to be analysed
  div                 division to be analysed

optional arguments:
  -h, --help          show this help message and exit
  -o, --output        output result to txt file
  -l, --problemlinks  prints the links to problems
```

## stable version(Problem Ratings are calculated as average of Final Ratings of coders, minimal execution time)
https://pypi.org/project/tc-scraper/ 