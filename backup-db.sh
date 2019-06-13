#!/bin/bash

DATE=$(date +"%Y%m%d%H%M")

cd /home/ubuntu/backups/postgres_backups

pg_dump -h localhost -U ubuntu -F t godakhtar > godakhtar_${DATE}.tar

gzip godakhtar_${DATE}.tar

# Cleanup configuration backups older than 30 days.

find /home/ubuntu/backups/postgres_backups -name "godakhtar*.gz" -mtime +30 -type f -delete
