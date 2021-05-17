#!/bin/bash

REPO_DIR=/mnt/Volume/K2Systems/REPOSITORY/hello/
cd $REPO_DIR

pwd

git checkout master
git pull origin master

echo "--- Enter the branch you want to merge to master:"
read branch

echo "--- merging..."
git merge origin/"${branch}"

echo "--- pushing..."
git push origin master

echo "--- deleting..."
git push -d origin "${branch}"      # from remote
git branch -d "${branch}"           # from local