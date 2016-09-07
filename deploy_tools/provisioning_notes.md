Provisioning a new site
=======================

## Required packages:

    * nginx
    * Python 3
    * Git
    * pip
    * virtualenv

    eg, on Ubuntu:
        sudo apt-get install nginx git python3 python3-pip
        sudo pip3 install virtualenv


## Nginx Virtual Host config

    * see nginx.template.conf
    * replace SITENAME with, eg, staging.my-domain.com

    * copy config: sed "s/SITENAME/<your_site>/g" \
	deploy_tools/nginx.template.conf | sudo tee \
	/etc/nginx/sites-available/<your site>
    * activate: sudo ln -s ../sites-available/<your site> \
	/etc/nginx/sites-enabled/<your site>

## Systemd Job (this is now used on Ubuntu by default)
    * see gunicorn-systemd.template.service 
    * replace SITENAME with, eg, staging.my-domain.com

    * copy config: sed "s/SITENAME/<your site>/g" \
	deploy_tools/gunicorn-systemd.template.service | sudo tee \
	/lib/systemd/system/gunicorn-<your site>.service
    * sudo service nginx reload
    * sudo start gunicorn-<your site>

## Upstart Job (deprecated)

    * see gunicorn-upstart.template.conf
    * replace SITENAME with, eg, staging.my-domain.com


## Folder structure:

    Assume we have a user account at /home/username
    /home/username
    └── sites
        └── SITENAME
            ├── database
            ├── source
            ├── static
            └── virtualenv


## SETUP 

### On the server: 
Change settings.py (for security reasons):
 * DEBUG = False
 * ALLOWED_HOSTS = ['SITENAME']

 * Install required software, see requirements.txt
   - ../virtualenv/bin/pip install gunicorn
   - ../virtualenv/bin/pip install django


# Setup nginx server: 
 * make config (see above)
 * echo $SITENAME - set to your sitename
 * sudo ln -s /etc/nginx/sites-available/$SITENAME /etc/nginx/sites-enabled/$SITENAME
 * sudo service nginx start (or reload if running already)

# Setup gunicorn server:
 * copy config to /lib/systemd/system/gunicorn-SITENAME.service
 * sudo systemctl enable /lib/systemd/system/gunicorn-SITENAME.service
 * sudo service gunicorn-SITENAME start

# Test run webserver by hand: 
    * ../virtualenv/bin/python3 manage.py runserver


### On the local machine: 

# Setup:
 * Install virtualenv and requried packages: 
 * Update requirements.txt: pip freeze > requirements.txt

# Test functional tests on local server:
   * python manage.py test functional_tests --liveserver=$SITENAME

