#!/bin/bash

REPO_DIR=/mnt/Volume/K2Systems/REPOSITORY/hello/
cd $REPO_DIR

pwd


echo "Enter the branch you want to merge to master:"
read branch

echo "merging..."
git checkout master
git merge origin/"${branch}"

echo "deleting the remote branch..."
git push -d origin "${branch}"      # from remote
# echo "deleting locally..."
# git branch -d "${branch}"           # from local


# echo "--- Enter the push commit message"
# read message

# echo "pushing..."
# git add .
# git commit -m "${message}"
# git status
# git push -u origin master

