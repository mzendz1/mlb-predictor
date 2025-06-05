# Let me create the required files step by step to avoid indentation issues

# 1. Create requirements.txt
requirements = """streamlit==1.28.0
pandas==2.0.3
numpy==1.24.3
scikit-learn==1.3.0
plotly==5.15.0
requests==2.31.0
streamlit-autorefresh==0.0.1
joblib==1.3.2
"""

with open("requirements.txt", "w") as f:
    f.write(requirements)

print("✅ Created requirements.txt")

# 2. Create README.md
readme_content = """# MLB Spread Predictor

An AI-powered web application that analyzes daily MLB games and provides spread betting recommendations.

## Features

- **Daily Predictions**: Automated analysis of all MLB games
- **AI Models**: Ensemble of Random Forest and SVM algorithms
- **Real-time Updates**: Auto-refresh every 15 minutes
- **Interactive Dashboard**: Color-coded recommendations
- **Performance Tracking**: Model accuracy and betting value analysis

## Setup Instructions

### Option 1: Deploy to Streamlit Community Cloud (Recommended)

1. **Fork this repository** to your GitHub account
2. **Sign up** at [share.streamlit.io](https://share.streamlit.io) using your GitHub account
3. **Click "Create app"** and select your forked repository
4. **Set the main file path** to `mlb_predictor_app.py`
5. **Click "Deploy"** - your app will be live in minutes!

### Option 2: Run Locally

```bash
# Clone the repository
git clone https://github.com/yourusername/mlb-predictor.git
cd mlb-predictor

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run mlb_predictor_app.py
```

## How to Access Daily

Once deployed, your application will be available at:
`https://your-app-name.streamlit.app`

The app automatically:
- Refreshes predictions every 15 minutes
- Updates with new game data daily
- Retrains models with latest team statistics

## Usage Guide

1. **View Today's Games**: All MLB games are listed with predictions
2. **Check Recommendations**: Color-coded cards show betting strength
   - 🟢 Green: Strong Bet (70%+ confidence)
   - 🔵 Blue: Good Bet (60-69% confidence) 
   - 🟡 Orange: Fair Bet (55-59% confidence)
   - 🔴 Red: Pass (< 55% confidence)

3. **Filter Results**: Use sidebar to set minimum confidence threshold
4. **Monitor Performance**: Check model accuracy in expandable section

## Customization

You can customize the app by:
- Modifying team statistics sources
- Adjusting prediction confidence thresholds
- Adding new features or betting markets
- Integrating real-time odds APIs

## Disclaimer

This application is for entertainment and educational purposes only. Please bet responsibly and within your means.
"""

with open("README.md", "w") as f:
    f.write(readme_content)

print("✅ Created README.md")