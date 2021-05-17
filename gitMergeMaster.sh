#!/bin/bash

REPO_DIR=/mnt/Volume/K2Systems/REPOSITORY/hello/
cd $REPO_DIR

pwd


echo "--- Enter the branch:"
read branch

echo "merging..."
git checkout master
git merge origin/"${branch}"

echo "deleting..."
git push -d origin "${branch}"      # from remote
# echo "deleting locally..."
# git branch -d "${branch}"           # from local

echo "pushing..."
git push -u origin master

