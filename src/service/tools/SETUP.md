pip install django
pip install djangorestframework
pip install -r requirements.txt

## Migrate DB
python3 manage.py makemigrations
python3 manage.py migrate
## Install objects from fixtures
python3 manage.py loaddata items/fixtures/items_data.json
pip install flake8 isort
pip install python-dotenv

python3 manage.py runserver