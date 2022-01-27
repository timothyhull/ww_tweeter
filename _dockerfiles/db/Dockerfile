# Dockerfile for PostgreSQL database
FROM postgres:14.1-bullseye

# Expose the PostgreSQL DB port
EXPOSE 5432/TCP

# Set the working directory
# WORKDIR /db

# Update OS packages
RUN apt-get update && \
    apt-get upgrade -y

# Start the bash prompt
# CMD ["postgres -D $PGDATA"]
# ENTRYPOINT ["pg_ctl -D /var/lib/postgresql/data -l logfile start"]
