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
MONTHS_BACK = 6  # How many months of campaigns to export (used for filtering campaigns)
OUTPUT_FILENAME = "klaviyo_campaigns_export.csv"

# Timeframe for Statistics
# NOTE: The script uses "last_30_days" for fetching campaign statistics
# Valid options: today, yesterday, this_week, last_7_days, last_week, this_month,
#                last_30_days, last_month, last_90_days, last_3_months,
#                last_365_days, last_12_months, this_year, last_year
# The MONTHS_BACK setting above filters which campaigns to fetch, but statistics
# are always pulled using the timeframe below (hardcoded as last_30_days in the script)

# Rate Limiting
RATE_LIMIT_DELAY = 1.0  # Delay between API calls in seconds (1 request/sec, increase if you still hit rate limits)
