#!/bin/bash
# Start Docker containers
docker-compose up -d --build frontend
docker-compose up -d --build backend