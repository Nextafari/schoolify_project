web: gunicorn my_login_page.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate