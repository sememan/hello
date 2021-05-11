#!/bin/bash

#echo "Second arg: $2"
#echo "First arg: $1"

var1=blah
var2=foo
# Let's verify their current value
echo $0 :: var1 : $var1, var2 : $var2


REPO_DIR=/mnt/Volume/K2Systems/REPOSITORY/hello/
cd $REPO_DIR
pwd
echo "--- Enter your message"
read message
git add .
git commit -m "${message}"
if [ -n "$(git status - porcelain)" ];
then
 echo "IT IS CLEAN"
else
 git status
 echo "Pushing data to remote server!!!"
 echo "--- Enter your branch"
 read message
 git push -u origin master:message
fi
