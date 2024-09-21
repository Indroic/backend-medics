pip install -r requerements.txt

python manage.py collectstatic --no-input

python manage.py makemigrations

python manage.py migrate

python manage.py seed