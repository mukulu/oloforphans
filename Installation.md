#OLOFORPHANS INSTALLATION
#Oloforphans is django-cms powered, requires all requirements for django-cms installed.
#[Dependencies]

	- Django 1.2
	- Django-cms
	- Django-page-cms (optional, ships with Django-cms)
	- Python 2.6 or higher
	- Django-south (optional)

#[Installation]
##Make sure you have python 2.4 or higher installed.

###1. Download and install tarball Django 1.2 or higher from [Django website](http://www.djangoproject.com/download/1.2.1/tarball/) 
	$ tar xvzf Django-version.tar.gz
	$ cd Django-version
	$ sudo python setup.py install
   You can check if django installed by launching python interpreter
	$ python
	>>> import django
  	>>>
   It should return nothing(silent from errors) if django is installed.

###2. Download and install tarball of the latest release of [Django CMS from their website](http://www.django-cms.org/en/downloads/)
	$ tar xvzf django-cms-version.tar.gz
	$ cd django-cms-version
	$ sudo python setup.py install
   You can check if django-cms is installed by launching python interpreter
	$ python
	>>> import cms
	>>>
   It should return nothing(silent from errors) if django-cms is installed.
   Django-cms ships with mptt and publisher which are its dependencies, you can check them if they are installed too.
	>>> import mptt
	>>> import publisher
    
###3. Optional, for maintanance of website, django-south can be used in migrating database to new upgraded system
   You can install it with mercurial checkout, install mercurial in your system to check it out. or you can use easy_install.
   For full Installation instructions visit their [website.](http://south.aeracode.org/docs/installation.html)
   To check if django-cms is installed try importing it from python interpreter
    $ python
    >>> import south

###4. After you have installed the requirements, you can proceed with further django deployment of the website.
