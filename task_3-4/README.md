# Развертывание pgAdmin и PostgreSQL в Kubernetes

1. Для развертывания PostgreSQL выполните следующие команды:

```bash
kubectl apply -f config.yml
kubectl apply -f secret.yml
kubectl apply -f service.yml
kubectl apply -f statefulset.yml
```

2. Для развертывания PgAdmin выполните следующие команды:

```bash
kubectl apply -f config.yml
kubectl apply -f secret.yml
kubectl apply -f service.yml
kubectl apply -f deployment.yml
```

3. В файле `etc/hosts` добавьте следующую строку:
```text
127.0.0.1 pgadmin.local
```

4. Для настройки доступа к PgAdmin:

```bash
kubectl apply -f ingress.yml
```
PgAdmin будет доступен по адресу [http://pgadmin.local](http://pgadmin.local)

5. Для добавления базы данных в PgAdmin выполните следующие шаги:

   - Перейдите в **Object -> Register -> Server... -> Connection**.
   - В поле **Host name** укажите IP-адрес Minikube (получить его можно с помощью команды `minikube ip`).
   - В поле **Port** укажите `31000`.
   - В поле **Username** укажите `lena`.
   - В поле **Password** укажите `1234`.
