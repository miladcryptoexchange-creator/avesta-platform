.PHONY: install start test build deploy

install:
	cd backend && pip install -r requirements.txt
	cd frontend && npm install
	cd admin-panel && npm install

start:
	docker-compose up -d

stop:
	docker-compose down

test:
	cd backend && pytest

build:
	cd frontend && npm run build
	cd admin-panel && npm run build

deploy:
	docker-compose -f docker-compose.prod.yml up -d

logs:
	docker-compose logs -f

backup:
	docker-compose exec db pg_dump -U postgres avesta > backup.sql

migrate:
	cd backend && alembic upgrade head
