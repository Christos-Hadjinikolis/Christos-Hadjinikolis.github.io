SHELL := /bin/bash

RUBY_MIN_VERSION := 3.1.0
BUNDLE_APP_CONFIG := .bundle
BUNDLE_PATH := vendor/bundle
BUNDLE_CMD := BUNDLE_APP_CONFIG=$(BUNDLE_APP_CONFIG) bundle
JEKYLL_CMD := $(BUNDLE_CMD) exec jekyll
HOST ?= 127.0.0.1
PORT ?= 4000

.DEFAULT_GOAL := help

.PHONY: help check install serve build audit clean doctor social-x social-linkedin linkedin-auth-url linkedin-exchange-token linkedin-whoami install-hooks remove-hooks

help:
	@echo "Available targets:"
	@echo "  make install  - install gems into $(BUNDLE_PATH)"
	@echo "  make serve    - run the site locally with live reload"
	@echo "  make build    - build the site into _site/"
	@echo "  make audit    - build the site and list top-level generated files"
	@echo "  make clean    - remove generated build and cache files"
	@echo "  make doctor   - print Ruby, Bundler, and Jekyll versions"
	@echo "  make install-hooks - install local git hooks into .git/hooks"
	@echo "  make remove-hooks  - remove hooks installed by this repo"
	@echo "  make social-x ARGS='--text \"...\"'          - publish a post to X"
	@echo "  make social-linkedin ARGS='--text \"...\"'   - publish a post to LinkedIn"
	@echo "  make linkedin-auth-url                       - print the LinkedIn OAuth URL"
	@echo "  make linkedin-exchange-token ARGS='--code ... --write-env' - exchange a LinkedIn auth code for a token"
	@echo "  make linkedin-whoami ARGS='--write-env'      - resolve and store the LinkedIn author URN"

check:
	@command -v ruby >/dev/null || { echo "Ruby is not installed or not on PATH."; exit 1; }
	@command -v bundle >/dev/null || { echo "Bundler is not installed or not on PATH."; exit 1; }
	@ruby -e 'required = Gem::Version.new("$(RUBY_MIN_VERSION)"); current = Gem::Version.new(RUBY_VERSION); abort("Ruby #{required} or newer is required; found #{RUBY_VERSION}") if current < required'

install: check
	@$(BUNDLE_CMD) config set --local path "$(BUNDLE_PATH)"
	@$(BUNDLE_CMD) check || $(BUNDLE_CMD) install

serve: install
	@$(JEKYLL_CMD) serve --livereload --host $(HOST) --port $(PORT)

build: install
	@rm -rf _site
	@JEKYLL_ENV=production $(JEKYLL_CMD) build

audit: build
	@for forbidden in _site/scripts _site/cv _site/wip; do \
		if [ -e "$$forbidden" ]; then \
			echo "Unexpected published internal path: $$forbidden"; \
			exit 1; \
		fi; \
	done
	@if find _site -type f \( -name 'README.html' -o -name 'README.md' -o -path '*/README/index.html' \) | grep -q .; then \
		echo "Unexpected published README artifact found in _site"; \
		find _site -type f \( -name 'README.html' -o -name 'README.md' -o -path '*/README/index.html' \) | sort; \
		exit 1; \
	fi
	@find _site -mindepth 1 -maxdepth 1 | sort

clean:
	@rm -rf _site .sass-cache .jekyll-cache .jekyll-metadata

doctor:
	@ruby -v
	@bundle -v
	@$(BUNDLE_CMD) check >/dev/null 2>&1 || { echo "Project gems are not installed. Run 'make install' first."; exit 1; }
	@$(JEKYLL_CMD) -v

social-x:
	@python3 scripts/social/post_x.py $(ARGS)

social-linkedin:
	@python3 scripts/social/post_linkedin.py $(ARGS)

linkedin-auth-url:
	@python3 scripts/social/linkedin_oauth.py auth-url

linkedin-exchange-token:
	@python3 scripts/social/linkedin_oauth.py exchange-code $(ARGS)

linkedin-whoami:
	@python3 scripts/social/linkedin_oauth.py whoami $(ARGS)

install-hooks:
	@bash scripts/local_setup/setup-hooks.sh install

remove-hooks:
	@bash scripts/local_setup/setup-hooks.sh remove
