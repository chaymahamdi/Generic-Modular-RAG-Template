FROM liquibase/liquibase:5.0.0

USER root

RUN addgroup --system appgroup && \
    adduser --system --ingroup appgroup appuser


RUN mkdir -p /liquibase/lib && \
    curl -L -o /liquibase/lib/postgresql.jar \
    https://jdbc.postgresql.org/download/postgresql-42.7.8.jar

COPY liquibase/changelog/ /liquibase/
COPY liquibase/liquibase.properties /liquibase/

RUN chown -R appuser:appgroup /liquibase

USER appuser

CMD ["sh", "-c", "liquibase update --url=jdbc:postgresql://${VECTOR_DB_HOST}:${VECTOR_DB_PORT}/${VECTOR_DB_NAME} --username=${VECTOR_DB_USER} --password=${VECTOR_DB_PASSWORD} --defaultsFile=liquibase.properties"]
