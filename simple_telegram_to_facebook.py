"""
SIMPLE TELEGRAM TO FACEBOOK BOT
===============================
This script automatically copies posts from a Telegram channel to a Facebook page.
Perfect for beginners who want to automate their social media posting!

WHAT THIS SCRIPT DOES:
- Reads new messages from your Telegram channel
- Posts the content to your Facebook page
- Downloads and shares images automatically
- Adds custom hashtags and text

REQUIREMENTS:
1. Python 3.7+
2. Telegram API credentials
3. Facebook Page Access Token

SETUP INSTRUCTIONS:
1. Fill in the configuration section below
2. Install required packages: pip install telethon requests python-dotenv
3. Run the script: python simple_telegram_to_facebook.py
"""

import os
import logging
import requests
import time
import random
from datetime import datetime, timezone, timedelta
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ========================================
# CONFIGURATION FROM ENVIRONMENT VARIABLES
# ========================================

# Telegram Settings
TELEGRAM_API_ID = os.getenv('TELEGRAM_API_ID')
TELEGRAM_API_HASH = os.getenv('TELEGRAM_API_HASH')
TELEGRAM_PHONE = os.getenv('TELEGRAM_PHONE')
TELEGRAM_CHANNEL = os.getenv('TELEGRAM_CHANNEL')

# Facebook Settings
FACEBOOK_PAGE_TOKEN = os.getenv('FACEBOOK_PAGE_TOKEN')
FACEBOOK_PAGE_ID = os.getenv('FACEBOOK_PAGE_ID')

# Bot Settings
COPY_EXACT_TEXT = os.getenv('COPY_EXACT_TEXT', 'True').lower() == 'true'

# Custom Text and Hashtags (Set to empty if you want exact copy)
CUSTOM_MESSAGE = ""  # Leave empty to not add any extra text

HASHTAGS = []  # Leave empty to not add any hashtags

# Copy Settings
COPY_EXACT_TEXT = True  # Set to True to copy exactly as posted on Telegram

# ========================================
# END OF CONFIGURATION
# ========================================

# Validate required environment variables
def validate_environment():
    """Check if all required environment variables are set"""
    required_vars = [
        ('TELEGRAM_API_ID', TELEGRAM_API_ID),
        ('TELEGRAM_API_HASH', TELEGRAM_API_HASH),
        ('TELEGRAM_PHONE', TELEGRAM_PHONE),
        ('TELEGRAM_CHANNEL', TELEGRAM_CHANNEL),
        ('FACEBOOK_PAGE_TOKEN', FACEBOOK_PAGE_TOKEN),
        ('FACEBOOK_PAGE_ID', FACEBOOK_PAGE_ID)
    ]
    
    missing_vars = []
    for var_name, var_value in required_vars:
        if not var_value:
            missing_vars.append(var_name)
    
    if missing_vars:
        print("ERROR: Missing required environment variables:")
        for var in missing_vars:
            print(f"  - {var}")
        print("\nPlease check your .env file and make sure all required variables are set.")
        print("See .env.example for reference.")
        return False
    return True

