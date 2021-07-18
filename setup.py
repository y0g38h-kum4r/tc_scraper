from setuptools import setup

def readme():
      with open('README.md') as f:
            return f.read()
            
setup(name='tc_scraper',
      version='0.1',
      description='Software Project',
      long_description = readme(),
      long_description_content_type='text/markdown', 
      
      classifiers=[ 'License :: OSI Approved :: MIT License', 
      'Programming Language :: Python :: 3', 
      'Operating System :: OS Independent' ],
      
      url='https://github.com/y0g38h-kum4r/tc_scraper',
      author='y0g38h-kum4r',
      author_email='yogeshkumar.m200010@gmail.com',
      keywords = 'Software',
      packages = ['tc_scraper'],
      install_requires = [],
      include_package_data = True,
      zip_safe=False)