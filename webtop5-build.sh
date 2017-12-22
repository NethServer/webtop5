#!/bin/bash
#
# Copyright (C) 2017 Nethesis S.r.l.
# http://www.nethesis.it - nethserver@nethesis.it
#
# This script is part of NethServer.
#
# NethServer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License,
# or any later version.
#
# NethServer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NethServer.  If not, see COPYING.
#
#
#  This script will download and build webtop5,
#  at the end a war named webtop-webapp-5.war will
#  be available inside th current directory

set -e 

function exit_error
{
    echo "ERROR: please create a VERSION file containing the WebTop 5 git tag"
    echo
    echo "  Example: echo 'wt-5.1.4' > VERSION"
    echo
    exit 1
}

for P in mvn javac; do
    which $P >/dev/null 2>&1 || { echo "Missing '$P' executable!"; exit 1; }
done

if [ ! -f VERSION ]; then
   exit_error
fi

tag_name=$(cat VERSION)

if [ -z $tag_name ]; then
    exit_error
fi

if [ ! -d sonicle-webtop5-gate ]; then
    echo "Downloading sonicle-webtop5-gate..."
    echo
    git clone https://github.com/sonicle/sonicle-webtop5-gate.git
fi

pushd sonicle-webtop5-gate
git pull

echo
echo "Cleanup local copy... "
rm -rf sencha components

echo
echo "Cloning all repositories..."
echo
gmake clone


if [ -n $tag_name ]; then
    pushd components

    for d in $(find . -maxdepth 1  -type d)
    do
	repo_path="$d/.git"
	repo_name=$(basename $d)
        if [ -d $repo_path ]; then
           if git --git-dir=$repo_path tag | grep -q $tag_name ; then
	       echo "Checking out tag '$tag_name' for '$repo_name'"
               git --git-dir=$repo_path checkout tags/$tag_name
	   else
	       echo "Checking out 'master' for '$repo_name'"
           fi
	fi
    done

    popd
fi

echo
echo "Building..."
echo
gmake build

echo
echo "Creating war..."
echo
gmake deploy

echo
echo "Extracting sql scripts..."
tmpdir=$(mktemp -d)
mkdir $tmpdir/{data,schema}
find -path "*/resources/*" -name init-data\*.sql -type f  -exec cp -p '{}' $tmpdir/data \;
find -path "*/resources/*" -name init-\*.sql ! -name init-data\*.sql -type f -exec cp -p '{}' $tmpdir/schema \;
# Remove invalid lines starting with @ used inside WebTop
find $tmpdir/schema -name init-\*.sql | xargs sed -i '/^@/d'
tar cvzf sql-scripts.tar.gz -C $tmpdir .
echo "sql-scripts.tar.gz successfully created"
echo

popd

echo
echo "Copying files..."
echo
cp -v sonicle-webtop5-gate/components/webtop-webapp/target/webtop-webapp-5.war .
cp -v sonicle-webtop5-gate/sql-scripts.tar.gz .
echo
echo "webtop-webapp-5.war and sql-scripts.tar.gz successfully created"
echo

