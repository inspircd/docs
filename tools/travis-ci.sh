#!/bin/sh
set -euv
sudo apt-get update
if [ "$TRAVIS_PULL_REQUEST" = "false" ]
then
	sudo apt-get install python3-pip --assume-yes --install-recommends
	pip3 install markdown-include mkdocs mkdocs-cinder mkdocs-exclude mkdocs-redirects
	git config --global user.name "InspIRCd Robot"
	git config --global user.email "noreply@inspircd.org"
	mkdocs gh-deploy --force --message 'Update website for docs commit {sha}.' --remote-branch gh-pages --remote-name https://${GITHUB_TOKEN}@github.com/inspircd/inspircd-docs.git
else
	sudo apt-get install ruby --assume-yes --install-recommends
	./tools/find-missing
	./tools/find-orphans
	./tools/find-whitespace
fi
