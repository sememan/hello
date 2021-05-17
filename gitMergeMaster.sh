#!/bin/bash

REPO_DIR=/mnt/Volume/K2Systems/REPOSITORY/hello/
cd $REPO_DIR

pwd

git checkout master
git pull origin master

echo "--- Enter the branch:"
read branch
git merge "${branch}"

git push origin master
