#!/usr/bin/env bash
echo 'Folder Name: $1'
cd $1
mkdir -p models
mkdir -p views
mkdir -p routes
mkdir -p public/img
mkdir -p public/js
mkdir -p public/css