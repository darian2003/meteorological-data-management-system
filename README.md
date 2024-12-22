# Meteorological Data Management System

This project is a comprehensive RESTful API application designed for managing, storing, and querying meteorological data. The application enables efficient handling of geographic information, such as countries and cities, as well as temperature records associated with those locations. Built with Flask for the backend, PostgreSQL for data persistence, and Adminer for database visualization, it offers a scalable and maintainable architecture suitable for real-world scenarios.

## Features

### REST API
- Implements a robust RESTful API for data management and retrieval.
- Provides endpoints for managing:
  - **Countries**: Add, update, retrieve, and delete country records with geographic details such as latitude and longitude.
  - **Cities**: Manage cities, link them to their respective countries, and query city-specific data.
  - **Temperatures**: Record temperatures for cities and retrieve them based on time intervals, geographic coordinates, or city/country identifiers.

### Data Persistence
- Relational data is managed using **PostgreSQL**, ensuring data integrity and scalability.
- Database schema includes:
  - **Countries**: Stores country names and geographic details.
  - **Cities**: Linked to countries, stores city-specific data.
  - **Temperatures**: Records temperature values, timestamps, and links them to cities.
- Automatic timestamp generation for temperature records on creation.
- Ensures data consistency with constraints such as unique fields.

### Database Visualization
- **Adminer**, an intuitive and lightweight database management tool, is included for seamless interaction with the database. Users can easily view, update, and manage database records via a user-friendly web interface.

### Containerization with Docker
- Fully containerized architecture using **Docker** for isolated and reproducible environments.
- Docker Compose orchestrates the setup of:
  - A Flask-based API container.
  - A PostgreSQL database container for persistent storage.
  - An Adminer container for database visualization.
- Environment variables, network segmentation, and volumes ensure secure and optimized container communication and data persistence.

### JSON Integration
- All API interactions are conducted via JSON payloads, making the application lightweight and compatible with modern web and mobile clients.
- Supports flexible query options for temperatures based on latitude, longitude, and date ranges.

## API Endpoints

### Countries
- **POST /api/countries**: Add a new country.
- **GET /api/countries**: Retrieve all countries.
- **PUT /api/countries/:id**: Update a country by ID.
- **DELETE /api/countries/:id**: Delete a country by ID.

### Cities
- **POST /api/cities**: Add a new city linked to a country.
- **GET /api/cities**: Retrieve all cities.
- **GET /api/cities/country/:id**: Retrieve all cities in a specific country.
- **PUT /api/cities/:id**: Update a city by ID.
- **DELETE /api/cities/:id**: Delete a city by ID.

### Temperatures
- **POST /api/temperatures**: Add a temperature record for a city.
- **GET /api/temperatures**: Retrieve temperature records filtered by latitude, longitude, and/or date range.
- **GET /api/temperatures/cities/:id**: Retrieve temperatures for a specific city, optionally filtered by date range.
- **GET /api/temperatures/countries/:id**: Retrieve temperatures for all cities in a country, optionally filtered by date range.
- **PUT /api/temperatures/:id**: Update a temperature record by ID.
- **DELETE /api/temperatures/:id**: Delete a temperature record by ID.

## Technology Stack

- **Backend Framework**: Flask (Python)
- **Database**: PostgreSQL
- **Visualization Tool**: Adminer
- **Containerization**: Docker and Docker Compose
- **Data Format**: JSON for all API communication

## How It Works
1. **Data Entry**: Users can add geographic data (countries and cities) and their associated temperature records.
2. **Querying Data**: The API allows querying temperature records based on flexible parameters like geolocation or time intervals.
3. **Database Management**: Adminer provides an interactive web interface for viewing and modifying data directly in the PostgreSQL database.
4. **Scalable Deployment**: The containerized architecture ensures the application runs consistently across different environments, with easy setup using Docker Compose.

## Installation and Usage
1. Clone the repository and navigate to the project directory.
2. Build and start the containers using `docker-compose up --build`.
3. Access the API at `http://localhost:<API_PORT>` and Adminer at `http://localhost:<ADMINER_PORT>`.

This project showcases a scalable and modular approach to managing meteorological data, providing a solid foundation for further enhancements, such as integrating advanced analytics or real-time data updates. It is ideal for applications requiring precise and structured geographic and temporal data management.
