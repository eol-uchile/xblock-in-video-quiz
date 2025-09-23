.DEFAULT_GOAL := help
.PHONY: requirements

# include *.mk

# Generates a help message. Borrowed from https://github.com/pydanny/cookiecutter-djangopackage.
help: ## Display this help message
	@echo "Please use \`make <target>' where <target> is one of"
	@perl -nle'print $& if m{^[\.a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m %-25s\033[0m %s\n", $$1, $$2}'

lang_targets = en es_419
_extract_translations:
	pybabel extract -F invideoquiz/translations/babel.cfg -o invideoquiz/translations/django.pot --msgid-bugs-address=eol-ing@uchile.cl --copyright-holder='Oficina EOL' --project=xblock-in-video-quiz --version=1.0.0 --last-translator='Oficina EOL <eol-ing@uchile.cl>' *
	pybabel extract -F invideoquiz/translations/babel-js.cfg -o invideoquiz/translations/django-js.pot --msgid-bugs-address=eol-ing@uchile.cl --copyright-holder='Oficina EOL' --project=xblock-in-video-quiz --version=1.0.0 --last-translator='Oficina EOL <eol-ing@uchile.cl>' *

create_translations_catalogs: _extract_translations ## Create the initial configuration of .po files for translation
	for lang in $(lang_targets) ; do \
		pybabel init -i invideoquiz/translations/django.pot -D django -d invideoquiz/translations/ -l $$lang ; \
		pybabel init -i invideoquiz/translations/django-js.pot -D djangojs -d invideoquiz/translations/ -l $$lang ; \
	done

update_translations: _extract_translations ## update strings to be translated
	pybabel update -N -D django -i invideoquiz/translations/django.pot -d invideoquiz/translations/
	pybabel update -N -D djangojs -i invideoquiz/translations/django-js.pot -d invideoquiz/translations/
	rm invideoquiz/translations/django.pot
	rm invideoquiz/translations/django-js.pot

compile_translations: ## compile .po files into .mo files
	pybabel compile -f -D django -d invideoquiz/translations/; \
	pybabel compile -f -D djangojs -d invideoquiz/translations/
