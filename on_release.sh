
python manage.py makemigrations users
python manage.py migrate
gunicorn chq_backend.wsgi --log-file -