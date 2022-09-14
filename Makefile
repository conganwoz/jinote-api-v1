up:
	docker-compose up

down:
	docker-compose down

build:
	docker-compose build

bash:
	docker-compose run web sh

install:
	sudo docker-compose run web pip install __name__ && pip freeze > requirements.txt && docker-compose build