.PHONY: start stop logs build rebuild restart ps \
        bash-back bash-front \
        migrate makemigrations downgrade \
        bootstrap flush-db test

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

# Очистить данные в бд
flush-db:
	rm -f backend/data/app.db
	mkdir -p backend/data
	touch backend/data/app.db

# Тесты

test:
	docker compose exec backend python -m pytest tests/ -v

# Работа со сторонним апи

bootstrap:
	docker compose exec backend python -m app.core.cli