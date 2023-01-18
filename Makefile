install:
	sudo -u postgres psql -c "CREATE USER gustavoronconi WITH PASSWORD 'kanastra'"
	sudo -u postgres psql -c "CREATE DATABASE challenge_kanastra"
	sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE "challenge_kanastra" to gustavoronconi"
	sudo -u postgres psql -c "ALTER USER gustavoronconi CREATEDB"
	echo "from django.contrib.auth.models import User; User.objects.create_superuser('gustavoronconi', 'gustavoronconi95@gmail.com.br', 'kanastra')" | python payments-api/manage.py shell