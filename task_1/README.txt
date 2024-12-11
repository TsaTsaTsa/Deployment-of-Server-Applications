# Задание 1

## 1. Docker image собран при помощи Dockerfile и запушен в Docker Hub

1. Собираем Docker image:

   ```bash
   docker build -t server-app .
   ```

2. Входим в Docker Hub:

   ```bash
   docker login
   ```

3. Тегируем образ:

   ```bash
   docker tag <image-id> helenossy/server-app:v1
   ```

4. Запушиваем образ в Docker Hub:

   ```bash
   docker push helenossy/server-app:v1
   ```

5. Ссылка на Docker Hub:  
   [https://hub.docker.com/repository/docker/helenossy/server-app/general](https://hub.docker.com/repository/docker/helenossy/server-app/general)

## 2. При помощи docker-compose развернут контейнер

В каталоге с `docker-compose.yml` выполняем команду:

```bash
docker-compose up
```