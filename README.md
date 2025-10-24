# Klaviyo Campaign Export Tool

A Python script to export Klaviyo email campaign performance data including subject lines, sends, opens, and clicks. Perfect for analyzing campaign performance, creating reports, or building dashboards.

## Features

✅ Export campaign data from the last 6 months (or custom date range)  
✅ Get complete campaign details: subject lines, send times, sender info  
✅ Pull performance metrics: opens, clicks, bounces, delivery rates  
✅ Bonus analysis script with insights and benchmarks  
✅ Export to CSV for easy analysis in Excel, Python, or BI tools

## Setup

1. **Get your Klaviyo API Key:**
   - Log into Klaviyo
   - Go to Settings → API Keys
   - Create a Private API Key with these scopes:
     - `campaigns:read`
     - (Optional: `flows:read` if you want to expand this later)
   - Copy the API key

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your API key** (choose one method):

   **Option A: Config file (recommended)**
   ```bash
   cp config.example.py config.py
   # Edit config.py and add your API key
   ```

   **Option B: Environment variable**
   ```bash
   export KLAVIYO_API_KEY="your_api_key_here"
   ```

   **Option C: Edit the script directly**
   - Open `export_campaigns.py`
   - Replace `YOUR_API_KEY_HERE` with your actual API key

## Usage

Run the script:
```bash
python3 export_campaigns.py
```

The script will:
1. Fetch all email campaigns from the last 6 months
2. Get performance stats for each campaign
3. Export everything to `klaviyo_campaigns_export.csv`

## Configuration

You can customize the export by editing `config.py`:

```python
MONTHS_BACK = 6              # How many months of campaigns to export
OUTPUT_FILENAME = "..."      # CSV output filename  
RATE_LIMIT_DELAY = 0.2       # Delay between API calls (seconds)
```

## Output

The CSV includes:
- Campaign ID and Name
- Subject Line
- Status (sent, draft, etc.)
- Send Time
- From Name/Email
- Preview Text
- Recipients (total attempted sends)
- Delivered
- Bounced
- Opens (total)
- Opens (unique)
- Open Rate (%)
- Clicks (total)
- Clicks (unique)
- Click Rate (%)

## Notes

- The script respects Klaviyo's rate limits (5 requests/second)
- If you have many campaigns, it may take a few minutes
- The conversion_metric_id in the script is set to "PLACEHOLDER" - if you get errors about this, you may need to fetch a real metric ID first (like your "Placed Order" metric)

## Troubleshooting

**"Error fetching campaigns: 400"**
- Check your API key has the correct scopes
- Make sure you're using a Private API Key, not Public

**"Error fetching stats: 400"**  
- You may need to update the conversion_metric_id
- Run this command to get your metric IDs:
  ```bash
  curl --request GET \
    --url 'https://a.klaviyo.com/api/metrics/' \
    --header 'Authorization: Klaviyo-API-Key YOUR_API_KEY' \
    --header 'revision: 2024-10-15'
  ```
- Look for "Placed Order" or another metric and use its ID

**No campaigns found**
- Check that you have campaigns sent in the last 6 months
- Check they're email campaigns (not SMS)

## Analyzing the Data

Once exported, you can:
- Open in Excel/Google Sheets for quick analysis
- Load into Python with pandas:
  ```python
  import pandas as pd
  df = pd.read_csv('klaviyo_campaigns_export.csv')
  print(df.describe())
  ```
- Import into your database
- Use for reporting/dashboards

## Contributing

Contributions are welcome! Here are some ways you can help:

- 🐛 Report bugs or issues
- 💡 Suggest new features
- 📝 Improve documentation
- 🔧 Submit pull requests


## License

MIT License - see [LICENSE](LICENSE) file for details

## Disclaimer

This is an unofficial tool and is not affiliated with or endorsed by Klaviyo. Use at your own risk.

## Support

If you find this tool helpful, please:
- ⭐ Star this repo
- 🐦 Share it with others
- 🙏 Consider contributing improvements

---

Made with ☕ for the Klaviyo community
