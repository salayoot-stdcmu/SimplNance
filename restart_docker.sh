#!/bin/bash

# Restart Docker containers
docker-compose down -v
docker-compose up -d --build