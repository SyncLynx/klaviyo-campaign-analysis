"""
Example configuration file for Klaviyo Campaign Export Tool

To use this:
1. Copy this file to config.py:
   cp config.example.py config.py
2. Edit config.py and add your actual API key
3. config.py is in .gitignore so your key won't be committed
"""

# Your Klaviyo Private API Key
# Get this from: Klaviyo Settings → API Keys
# Required scopes: campaigns:read
API_KEY = "YOUR_API_KEY_HERE"

# Klaviyo API Configuration
BASE_URL = "https://a.klaviyo.com/api"
REVISION = "2024-10-15"

# Export Settings
MONTHS_BACK = 6  # How many months of campaigns to export
OUTPUT_FILENAME = "klaviyo_campaigns_export.csv"

# Rate Limiting
RATE_LIMIT_DELAY = 0.5  # Delay between API calls in seconds (conservative to avoid 429 errors)
