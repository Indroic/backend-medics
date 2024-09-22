python -m pip install -r requirements.txt

echo "si esta ejecutando esto"

python manage.py collectstatic --no-input

python manage.py makemigrations

python manage.py migrate
