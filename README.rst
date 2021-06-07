
Install and Run
---------------

*(Optional)* Create a virtual environment and activate it with::

    $ python3 -m venv .venv && source .venv/bin/activate

Install dependencies with::

    $ pip install --upgrade pip wheel
    $ pip install -r requirements.txt
    $ pip install -r requirements-dev.txt       # For DEV environments

Create the database with::

    $ python3 manage.py makemigrations
    $ python3 manage.py makemigrations mtasks
    $ python3 manage.py makemigrations partner
    $ python3 manage.py migrate

To create an admin user::

    $ python3 manage.py createsuperuser

Then run in development mode with::

    $ python3 manage.py runserver

Or use the script to startup in the same mode::

    $ ./run.sh dev

Some settings can be overwritten with environment variables.
For example to overwrite the language translations of the application and
set *debug* options to false::

    $ DEBUG=False LANGUAGE_CODE=es-ar python3 manage.py runserver

Available settings to override are:

* ``DEBUG``: set the Django ``DEBUG`` option. Default ``True``.
* ``TIME_ZONE``: default ``UTC``. Other example: ``America/Buenos_Aires``.
* ``LANGUAGE_CODE``: default ``en-us``. Other example: ``es-ar``.
* ``SITE_HEADER``: Header title of the app. Default to *"Django Coleman - A Simple Task Manager"*.
* ``DATABASE_URL``: Database string connection. Default uses SQLite database. Other
  example: ``postgresql://elan:postgres@localhost/elan_dev``.
* More settings like email notifications, check the ``settings.py`` file
  for more details, any variable that is set with ``os.getenv(...`` is able
  to be configured using environment variables.

To run in a production environment, check the `<README-production.rst>`_ notes, or
see the official Django documentation.

