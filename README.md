# Tema 2 SCD  
**BALAGIU DARIAN 341 C4**

## Microservicii:
- **API**: Flask  
- **Database**: PostgreSQL  
- **Utilitar gestiune baze de date**: Adminer  

## Organizare Network-uri
Microserviciile au fost împărțite în două network-uri: **backend** și **database**.  
- **API-ul** face parte din **backend**.  
- **Adminer** face parte din **database**.  

Baza de date (PostgreSQL) este **singurul microserviciu** care se leagă de ambele celelalte două microservicii, așadar ea este plasată în **ambele network-uri**.

## Persistența Bazei de Date
Persistența bazei de date este realizată prin intermediul **volumului** atașat în `docker-compose.yml`:  

# Database configuration
DB_HOST=db
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=weather

# Flask API configuration
FLASK_RUN_PORT=5001

