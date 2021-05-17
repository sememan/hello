#!/bin/bash

REPO_DIR=/mnt/Volume/K2Systems/REPOSITORY/hello/
cd $REPO_DIR

pwd

git checkout master
git pull origin master

echo "--- Enter the branch you want to merge to master:"
read branch
git merge origin/"${branch}"

git push origin master

git remote remove origin
