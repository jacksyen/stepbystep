#!/usr/bin/env bash

PROJECT_NAME=$1
echo $PROJECT_NAME
mkdir -p $PROJECT_NAME/models/
mkdir -p $PROJECT_NAME/controllers/
mkdir -p $PROJECT_NAME/config/
mkdir -p $PROJECT_NAME/routers/
touch $PROJECT_NAME/app.js

echo 'create folders successfully'

