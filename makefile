rundev:
	python manage.py runserver --settings=blog.config.settings.dev

runprod:
	python manage.py runserver --settings=blog.config.settings.prod