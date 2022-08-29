web: gunicorn coolsite.wsgi --log-file -
release: python manage.py migrate && python manage.py collectstatic -yes
