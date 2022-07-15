.PHONY: run

run:
	cd superclean; uvicorn presentation.api:app
