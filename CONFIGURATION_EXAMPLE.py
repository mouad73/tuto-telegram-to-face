"""
EXAMPLE CONFIGURATION
=====================
This file shows you exactly what to change in the main script.
Copy these values to the CONFIGURATION SECTION in simple_telegram_to_facebook.py

BEFORE (what you'll see in the script):
"""

# TELEGRAM SETTINGS (Replace with your real values)
TELEGRAM_API_ID = 'YOUR_API_ID_HERE'  # Get from my.telegram.org
TELEGRAM_API_HASH = 'YOUR_API_HASH_HERE'  # Get from my.telegram.org  
TELEGRAM_PHONE = '+1234567890'  # Your phone number with country code
TELEGRAM_CHANNEL = 't.me/yourchannel'  # Your Telegram channel

# FACEBOOK SETTINGS (Replace with your real values)
FACEBOOK_PAGE_TOKEN = 'YOUR_FACEBOOK_PAGE_TOKEN_HERE'  # Get from Facebook for Developers
FACEBOOK_PAGE_ID = 'YOUR_FACEBOOK_PAGE_ID_HERE'  # Your Facebook page ID

# ALIEXPRESS SETTINGS (Optional - for affiliate links)
ALIEXPRESS_APP_KEY = "YOUR_APP_KEY"
ALIEXPRESS_SECRET_KEY = "YOUR_SECRET_KEY"
USE_ALIEXPRESS = True  # Set to False if you don't have AliExpress API

"""
AFTER (example with real-looking values):
"""

# TELEGRAM SETTINGS
TELEGRAM_API_ID = '12345678'  # This will be a number from my.telegram.org
TELEGRAM_API_HASH = 'abcd1234efgh5678ijkl9012mnop3456'  # This will be a long string
TELEGRAM_PHONE = '+212650240022'  # Your actual phone number
TELEGRAM_CHANNEL = 't.me/AutomatePost73'  # Your actual channel

# FACEBOOK SETTINGS  
FACEBOOK_PAGE_TOKEN = 'EAAiAZBDCxKZBsBO...'  # Very long token from Facebook
FACEBOOK_PAGE_ID = '345602361977620'  # Your page ID (numbers only)

# ALIEXPRESS SETTINGS
ALIEXPRESS_APP_KEY = "508800"
ALIEXPRESS_SECRET_KEY = "TK2sfsvmmxQ89nS4oV9i7AX8OJM8XEH6"
USE_ALIEXPRESS = True

"""
STEP-BY-STEP GUIDE:
===================

1. Open 'simple_telegram_to_facebook.py' in any text editor
2. Find the line that says '# CONFIGURATION SECTION - EDIT THIS PART'
3. Replace each 'YOUR_..._HERE' with your actual values
4. Save the file
5. Run: python simple_telegram_to_facebook.py

GETTING YOUR CREDENTIALS:
========================

Telegram API:
- Go to https://my.telegram.org
- Login with your phone number
- Go to 'API development tools'
- Create a new application
- Copy the api_id and api_hash

Facebook Page Token:
- Go to https://developers.facebook.com
- Create an app or use existing one
- Add 'Pages' product to your app
- Go to Pages -> Settings
- Generate a Page Access Token
- Select your page and copy the token

Facebook Page ID:
- Go to your Facebook page
- Click 'About' section
- Scroll down to find 'Page ID'
- Or use Graph API Explorer with /me/accounts

AliExpress API (Optional):
- Go to https://portals.aliexpress.com
- Register as a developer
- Create an app
- Get your App Key and Secret Key

TIPS:
=====
- Keep your credentials secure and private
- Test with a small channel first
- The bot only processes messages with AliExpress links
- Check bot_activity.log file for any errors
- The bot looks for new messages from the last 3 hours
"""
