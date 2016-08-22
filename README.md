# Meta-data Reader
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/aaa830e2a8a148ce8a86200796335430/snapshot/origin:dev:HEAD/badge.svg)](https://www.quantifiedcode.com/app/project/aaa830e2a8a148ce8a86200796335430?branch=origin%2Fdev)
[![Build Status](https://travis-ci.org/berong91/django-practice.svg?branch=dev)](https://travis-ci.org/berong91/django-practice) 

## Description
Meta-data Reader is a django simple web-app that auto detects thread meta-data files and generates a view on a web.

The project is currently setup in two main branches. 
- `dev` - This is where the latest features are
- `master` The app is stable on this branch

# Installation

## Requirements (click each one for install guide)
- [Python 2.7.x](http://docs.python-guide.org/en/latest/starting/installation/)
- [pip](https://pip.pypa.io/en/stable/installing/)
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Easy installation
1. Clone the git: `git clone https://github.com/berong91/django-practice`
2. Go into the new directory: `cd django-practice`
3. Run `pip install --upgrade -r requirements.txt`, this will install the app and all library that is needed to run it
    
    Please choose to (w)ipe if you are asked for this:
    ````
    The plan is to install the git repository https://github.com/XXXXXXXXXXXXXXXXXXXXXXXXXX
    What to do?  (i)gnore, (w)ipe, (b)ackup
    ````
4. Run `python manage.py runserver`  
    After you are done following it this will start the app.
5. Open the app on browser `http://127.0.0.1:8000`
6. Copy new data to folder `django-practice\data\` for testing purpose. Enjoy.

# Features
- [x] Read and Validate AJAX file
- [x] Detect changes in data folder
- [x] Rendering data into HTML table
- [x] Populate data based on the record's threat level 
- [x] Auto reload data on web browser
- [x] Well looking Web UI
- [ ] Trigger reloading from server-side
- [ ] Sort data from browser
- [ ] Auto script to reload the list of sources on homepage
- [ ] Setup script

# Credits
- [Duy Pham](https://github.com/berong91) I did it again, oops
