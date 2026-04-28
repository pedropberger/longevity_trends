# Longevity Trends Reddit Scraper

A Python-based tool designed to scrape health and longevity-related subreddits to identify emerging trends, popular supplements, and lifestyle interventions.

## 🚀 Features

- **Reddit Scraper**: Efficiently fetch posts and comments from targeted subreddits using the Reddit API (PRAW).
- **Data Processor**: Clean and structure raw Reddit data for analysis.
- **Trend Analyzer**: Identify recurring themes, keywords, and sentiment trends using NLP.
- **Configurable**: Easily add new subreddits or keywords to track.

## 📂 Project Structure

```text
longevity_trends/
├── src/
│   ├── collector/      # Scripts for data collection (Reddit API)
│   ├── processor/      # Data cleaning and preprocessing
│   ├── analyzer/       # Trend analysis and visualization
│   └── utils/          # Shared utilities and helpers
├── config/             # Configuration files (YAML)
├── data/               # Local data storage (ignored by Git)
├── notebooks/          # Exploratory analysis and prototyping
├── tests/              # Unit and integration tests
├── .env.example        # Template for environment variables
└── requirements.txt    # Project dependencies
```

## 🛠️ Setup

### Prerequisites

- Python 3.9+
- A Reddit account and [API credentials](https://www.reddit.com/prefs/apps)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd longevity_trends
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   - Copy `.env.example` to `.env`
   - Fill in your Reddit API credentials (`REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET`, etc.)

## 📖 Usage

*(To be updated as implementation progresses)*

### Running the Scraper
```bash
python -m src.collector.reddit_scraper
```

### Running Analysis
```bash
python -m src.analyzer.trend_analyzer
```

## 🧪 Testing

Run tests using pytest:
```bash
pytest
```

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
