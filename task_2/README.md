# Развертывание PostgreSQL и pgAdmin (GUI)

### 1. Делаем pull образов:

```bash
docker pull dpage/pgadmin4:latest
docker pull postgres:latest
```

### 2. Из директории, содержащей `docker-compose.yml` выполняем:

```bash
docker-compose up -d
```

> `-d` — запуск в фоновом режиме.

### 3. Теперь pgAdmin доступен по адресу:

[http://localhost:8080](http://localhost:8080)

Залогинеться в pgAdmin можно используя данные, указанные в переменных окружения
