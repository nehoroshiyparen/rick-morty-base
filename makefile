.PHONY: up down logs build rebuild restart ps \
        bash-back bash-front \
        migrate makemigrations downgrade

# 🚀 Запуск
start:
	docker compose up -d

# 🛑 Остановка
stop:
	docker compose down

# 🔨 Сборка
build:
	docker compose build

# 💣 Полная пересборка
rebuild:
	docker compose down -v
	docker compose up -d --build

# 🔄 Рестарт
restart:
	docker compose down
	docker compose up -d

# 📜 Логи
logs:
	docker compose logs -f

logs-back:
	docker compose logs -f backend

logs-front:
	docker compose logs -f frontend

# 📊 Контейнеры
ps:
	docker compose ps

# 🐚 Войти в контейнеры
bash-back:
	docker compose exec backend bash

bash-front:
	docker compose exec frontend sh

# 🗄️ Миграции

# применить миграции
migrate:
	docker compose exec backend alembic upgrade head

# создать миграцию (нужно передать msg)
makemigrations:
	docker compose exec backend alembic revision --autogenerate -m "$(msg)"

# откат на 1 шаг

downgrade:
	docker compose exec backend alembic downgrade -1


import-all:
	docker compose exec backend python -m app.core.cli import-all


import-characters:
	docker compose exec backend python -m app.core.cli import-data characters


import-episodes:
	docker compose exec backend python -m app.core.cli import-data episode


import-locations:
	docker compose exec backend python -m app.core.cli import-data location

bootstrap:
	docker compose exec backend python -m app.core.cli import-all