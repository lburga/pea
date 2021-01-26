@echo off
manage.py migrate
manage.py collectstatic
pip freeze>requirements.txt
git add .
git commit -m "Update"
git push origin main
git push heroku main
heroku run python manage.py migrate -a dt-data-pea
