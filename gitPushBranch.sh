#!/bin/bash

REPO_DIR=/mnt/Volume/K2Systems/REPOSITORY/hello/
cd $REPO_DIR

pwd

echo "--- Enter the commit message"
read message

git add .
git commit -m "${message}"
git status

echo "--- Enter the branch you want to push to:"
read branch
git push -u origin master:"${branch}"
