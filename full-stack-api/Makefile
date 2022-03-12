build:
	docker-compose -f docker-compose.yaml up token-tracker-app token-tracker-db --build

up:
	docker-compose -f docker-compose.yaml up token-tracker-app token-tracker-db

down:
	docker-compose -f docker-compose.yaml down

clean:
	docker-compose -f docker-compose.yaml down -v

up-db:
	docker-compose -f docker-compose.yaml up token-tracker-db -d

up-test-db:
	docker-compose -f docker-compose.yaml up token-tracker-testing-db -d