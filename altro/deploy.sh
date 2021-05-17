#!/usr/bin/env bash

# Set script to exit on errors.
set -e

# Get script's absolute location.
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Change to repo root.
cd ${DIR};
cd ..

# Git pull.
git status
git pull

# Run Gulp.
gulp sass