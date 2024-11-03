# Shopper Flask API
A [Flask](https://flask.palletsprojects.com/en/stable/) API backend built to support the [shopper](https://github.com/zeta-squared/shopper) React application.

## Installation
This API was developed with Python 3.12.3. To avoid any version errors ensure yours is also on this release or above by using `python3 --version`. If you are comfortable working on an older version you can go ahead and see all requirements, and their version, in `./requirements.txt`.

Once you have ensured your Python install is ready to use, create a virtual environment within the project directory, `./`, by running
```
python3 -m venv venv
```
Always ensure you are working with the virtual environment. We can now install all the dependencies using `pip`. You will need to make sure you have `pip` install using `python3 -m pip --version`. If you don't have `pip` installed you can find more information [here](https://pip.pypa.io/en/stable/installation/') on how to install.

Now we are ready to install and run the API. Activate the virtual environment by running `source venv/bin/activate`. Once inside the virtual environment run `python3 -m pip install -r requirements.txt` to install all dependencies.
>[!IMPORTANT]
>Make sure you are in the virtual environment. Otherwise the `pip` command will install the dependencies to your user account rather than just the virtual environment.

Once all the dependencies are installed you need to configure the envionrment variables. Create the file `./config/.env`. The following configuration variables need to be set
```
ACCESS_TOKEN_DURATION=15
REFRESH_TOKEN_DURATION=7

APIFAIRY_TITLE=Shopper API
APIFAIRY_VERSION=1.0
APIFAIRY_UI=elements

SQLALCHEMY_DATABASE_URI=sqlite:///shopper.db

SECRET_KEY='my secret key'
```
These are just default/dummy values I have included here. You are welcome to choose what you please.
>[!CAUTION]
>If you ever deploy this application make sure the `SECRET_KEY` is set to something secure. This can be done with the [UUID](https://docs.python.org/3/library/uuid.html) Python module or another method of your preference.

Finally, create the file `./.flaskenv` and set
```
FLASK_APP=shopper.py
```

I have included all the database migration files (generated with
[Flask-Migrate](https://flask-migrate.readthedocs.io)) in `./migrations/`. To initialise the database run
`flask db upgrade`. This will create the `sqlite` database `./instance/shopper.db`.

Now use `flask run` to start the application. It will run, by default, on `localhost:5000`. You can optionally, change the port by using the `FLASK_RUN_PORT=<port>` variable in `./.flaskenv`. Documentation can be found at `localhost:<port>/`.

### Acknowledgements
The API uses several Python/Flask packages. I have listed as many as I can remember here but for a complete list see `./requirements.txt`
- [APIFairy](https://apifairy.readthedocs.io)
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest)
- [flask-HTTPAuth](https://flask-httpauth.readthedocs.io)
- [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io)
- [Flask-Migrate](https://flask-migrate.readthedocs.io)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.readthedocs.io)
- [Marshmallow](https://marshmallow.readthedocs.io)
- [PyJWT](https://pyjwt.readthedocs.io/en/latest)
- [SQLAlchemy](https://www.sqlalchemy.org)
- [Werkzeug](https://werkzeug.palletsprojects.com)

Apologies if I have left someones' work out.
