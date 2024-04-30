## Lorsque le conteneur est créer via docker-compose        
        docker exec -it nom_du_conteneur_postgresql bash
        psql -U postgres
        GRANT ALL PRIVILEGES ON DATABASE nom_db TO user_db;