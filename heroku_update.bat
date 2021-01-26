@echo off
manage.py migrate
manage.py collectstatic
pip freeze>requirements.txt
git add .
git commit -m "Update"
git push origin master
git push heroku master
heroku run python manage.py migrate -a dt-data-pea
