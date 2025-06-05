#!/bin/bash
# Quick Start Script for MLB Predictor

echo "🚀 Starting MLB Predictor Setup..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    echo "❌ pip is not installed. Please install pip first."
    exit 1
fi

echo "✅ Python and pip found"

# Install requirements
echo "📦 Installing requirements..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Requirements installed successfully"
else
    echo "❌ Failed to install requirements"
    exit 1
fi

# Run the application
echo "🏃 Starting MLB Predictor..."
echo "🌐 Your app will open at: http://localhost:8501"
echo "🔗 Press Ctrl+C to stop the application"

streamlit run mlb_predictor_app.py
