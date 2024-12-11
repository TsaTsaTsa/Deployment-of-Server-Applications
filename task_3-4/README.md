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
