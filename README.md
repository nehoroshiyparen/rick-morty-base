# Rick & Morty Base

Fullstack-приложение для просмотра и управления данными вселенной Rick and Morty. Данные импортируются из [The Rick and Morty API](https://rickandmortyapi.com/) и хранятся в локальной базе данных. Через интерфейс можно просматривать персонажей, эпизоды и локации, переходить между связанными сущностями и редактировать имена записей прямо на странице.

---

## Используемый API

**The Rick and Morty API** — открытый REST API с данными по вселенной сериала.
Документация: [https://rickandmortyapi.com/documentation](https://rickandmortyapi.com/documentation)

Использованные ресурсы:

| Ресурс | Эндпоинт |
|---|---|
| Персонажи | `GET /api/character?page={n}` |
| Эпизоды | `GET /api/episode?page={n}` |
| Локации | `GET /api/location?page={n}` |

Данные загружаются постранично до тех пор, пока не закончатся страницы (404 = конец). При получении 429 (rate limit) импорт делает паузу в 5 секунд и продолжает.

---

## Что реализовано

### Бэкенд

- **Импорт данных из внешнего API** — CLI-команда запускает полный импорт всех персонажей, эпизодов и локаций. Данные сохраняются через upsert (обновляются если уже существуют).
- **Синхронизация связей** — после импорта персонажей автоматически связываются с локациями, после импорта эпизодов — с персонажами через таблицу many-to-many.
- **REST API** — CRUD-эндпоинты для всех трёх сущностей (список, деталь, обновление, удаление).
- **Унифицированный формат ответа** — все ответы оборачиваются в `ApiSuccess { success, data }` или `ApiFail { success, error, status }`.
- **Тесты** — покрытие основных эндпоинтов через pytest + pytest-asyncio с in-memory SQLite базой.

### Фронтенд

- **Лента персонажей / эпизодов / локаций** с бесконечной прокруткой (IntersectionObserver).
- **Детальные страницы** для каждой сущности — все связи кликабельны (персонаж → его эпизоды, эпизод → участвующие персонажи, локация → жители).
- **Inline-редактирование имени** — на каждой детальной странице есть кнопка-карандаш, переводящая заголовок в режим редактирования прямо в UI. Изменения сохраняются через PATCH-запрос. Поддержка Enter / Escape.
- **ImageWithRetry** — компонент изображения с экспоненциальным переповтором при ошибке загрузки.
- **Runtime-валидация** ответов через Zod-схемы на каждый тип данных.

---

## Стек технологий

### Бэкенд

| | |
|---|---|
| Язык | Python 3.13 |
| Фреймворк | FastAPI 0.135 |
| ORM | SQLAlchemy 2.0 (async) |
| База данных | SQLite (aiosqlite) |
| Миграции | Alembic |
| Валидация | Pydantic v2 |
| HTTP-клиент | httpx |
| CLI | Typer |
| Тесты | pytest + pytest-asyncio |
| Сервер | Uvicorn |

### Фронтенд

| | |
|---|---|
| Язык | TypeScript |
| Фреймворк | React 19 |
| Сборщик | Vite 8 |
| Роутинг | React Router v7 |
| Стили | Tailwind CSS v4 |
| HTTP | Axios |
| Валидация | Zod v4 |

---

## Архитектура

### Бэкенд

```
app/
├── core/               # Конфигурация, роуты, CLI, обработчики ошибок
├── infrastructure/
│   ├── database/       # Engine, Session, BaseRepository, BaseModel
│   ├── integrations/   # HTTP-клиент Rick&Morty, маперы, схемы внешнего API
│   └── lib/            # ApiSuccess / ApiFail, логгер
├── modules/
│   ├── character/      # Model, Repository, Service, Router, Schemas
│   ├── episode/        # Model, Repository, Service, Router, Schemas
│   └── location/       # Model, Repository, Service, Router, Schemas
└── workflows/
    ├── base/           # BaseWorkflow, BaseImportWorkflow, BaseSyncWorkflow
    └── rick_morty/
        ├── uploading/  # CharacterImport, EpisodeImport, LocationImport, Orchestrator
        └── sync/       # SyncLocationChar, SyncCharEpisode
```

Импорт реализован через **Workflow/Orchestrator** паттерн:

1. `BaseImportWorkflow` — постраничный обход внешнего API, маппинг, upsert в БД, накопление `self.mapped`
2. `BaseSyncWorkflow` — получает уже загруженные данные, строит связи между сущностями в БД
3. `BaseWorkflowOrchestrator` — открывает сессию и запускает воркфлоу в нужном порядке: сначала локации → затем персонажи (с синхронизацией location↔character) → затем эпизоды (с синхронизацией character↔episode)

Репозитории используют паттерн `bind(session)` — один инстанс репозитория переиспользуется, сессия передаётся при каждом вызове.

### Фронтенд

```
src/
├── app/          # Роутер, layout, конфигурация роутов
├── entities/     # Данные по доменам (characters / episodes / locations)
│   └── {entity}/
│       ├── api/      # getList, getOne, update, delete
│       ├── hooks/    # useCharacters / useEpisodes / useLocations
│       ├── types/    # Zod-схемы + TypeScript-типы
│       └── ui/       # Карточки сущностей
├── features/     # ImageWithRetry, InfiniteScroll
├── pages/        # CharactersPage, CharacterPage, EpisodesPage, EpisodePage...
├── shared/
│   └── api/      # Axios-инстанс, request() wrapper, ApiResponse типы
└── widgets/      # Header, Feed-компоненты
```

Каждый `request()` автоматически разворачивает обёртку `ApiSuccess.data`, валидирует через переданную Zod-схему и возвращает дискриминированный union `{ success: true, data } | { success: false, error }`.

---

## Запуск

### Требования

- Docker + Docker Compose
- Make (опционально, но удобно)

### Шаг 1 — Запустить контейнеры

```bash
make start
# или
docker compose up -d
```

После запуска доступно:
- Фронтенд: [http://localhost:5173](http://localhost:5173)
- Бэкенд API: [http://localhost:7812](http://localhost:7812)
- Swagger UI: [http://localhost:7812/docs](http://localhost:7812/docs)

### Шаг 2 — Применить миграции

```bash
make migrate
# или
docker compose exec backend alembic upgrade head
```

### Шаг 3 — Импортировать данные из Rick and Morty API

```bash
make bootstrap
# или
docker compose exec backend python -m app.core.cli import-all
```

Импорт загружает все страницы персонажей, эпизодов и локаций (~800 персонажей, ~51 эпизод, ~126 локаций) и строит связи между ними. Занимает около 1–2 минут.

После этого приложение полностью готово к работе — откройте [http://localhost:5173](http://localhost:5173).

---

## Полный список make-команд

| Команда | Описание |
|---|---|
| `make start` | Запустить контейнеры |
| `make stop` | Остановить контейнеры |
| `make build` | Собрать образы |
| `make rebuild` | Полная пересборка с очисткой volumes |
| `make restart` | Перезапустить |
| `make logs` | Логи всех сервисов |
| `make logs-back` | Логи бэкенда |
| `make logs-front` | Логи фронтенда |
| `make ps` | Статус контейнеров |
| `make migrate` | Применить миграции |
| `make makemigrations msg="..."` | Создать новую миграцию |
| `make downgrade` | Откатить на 1 миграцию |
| `make bootstrap` | Импорт всех данных из Rick&Morty API |
| `make import-characters` | Импорт только персонажей |
| `make import-episodes` | Импорт только эпизодов |
| `make import-locations` | Импорт только локаций |
| `make flush-db` | Очистить базу данных |
| `make test` | Запустить тесты |

---

## API Reference

Все ответы имеют формат:

```json
{ "success": true, "data": { ... } }
{ "success": false, "error": "Not found", "status": 404 }
```

### Characters

| Метод | Путь | Описание |
|---|---|---|
| `GET` | `/characters?limit=20&offset=0` | Список персонажей |
| `GET` | `/characters/{id}` | Персонаж с эпизодами и локацией |
| `PATCH` | `/characters/{id}` | Обновить имя: `{ "name": "..." }` |
| `DELETE` | `/characters/{id}` | Удалить персонажа |

### Episodes

| Метод | Путь | Описание |
|---|---|---|
| `GET` | `/episodes?limit=20&offset=0` | Список эпизодов |
| `GET` | `/episodes/{id}` | Эпизод с персонажами |
| `PATCH` | `/episodes/{id}` | Обновить имя: `{ "name": "..." }` |
| `DELETE` | `/episodes/{id}` | Удалить эпизод |

### Locations

| Метод | Путь | Описание |
|---|---|---|
| `GET` | `/locations?limit=20&offset=0` | Список локаций |
| `GET` | `/locations/{id}` | Локация с жителями |
| `PATCH` | `/locations/{id}` | Обновить имя: `{ "name": "..." }` |
| `DELETE` | `/locations/{id}` | Удалить локацию |