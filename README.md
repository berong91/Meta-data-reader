# Meta-data Reader
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/aaa830e2a8a148ce8a86200796335430/badge.svg)](https://www.quantifiedcode.com/app/project/aaa830e2a8a148ce8a86200796335430)
[![Build Status](https://travis-ci.org/berong91/Meta-data-reader.svg?branch=master)](https://travis-ci.org/berong91/Meta-data-reader)

## Description
Meta-data Reader is a django simple web-app that auto detects thread meta-data files and generates a view on a web. Data file must follow this JSON format, respectively.

````
[
  {
    "date": "Jan 1, 2015 13:10:59",
    "filename": "virus.exe",
    "action": "files-deleted",
    "submit-type": "FG300B3910602113/root",
    "rating": "high-risk"
  },
  {
    "date": "Jan 1, 2015 13:12:59",
    "filename": "helper.exe",
    "action": "files-added",
    "submit-type": "FG300B3910602113/root",
    "rating": "low-risk"
  }
]
````

The project is currently setup in two main branches. 
- `dev` - This is where the latest features are
- `master` The app is stable on this branch

# Installation

## Requirements (click each one for install guide)
- [Python 2.7.x](http://docs.python-guide.org/en/latest/starting/installation/)
- [pip](https://pip.pypa.io/en/stable/installing/)
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Easy installation
1. Clone the git: `git clone https://github.com/berong91/Meta-data-reader`
2. Go into the new directory: `cd Meta-data-reader`
3. Run `pip install --upgrade -r requirements.txt`, this will install the app and all library that is needed to run it
    
    Please choose to (w)ipe if you are asked for this:
    ````
    The plan is to install the git repository https://github.com/XXXXXXXXXXXXXXXXXXXXXXXXXX
    What to do?  (i)gnore, (w)ipe, (b)ackup
    ````
4. Run `python manage.py runserver`  
    After you are done following it this will start the app.
5. Open the app on browser `http://127.0.0.1:8000`
6. Copy new data to folder `Meta-data-reader\data\` for testing purpose. Enjoy.

# Features
- [x] Read and Validate AJAX file
- [x] Detect changes in data folder
- [x] Rendering data into HTML table
- [x] Populate data based on the record's threat level 
- [x] Auto reload data on web browser
- [x] Well looking Web UI
- [ ] Implement database versioning for UI update 
- [ ] Sort data output
- [ ] Update list of sources on the browser
- [ ] Update data folder from a concurrent thread or process
- [ ] Setup script

# Credits
- [Duy Pham](https://github.com/berong91) I did it again, oops
