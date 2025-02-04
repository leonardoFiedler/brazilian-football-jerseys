.PHONY: create_venv upgrade_libs gen_data format clean

create_venv:
	@uv venv .venv

upgrade_libs:
	@uv sync --upgrade

format:
	@ruff format

gen_data:
	@rm -rf data/processed/brazil-teams-jersey-price-processed.csv data/processed/minimum_wage_historical.csv
	@echo "Generating minimum wage historical data..."
	@python app/minimum_wage/minimum_wage.py
	@echo "Generating Processed data..."
	@python app/data/add_columns_raw_data.py

clean: ## Clean venv and generated folders
	rm -rf .venv target

