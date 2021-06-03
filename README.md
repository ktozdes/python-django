# docker-django-redis-celery
Initial configuration of Docker Django Redis Celery

## Getting Started
This project works on Python 3+ and Django 2+.
Simply, run the following command:
```
docker-compose up --build
```

useful docker commands

```
docker-compose run app python manage.py createsuperuser 	// creates superuser
docker-compose run app 	django-admin startapp polls 		// creates app named polls
docker-compose run app 	python manage.py makemigrations		// makes migration
docker-compose run app 	python manage.py migrate			// runs migration
						manage.py makemigrations --merge	//	
Docker exec -it  ### sh										// ssh into docker container						
```
## webpack related info

All frontend related js and css files are stored within scr folder

in order to compile them use following commands

```
npx webpack watch										// for dev
npx webpack build --config wepack.config.prod.js		// for production
```


