.PHONY: create_venv upgrade_libs format analytics clean

create_venv:
	@uv venv

upgrade_libs:
	@uv sync --upgrade

format:
	@ruff format

analytics: ## Start analytics
	msgfmt -o app/analytics/locales/en/LC_MESSAGES/messages.mo app/analytics/locales/en/LC_MESSAGES/messages && \
	msgfmt -o app/analytics/locales/pt/LC_MESSAGES/messages.mo app/analytics/locales/pt/LC_MESSAGES/messages && \
	streamlit run app/analytics/main.py
	
clean: ## Clean venv and generated folders
	rm -rf .venv target

