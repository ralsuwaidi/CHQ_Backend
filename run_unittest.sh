docker-compose run --rm backend ./wait-for-it.sh db:5432
docker-compose run --rm backend python manage.py makemigrations users
docker-compose run --rm backend python manage.py migrate
docker-compose run --rm backend python manage.py jenkins