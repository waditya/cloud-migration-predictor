.PHONY: setup train run clean

setup:
	python -m venv .venv
	source .venv/bin/activate && pip install -r requirements.txt

train:
	source .venv/bin/activate && python model/train_model.py

run:
	source .venv/bin/activate && python app/inference.py

clean:
	rm -rf .venv __pycache__ *.pkl