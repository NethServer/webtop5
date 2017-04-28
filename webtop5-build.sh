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

for P in mvn javac; do
    which $P >/dev/null 2>&1 || { echo "Missing '$P' executable!"; exit 1; }
done

if [ ! -d sonicle-webtop5-gate ]; then
    echo "Downloading sonicle-webtop5-gate..."
    echo
    git clone https://github.com/sonicle/sonicle-webtop5-gate.git
fi

pushd sonicle-webtop5-gate

if [ ! -d sencha ]; then
     echo
    echo "Cloning all repositories..."
    echo
    gmake clone
fi

echo
echo "Checking for updates..."
echo
gmake update

echo
echo "Building..."
echo
gmake build

echo
echo "Createing war..."
echo
gmake deploy

echo
echo "Extracting sql scripts..."
tmpdir=$(mktemp -d)
mkdir $tmpdir/{data,schema}
find -path "*/resources/*" -name init-data\*.sql -type f  -exec cp -p '{}' $tmpdir/data \;
find -path "*/resources/*" -name \*.sql ! -name init-data\*.sql -type f -exec cp -p '{}' $tmpdir/schema \;
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

