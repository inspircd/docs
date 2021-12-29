build:
	mkdocs build

build-dev:
	mkdocs build --config-file mkdocs_dev.yml

clean:
	rm -rf site/

serve:
	mkdocs serve

serve-dev:
	mkdocs serve --config-file mkdocs_dev.yml
