.PHONY: setup train run clean

# Location of the virtual environment activation script
ACTIVATE = source .venv/bin/activate

# Create virtual environment and install dependencies
setup:
	@echo "🔧 Creating virtual environment and installing dependencies..."
	python3 -m venv .venv
	$(ACTIVATE) && pip install --upgrade pip && pip install -r requirements.txt

# Train the ML model
train:
	@echo "🚀 Training the model..."
	$(ACTIVATE) && python model/train_model.py

# Run the Flask inference API
run:
	@echo "🌐 Starting the Flask API..."
	$(ACTIVATE) && python app/inference.py

# Clean up environment and model artifacts
clean:
	@echo "🧹 Cleaning up..."
	rm -rf .venv
	rm -rf __pycache__
	rm -f model/xgboost_model.pkl
