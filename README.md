# MM Product

This is an example product that uses a "core wagtail" layer

The core wagtail layer is hosted on github at (mikemonteith/mm-core)[https://github.com/mikemonteith/mm-core]

## Aims

The aim is to make development with this product as close to a regular wagtail site as possible,
while providing defaults and some restrictions on what can be configured.

`pip install -r requirements.txt` to install your dependencies.

`python manage.py` to run site setup commands.

Core platform components can be imported with `from mm_core import foo, bar, baz`

## Getting started

1. Create a virtual environment `virtualenv venv`
2. Activate your virtual environment `. ./venv/bin/activate`
3. Install dependencies `pip install -r requirements.txt`
4. Run migrations `python manage.py migrate`
5. Create a superuser `python manage.py createsuperuser`
6. Start your server `python manage.py runserver 0.0.0.0:8000`

## Settings

In the same way that django settings are defined with a `DJANGO_SETTINGS_MODULE` environment
variable, the core platform expects an `APP_SETTINGS` variable with a path to your
settings file so that the core layer installs your product.
The `APP_SETTINGS` variable is set to `mm_product.settings` by default in the manage.py file.

## Developing on top of this product

You can create new page models in `mm_product/models.py`

Remember to create new migration files `python manage.py makemigrations` and run
them `python manage.py migrate`.

## Docker

A docker image can be created based on mm_core.
Make sure you've built the mm_core docker image with tag=mm-core:latest if you want to
build the mm-product docker image.
