FROM openjdk:21-jdk

WORKDIR /app
COPY target/server-1.0-SNAPSHOT.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "app.jar"]
