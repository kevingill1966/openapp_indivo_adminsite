Indivo Django Admin Site
========================

.. highlights::

    THIS IS A DEVELOPERS TOOL. DO NOT USE IT IN AN ENVIRONMENT WITH LIVE MEDICAL DATA.
    THIS TOOL BY-PASSES THE INDIVO SECURITY

Indivo does not have a Django Admin Site. This tool is very useful for developers.
I have implemented an AdminSite.

The Site is of interest for comprehending how the Record is connected. Start with
a Record and work your way around.

For further information on Indivo, visit::

    http://indivohealth.org/

Screenshot
----------

.. image:: https://raw.github.com/kevingill1966/openapp_indivo_adminsite/master/docs/images/screenshot1.png

Installation
------------

Make sure you are in the correct virtualenv environment::

    . python/bin/activate  (or similar)

If you are running Django 1.4, we recommend using admin_enhancer ::

    pip install django-admin-enhancer

Install the package::

    pip install openapp_indivo_adminsite

You need to create a separate settings file, for the admin site, in the indivo_server
directory. This settings file is intended only to run the admin site. Call this 
file settings_admin.py. Include the following code.

.. code::


    # This configuration is for the Indivo admin site - it uses the standard
    # settings, but replaces a middleware to allow the Django Authentication
    # system to work.

    import os.path
    from settings import *


    # The admin site requires the Django Static Files logic.
    STATIC_ROOT = ''
    STATIC_URL = '/static/'
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    # Need to load the templates from an egg.
    TEMPLATE_LOADERS += (
         'django.template.loaders.eggs.Loader',
    )

    # THIS REPLACES THE INDIVO MIDDLEWARE TO PERMIT DJANGO AUTHENTICATION
    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    )

    # ENABLE THE ADMIN URLS
    ROOT_URLCONF = 'openapp_indivo.adminsite.urls'

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.admin',
        'django.contrib.admindocs',
        'indivo',
        'codingsystems',
        'south',
        'openapp_indivo.adminsite',
    )

    # Admin urls are picky about the trailing slash
    APPEND_SLASH = True


    # If admin enhancer is available, use it (requires django 1.4)
    try:
        import admin_enhancer
        INSTALLED_APPS += 'admin_enhancer',
    except:
        pass

    import openapp_indivo.adminsite
    ADMINSITE_ROOT_DIR = os.path.dirname(openapp_indivo.adminsite.__file__)
    TEMPLATE_DIRS = (ADMINSITE_ROOT_DIR + '/templates/',) + TEMPLATE_DIRS


Sync your database to create tables required to support admin.::

    python manage.py syncdb --settings=settings_admin
    python manage.py migrate --settings=settings_admin

Create a superuser. You login as superuser to create other users.::

    python manage.py createsuperuser --settings=settings_admin

Now start your server. This will run the admin web server on port 10000.
If you want to make the admin url visible outside of the current server,
either use 0.0.0.0 instead of localhost, or proxy this server via apache or similar.::

    python manage.py runserver localhost:10000 --settings=settings_admin

You can access this url from your browser using:

    http://localhost:10000/admin/

Short-comings
-------------

After upload of a document, display the status and provide a hyperlink to go to the
document. Allow user to provide more fields.

On the document view, provide links to facts contained in the document only.

For all foreign keys, need autocomplete logic. Otherwise the system cannot
function with any volume of data.

All changelists require search configuration for dealing with volumes of data.

Support for Django 1.3.X. Currently index.html is coded to support 1.4 only.

Integration of the Document Revision History and the Django Revision History.

Integration of the Audit Trail and the Django Revision History.

Licence
-------

This code is distributed under GPLv3. This is for consistency with Indivo, which
is also distributed under that licence.

    http://www.gnu.org/licenses/gpl-3.0-standalone.html

