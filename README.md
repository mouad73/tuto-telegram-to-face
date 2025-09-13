# 🤖 Simple Telegram to Facebook Bot

## 📖 What This Bot Does
This bot automatically copies posts from your Telegram channel to your Facebook page. It's perfect for:
- Auto-posting with custom hashtags
- Sharing images automatically

## 🛠️ Setup Instructions

### Step 1: Install Python
1. Download Python 3.7+ from [python.org](https://python.org)
2. During installation, check "Add Python to PATH"

### Step 2: Clone or Download the Bot
```bash
git clone https://github.com/mouad73/tuto-telegram-to-face.git
cd tuto-telegram-to-face
```

### Step 3: Install Required Packages
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
2. Edit the `.env` file with your actual credentials:
   ```bash
   notepad .env  # On Windows
   nano .env     # On Linux/Mac
   ```

### Step 5: Get Your API Credentials

#### Telegram API:
1. Go to [my.telegram.org](https://my.telegram.org)
2. Log in with your phone number
3. Create a new app
4. Copy your `api_id` and `api_hash` to `.env` file

#### Facebook Page Token:
1. Go to [Facebook for Developers](https://developers.facebook.com)
2. Create an app
3. Add "Pages" product
4. Generate a Page Access Token
5. Copy your Page ID and token to `.env` file

### Step 6: Run the Bot
```bash
python simple_telegram_to_facebook.py
```

## 📋 Project Structure

```
tuto-telegram-to-face/
├── simple_telegram_to_facebook.py  # Main bot script
├── requirements.txt                # Required Python packages
├── .env.example                   # Example environment file
├── .env                          # Your actual credentials (not in git)
├── .gitignore                    # Files to ignore in git
├── README.md                     # This file
├── CONFIGURATION_EXAMPLE.py      # Configuration help
├── test_setup.py                 # Setup validation script
├── setup.bat                     # Windows setup script
└── run_bot.bat                   # Windows run script
```

## 🔧 Environment Variables

Edit the `.env` file with your credentials:

```env
# Telegram API Configuration
TELEGRAM_API_ID=your_api_id
TELEGRAM_API_HASH=your_api_hash
TELEGRAM_PHONE=+1234567890
TELEGRAM_CHANNEL=t.me/yourchannel

# Facebook API Configuration
FACEBOOK_PAGE_TOKEN=your_page_token
FACEBOOK_PAGE_ID=your_page_id

# Bot Settings
COPY_EXACT_TEXT=True
```

## 🚨 Troubleshooting

### Common Issues:

1. **"Module not found" error**
   ```bash
   pip install -r requirements.txt
   ```

2. **"Missing environment variables" error**
   - Make sure `.env` file exists
   - Check that all required variables are set
   - Run `python test_setup.py` to validate

3. **Telegram login issues**
   - Verify your phone number format (+country_code)
   - Check your API credentials from my.telegram.org

4. **Facebook posting fails**
   - Verify your Page Access Token is valid
   - Check if your Facebook app has proper permissions

### Getting Help:
- Check the `bot_activity.log` file for detailed error messages
- Run `python test_setup.py` to validate your setup
- Make sure all credentials are correctly entered in `.env`

## ⚡ Running Automatically

### Windows (Task Scheduler):
1. Open Task Scheduler
2. Create Basic Task
3. Set it to run daily or hourly
4. Action: Start Program
5. Program: `python`
6. Arguments: `path\to\simple_telegram_to_facebook.py`

### Mac/Linux (Cron):
Add this to crontab (`crontab -e`):
```bash
# Run every hour
0 * * * * cd /path/to/tuto-telegram-to-face && python simple_telegram_to_facebook.py
```

## 🔒 Security Notes

- Never commit your `.env` file to git
- Keep your API credentials secure
- Don't share your tokens publicly
- The `.env` file is automatically ignored by git

## 📝 License
This script is provided free for educational purposes. Use responsibly and follow platform terms of service.

## ⚠️ Important Notes
- Respect rate limits to avoid being blocked
- Test thoroughly before using in production
- Always follow Facebook and Telegram terms of service
- This bot only copies text posts and images (no videos, documents, etc.)

## 🤝 Contributing
Feel free to fork this project and submit pull requests for improvements!
