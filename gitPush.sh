#!/bin/bash

REPO_DIR=/mnt/Volume/K2Systems/REPOSITORY/hello/
cd $REPO_DIR
pwd
echo "--- Enter your message"
read message
git add .
git commit -m "${message}"
git status
# echo "--- Pushing data to remote server!!!"
echo "--- Enter the branch:"
read branch
git push -u origin "${branch}"
