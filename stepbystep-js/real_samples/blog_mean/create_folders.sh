#!/usr/bin/env bash

PROJECT_NAME=$1
echo $PROJECT_NAME
mkdir -p $PROJECT_NAME/css/
mkdir -p $PROJECT_NAME/js/
mkdir -p $PROJECT_NAME/assert/
touch -p $PROJECT_NAME/index.html

echo 'create folders successfully'

