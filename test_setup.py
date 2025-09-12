"""
SIMPLE TEST SCRIPT
==================
This script helps you test if your setup is working correctly.
Run this BEFORE running the main bot to catch any issues early.
"""

import os
import sys

def test_python_packages():
    """Test if all required packages are installed"""
    print("📦 Testing Python packages...")
    
    required_packages = [
        ('telethon', 'Telegram API client'),
        ('requests', 'HTTP requests library'),
        ('aliexpress_api', 'AliExpress affiliate links (optional)')
    ]
    
    all_good = True
    
    for package, description in required_packages:
        try:
            __import__(package)
            print(f"  ✅ {package} - {description}")
        except ImportError:
            print(f"  ❌ {package} - {description} - NOT INSTALLED")
            all_good = False
    
    if not all_good:
        print("\n❌ Some packages are missing!")
        print("🔧 Run this command to install them:")
        print("   pip install -r requirements.txt")
        return False
    
    print("✅ All packages installed correctly!\n")
    return True

def test_configuration():
    """Test if configuration looks correct"""
    print("⚙️ Testing configuration...")
    
    try:
        # Import our main script to check configuration
        sys.path.append('.')
        import simple_telegram_to_facebook as bot
        
        # Check Telegram settings
        if bot.TELEGRAM_API_ID == 'YOUR_API_ID' or not bot.TELEGRAM_API_ID:
            print("  ❌ TELEGRAM_API_ID not configured")
            return False
        else:
            print("  ✅ TELEGRAM_API_ID configured")
        
        if bot.TELEGRAM_API_HASH == 'YOUR_API_HASH' or not bot.TELEGRAM_API_HASH:
            print("  ❌ TELEGRAM_API_HASH not configured")
            return False
        else:
            print("  ✅ TELEGRAM_API_HASH configured")
        
        if not bot.TELEGRAM_PHONE.startswith('+') or len(bot.TELEGRAM_PHONE) < 10:
            print("  ❌ TELEGRAM_PHONE format looks incorrect (should start with + and country code)")
            return False
        else:
            print("  ✅ TELEGRAM_PHONE format looks good")
        
        # Check Facebook settings
        if bot.FACEBOOK_PAGE_TOKEN == 'YOUR_PAGE_TOKEN' or len(bot.FACEBOOK_PAGE_TOKEN) < 50:
            print("  ❌ FACEBOOK_PAGE_TOKEN not configured or too short")
            return False
        else:
            print("  ✅ FACEBOOK_PAGE_TOKEN configured")
        
        if bot.FACEBOOK_PAGE_ID == 'YOUR_PAGE_ID' or not bot.FACEBOOK_PAGE_ID.isdigit():
            print("  ❌ FACEBOOK_PAGE_ID not configured or not numeric")
            return False
        else:
            print("  ✅ FACEBOOK_PAGE_ID configured")
        
        print("✅ Configuration looks good!\n")
        return True
        
    except ImportError as e:
        print(f"  ❌ Could not import main script: {e}")
        return False
    except Exception as e:
        print(f"  ❌ Configuration error: {e}")
        return False

def test_facebook_connection():
    """Test Facebook API connection"""
    print("📘 Testing Facebook connection...")
    
    try:
        import requests
        import simple_telegram_to_facebook as bot
        
        # Test Facebook API with a simple call
        url = f"https://graph.facebook.com/v18.0/{bot.FACEBOOK_PAGE_ID}"
        params = {'access_token': bot.FACEBOOK_PAGE_TOKEN}
        
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            page_data = response.json()
            page_name = page_data.get('name', 'Unknown')
            print(f"  ✅ Connected to Facebook page: {page_name}")
            return True
        else:
            print(f"  ❌ Facebook API error: {response.text}")
            return False
            
    except Exception as e:
        print(f"  ❌ Facebook connection failed: {e}")
        return False

def test_telegram_connection():
    """Test Telegram connection"""
    print("📱 Testing Telegram connection...")
    
    try:
        import simple_telegram_to_facebook as bot
        from telethon.sync import TelegramClient
        
        client = TelegramClient(bot.TELEGRAM_PHONE, bot.TELEGRAM_API_ID, bot.TELEGRAM_API_HASH)
        
        with client:
            # Try to get info about the user (yourself)
            me = client.get_me()
            print(f"  ✅ Connected to Telegram as: {me.first_name}")
            
            # Try to get the channel
            try:
                channel = client.get_entity(bot.TELEGRAM_CHANNEL)
                print(f"  ✅ Found Telegram channel: {channel.title}")
                return True
            except Exception as e:
                print(f"  ❌ Could not access channel {bot.TELEGRAM_CHANNEL}: {e}")
                print(f"     Make sure the channel username is correct and you have access to it")
                return False
                
    except Exception as e:
        print(f"  ❌ Telegram connection failed: {e}")
        print("     This might be normal on first run - you may need to verify your phone number")
        return False

def main():
    """Run all tests"""
    print("🧪 TESTING TELEGRAM TO FACEBOOK BOT SETUP")
    print("=" * 50)
    
    all_tests_passed = True
    
    # Test 1: Python packages
    if not test_python_packages():
        all_tests_passed = False
    
    # Test 2: Configuration
    if not test_configuration():
        all_tests_passed = False
        print("❌ Configuration test failed. Please check your settings.")
        print("📖 See CONFIGURATION_EXAMPLE.py for help")
        return
    
    # Test 3: Facebook connection
    if not test_facebook_connection():
        all_tests_passed = False
    
    # Test 4: Telegram connection
    if not test_telegram_connection():
        all_tests_passed = False
    
    print("\n" + "=" * 50)
    
    if all_tests_passed:
        print("🎉 ALL TESTS PASSED!")
        print("✅ Your bot setup looks good!")
        print("🚀 You can now run: python simple_telegram_to_facebook.py")
    else:
        print("❌ SOME TESTS FAILED")
        print("🔧 Please fix the issues above before running the main bot")
        print("📖 Check README.md for detailed setup instructions")

if __name__ == "__main__":
    main()
