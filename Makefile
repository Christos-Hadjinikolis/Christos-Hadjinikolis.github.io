# Use @ to silence the output, or remove it to see the commands being run

# This target sets up the local environment by checking for dependencies
# and installing them if they are not present
# First we define the shell we're using
SHELL := /bin/bash

# Define paths to the user bin and ensure we're using the right version
USER_BIN_PATH := $(HOME)/.gem/bin
RBENV_BIN_PATH := $(HOME)/.rbenv/bin
RBENV_COMMAND := eval "$$(rbenv init - bash)"

# Use this to set up the local environment
setup-local-env:
	@echo "Setting up the local Ruby and Jekyll environment..."
	@if ! which brew &>/dev/null; then echo "Homebrew not found. Please install it."; exit 1; fi
	@if ! which rbenv &>/dev/null; then brew install rbenv; fi
	@if ! which ruby-build &>/dev/null; then brew install ruby-build; fi

	# Initialize rbenv in the current shell session
	@export PATH="$(RBENV_BIN_PATH):$$PATH" && eval "$$(rbenv init -)"

	# Install the Ruby version specified in the .ruby-version file if it's not already installed
	@rbenv install --skip-existing `cat .ruby-version`

	# Set the local (directory-specific) Ruby version
	@rbenv local `cat .ruby-version`

	# Make sure the shims are properly set
	@rbenv rehash

	# Install Jekyll and Bundler, ensuring we're using the user's gem bin directory
	@export PATH="$(USER_BIN_PATH):$$PATH" && gem install jekyll bundler --user-install

	# Rehash after installing gems to ensure binaries are available
	@rbenv rehash

# This target serves your Jekyll site locally
serve-site:
	@echo "Serving your Jekyll site locally..."
	@export PATH="$(USER_BIN_PATH):$(RBENV_BIN_PATH):$$PATH" && eval "$$(rbenv init -)"
	@rbenv rehash
	@gem list -i bundler || gem install bundler
	@bundle check || bundle install
	@gem list -i http_parser.rb -v 0.6.0 || gem install http_parser.rb -v 0.6.0
	@gem cleanup
	@bundle exec jekyll serve --livereload

# Use this to open the site in your default browser
open-site:
	@echo "Opening the local Jekyll site in your default browser..."
	@open http://localhost:4000
