import pandas as pd
from collections import Counter
import re

class TrendAnalyzer:
    def __init__(self, data_path=None):
        self.data_path = data_path
        self.stop_words = set(["the", "and", "a", "of", "to", "is", "in", "it", "that", "i"]) # Minimal example

    def clean_text(self, text):
        """
        Simple text cleaning logic.
        """
        text = text.lower()
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        return text

    def get_top_keywords(self, texts, top_n=10):
        """
        Identifies the most frequent keywords in a list of texts.
        """
        all_words = []
        for text in texts:
            cleaned = self.clean_text(text)
            words = [w for w in cleaned.split() if w not in self.stop_words and len(w) > 3]
            all_words.extend(words)
        
        return Counter(all_words).most_common(top_n)

if __name__ == "__main__":
    analyzer = TrendAnalyzer()
    sample_texts = [
        "NMN and Resveratrol are popular longevity supplements.",
        "Metformin might have anti-aging properties according to recent studies.",
        "Intermittent fasting is a key trend in health and longevity.",
        "Rapamycin is being studied for its effects on life extension."
    ]
    
    print("Analyzing sample trends...")
    keywords = analyzer.get_top_keywords(sample_texts)
    for word, count in keywords:
        print(f"{word}: {count}")