# Set up logging to track what the bot is doing
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler('bot_activity.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

# Create folders if they don't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Initialize Telegram client
telegram_client = TelegramClient(TELEGRAM_PHONE, TELEGRAM_API_ID, TELEGRAM_API_HASH)

def print_status(message):
    """Print status messages to console and log file"""
    # Remove emojis for console output to avoid encoding issues
    console_message = message.encode('ascii', 'ignore').decode('ascii')
    print(f"[BOT] {console_message}")
    
    # Log the full message with emojis to file
    try:
        logging.info(message)
    except UnicodeEncodeError:
        # Fallback to ASCII if Unicode fails
        logging.info(console_message)

def create_full_message(original_text):
    """Create the final message - exact copy or with additions"""
    if COPY_EXACT_TEXT:
        # Return exact copy of original message
        return original_text
    
    # Add custom text and hashtags only if COPY_EXACT_TEXT is False
    full_message = original_text
    
    if CUSTOM_MESSAGE.strip():
        full_message += f"\n\n{CUSTOM_MESSAGE}"
    
    if HASHTAGS:
        full_message += f"\n\n{' '.join(HASHTAGS)}"
    
    return full_message

def upload_image_to_facebook(image_path):
    """Upload an image to Facebook and return the photo ID"""
    url = f"https://graph.facebook.com/v18.0/{FACEBOOK_PAGE_ID}/photos"
    
    try:
        with open(image_path, 'rb') as image_file:
            files = {'source': ('image.jpg', image_file, 'image/jpeg')}
            data = {
                'access_token': FACEBOOK_PAGE_TOKEN,
                'published': 'false'  # Don't publish yet, just upload
            }
            
            response = requests.post(url, files=files, data=data)
            
            if response.status_code == 200:
                photo_id = response.json().get('id')
                print_status(f"Image uploaded successfully (ID: {photo_id})")
                return photo_id
            else:
                print_status(f"Failed to upload image: {response.text}")
                return None
                
    except Exception as e:
        print_status(f"Error uploading image: {e}")
        return None

def post_to_facebook(message_text, image_path=None):
    """Post a message (with optional image) to Facebook page"""
    url = f"https://graph.facebook.com/v18.0/{FACEBOOK_PAGE_ID}/feed"
    
    try:
        data = {
            'message': message_text,
            'access_token': FACEBOOK_PAGE_TOKEN
        }
        
        # If there's an image, upload it first
        if image_path and os.path.exists(image_path):
            photo_id = upload_image_to_facebook(image_path)
            if photo_id:
                data['attached_media[0]'] = f'{{"media_fbid":"{photo_id}"}}'
        
        response = requests.post(url, data=data)
        
        if response.status_code == 200:
            post_id = response.json().get('id')
            print_status(f"Posted to Facebook successfully! Post ID: {post_id}")
            return post_id
        else:
            print_status(f"Failed to post to Facebook: {response.text}")
            return None
            
    except Exception as e:
        print_status(f"Error posting to Facebook: {e}")
        return None

async def download_telegram_image(message):
    """Download image from Telegram message"""
    try:
        image_path = os.path.join('images', f"telegram_image_{message.id}.jpg")
        await telegram_client.download_media(message.media, file=image_path)
        print_status(f"Downloaded image: {image_path}")
        return image_path
    except Exception as e:
        print_status(f"Error downloading image: {e}")
        return None

async def process_telegram_message(message):
    """Process a single Telegram message and post it to Facebook"""
    try:
        # Check if message has text content
        if not message.message:
            print_status("Message has no text content, skipping...")
            return
        
        print_status(f"Processing message: {message.message[:50]}...")
        
        # Create final message (exact copy or with additions based on settings)
        final_message = create_full_message(message.message)
        
        # Handle image if present
        image_path = None
        if message.photo:
            image_path = await download_telegram_image(message)
        
        # Post to Facebook
        post_to_facebook(final_message, image_path)
        
        # Wait a bit between posts to avoid rate limits
        time.sleep(random.uniform(2, 5))
        
    except Exception as e:
        print_status(f"Error processing message: {e}")

def get_last_check_time():
    """Get the last time we checked for new messages"""
    last_check_file = 'last_check_time.txt'
    
    if os.path.exists(last_check_file):
        try:
            with open(last_check_file, 'r') as f:
                time_str = f.read().strip()
                return datetime.fromisoformat(time_str)
        except:
            pass
    
    # If no file or error, return 3 hours ago
    return datetime.now(timezone.utc) - timedelta(hours=3)

def save_last_check_time():
    """Save the current time as last check time"""
    with open('last_check_time.txt', 'w') as f:
        f.write(datetime.now(timezone.utc).isoformat())

async def main():
    """Main function that runs the bot"""
    print_status("Starting Telegram to Facebook Bot...")
    print_status(f"Telegram Channel: {TELEGRAM_CHANNEL}")
    print_status(f"Facebook Page ID: {FACEBOOK_PAGE_ID}")
    print_status(f"Copy Mode: {'Exact Copy' if COPY_EXACT_TEXT else 'With Additions'}")
    
    last_check_time = get_last_check_time()
    print_status(f"Looking for messages newer than: {last_check_time}")
    
    try:
        async with telegram_client:
            # Get the Telegram channel
            channel = await telegram_client.get_entity(TELEGRAM_CHANNEL)
            
            # Get recent messages
            history = await telegram_client(GetHistoryRequest(
                peer=channel,
                offset_id=0,
                offset_date=None,
                add_offset=0,
                limit=5,  # Check last 5 messages
                max_id=0,
                min_id=0,
                hash=0
            ))
            
            new_messages_count = 0
            
            # Process each message
            for message in history.messages:
                if message.date > last_check_time:
                    await process_telegram_message(message)
                    new_messages_count += 1
            
            if new_messages_count == 0:
                print_status("No new messages found")
            else:
                print_status(f"Processed {new_messages_count} new messages")
            
            # Save the current time
            save_last_check_time()
            
    except Exception as e:
        print_status(f"Error in main function: {e}")
    
    print_status("Bot finished running")

if __name__ == "__main__":
    """Run the bot when script is executed"""
    
    print("=" * 50)
    print("  TELEGRAM TO FACEBOOK BOT")
    print("  Simple version for beginners")
    print("=" * 50)
    
    # Validate environment variables
    if not validate_environment():
        exit(1)
    
    # Run the bot
    with telegram_client:
        telegram_client.loop.run_until_complete(main())
    
    print("\nBot execution completed!")
    print("Check 'bot_activity.log' file for detailed logs")
