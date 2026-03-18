import time
import random
import string
import json
from datetime import datetime
from playwright.sync_api import sync_playwright

print("🚀 Outlook Creator v5.2 — DYNAMIC TAB PRIMING + LOCATOR FALLBACK 🔥 (self-healing!)")

NUM_ACCOUNTS = int(input("How many accounts? (start with 1): "))

# === REALISTIC HUMAN NAMES ===
first_names = ["Alex", "Jordan", "Taylor", "Casey", "Morgan", "Jamie", "Riley", "Cameron", "Quinn", "Parker",
               "Drew", "Avery", "Reese", "Hayden", "Logan", "Skyler", "Blake", "Emerson", "Rowan"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez",
              "Martinez", "Hernandez", "Lopez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson"]

def generate_strong_password(length=16):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

def is_email_field_focused(page):
    """Dynamic check: is the active element the email/username field?"""
    return page.evaluate("""() => {
        const el = document.activeElement;
        return el && (el.placeholder && el.placeholder.includes("outlook") || 
                     el.id && (el.id.includes("MemberName") || el.id.includes("username")) ||
                     el.getAttribute("aria-label") && el.getAttribute("aria-label").toLowerCase().includes("email"));
    }""")

def create_outlook_account():
    username = "steamout" + ''.join(random.choices(string.digits, k=8))
    outlook_email = f"{username}@outlook.com"
    outlook_password = generate_strong_password()
   
    with sync_playwright() as p:
        # Stealth + realistic
        browser = p.chromium.launch(
            headless=False, 
            slow_mo=650,
            args=["--disable-blink-features=AutomationControlled"]
        )
        page = browser.new_page()
        page.set_viewport_size({"width": 1280, "height": 900})
       
        YOUR_URL = "https://signup.live.com/signup?sru=https%3a%2f%2flogin.live.com%2foauth20_authorize.srf%3flc%3d1033%26client_id%3d9199bf20-a13f-4107-85dc-02114787ef48%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26mkt%3dEN-US%26opid%3dADF6A33CFB797721%26opidt%3d1773813230%26uaid%3de9cc442c60f57c549340a4be05df609d%26contextid%3d97A9CB9121F58BB3%26opignore%3d1&mkt=EN-US&uiflavor=web&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c&client_id=9199bf20-a13f-4107-85dc-02114787ef48&uaid=e9cc442c60f57c549340a4be05df609d&suc=9199bf20-a13f-4107-85dc-02114787ef48&fluent=2&lic=1"
       
        print("🌐 Opening signup page...")
        page.goto(YOUR_URL, wait_until="networkidle")
        time.sleep(15)  # full load + banners
        
        page.bring_to_front()
        page.click("body")
        time.sleep(3)
        page.keyboard.press("Escape")  # kill banner
        time.sleep(2)

        # === DYNAMIC EMAIL PRIMING (self-healing!) ===
        print("→ Dynamic priming to email field...")
        for i in range(25):  # safety max
            page.keyboard.press("Tab")
            time.sleep(0.4)
            if is_email_field_focused(page):
                print(f"✅ Email field found after {i+1} tabs!")
                break
        else:
            print("⚠️ Fallback: using locator")
            try:
                page.get_by_role("textbox", name="Email address").click()
            except:
                page.locator("input[placeholder*='outlook'], input[name*='MemberName']").click()

        page.keyboard.type(username, delay=75)
        time.sleep(1.2)
        page.keyboard.press("Tab")
        page.keyboard.press("Tab")
        page.keyboard.press("Enter")
        time.sleep(6)
        page.screenshot(path="step_1_email.png")

        # === PASSWORD (locator fallback + keyboard) ===
        print("→ Typing password...")
        try:
            page.get_by_role("textbox", name="Create password").fill(outlook_password)
        except:
            page.keyboard.type(outlook_password, delay=65)
        time.sleep(1)
        page.keyboard.press("Tab")
        page.keyboard.press("Tab")
        page.keyboard.press("Enter")
        time.sleep(6)
        page.screenshot(path="step_2_password.png")

        # === DOB (kept keyboard - reliable for selects) ===
        print("→ DOB...")
        page.keyboard.press("Tab")
        for _ in range(random.randint(1, 8)):
            page.keyboard.press("ArrowDown")
            time.sleep(0.35)
        page.keyboard.press("Tab")
        for _ in range(random.randint(1, 8)):
            page.keyboard.press("ArrowDown")
            time.sleep(0.35)
        page.keyboard.press("Tab")
        year = random.randint(1989, 2007)
        page.keyboard.type(str(year))
        time.sleep(1)
        page.keyboard.press("Tab")
        page.keyboard.press("Tab")
        page.keyboard.press("Enter")
        time.sleep(7)
        page.screenshot(path="step_3_dob.png")
import time
import random
import string
import json
from datetime import datetime
from playwright.sync_api import sync_playwright

print("🚀 Outlook Creator v5.2 — DYNAMIC TAB PRIMING + LOCATOR FALLBACK 🔥 (self-healing!)")

NUM_ACCOUNTS = int(input("How many accounts? (start with 1): "))

# === REALISTIC HUMAN NAMES ===
first_names = ["Alex", "Jordan", "Taylor", "Casey", "Morgan", "Jamie", "Riley", "Cameron", "Quinn", "Parker",
               "Drew", "Avery", "Reese", "Hayden", "Logan", "Skyler", "Blake", "Emerson", "Rowan"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez",
              "Martinez", "Hernandez", "Lopez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson"]

def generate_strong_password(length=16):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

def is_email_field_focused(page):
    """Dynamic check: is the active element the email/username field?"""
    return page.evaluate("""() => {
        const el = document.activeElement;
        return el && (el.placeholder && el.placeholder.includes("outlook") || 
                     el.id && (el.id.includes("MemberName") || el.id.includes("username")) ||
                     el.getAttribute("aria-label") && el.getAttribute("aria-label").toLowerCase().includes("email"));
    }""")

def create_outlook_account():
    username = "steamout" + ''.join(random.choices(string.digits, k=8))
    outlook_email = f"{username}@outlook.com"
    outlook_password = generate_strong_password()
   
    with sync_playwright() as p:
        # Stealth + realistic
        browser = p.chromium.launch(
            headless=False, 
            slow_mo=650,
            args=["--disable-blink-features=AutomationControlled"]
        )
        page = browser.new_page()
        page.set_viewport_size({"width": 1280, "height": 900})
       
        YOUR_URL = "https://signup.live.com/signup?sru=https%3a%2f%2flogin.live.com%2foauth20_authorize.srf%3flc%3d1033%26client_id%3d9199bf20-a13f-4107-85dc-02114787ef48%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26mkt%3dEN-US%26opid%3dADF6A33CFB797721%26opidt%3d1773813230%26uaid%3de9cc442c60f57c549340a4be05df609d%26contextid%3d97A9CB9121F58BB3%26opignore%3d1&mkt=EN-US&uiflavor=web&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c&client_id=9199bf20-a13f-4107-85dc-02114787ef48&uaid=e9cc442c60f57c549340a4be05df609d&suc=9199bf20-a13f-4107-85dc-02114787ef48&fluent=2&lic=1"
       
        print("🌐 Opening signup page...")
        page.goto(YOUR_URL, wait_until="networkidle")
        time.sleep(5)  # full load + banners
        
        page.bring_to_front()
        page.click("body")
        time.sleep(3)
        page.keyboard.press("Escape")  # kill banner
        time.sleep(2)

        # === DYNAMIC EMAIL PRIMING (self-healing!) ===
        print("→ Dynamic priming to email field...")
        for i in range(25):  # safety max
            page.keyboard.press("Tab")
            time.sleep(0.4)
            if is_email_field_focused(page):
                print(f"✅ Email field found after {i+1} tabs!")
                break
        else:
            print("⚠️ Fallback: using locator")
            try:
                page.get_by_role("textbox", name="Email address").click()
            except:
                page.locator("input[placeholder*='outlook'], input[name*='MemberName']").click()

        page.keyboard.type(username, delay=4)
        time.sleep(1.2)
        page.keyboard.press("Tab")
        page.keyboard.press("Tab")
        page.keyboard.press("Enter")
        time.sleep(6)
        page.screenshot(path="C:\\Users\\Jweng\\OneDrive\\Desktop\\protonMailGenerator-main\\mailgen\\Logger\\step_1_email.png")

        # === PASSWORD (locator fallback + keyboard) ===
        print("→ Typing password...")
        try:
            page.get_by_role("textbox", name="Create password").fill(outlook_password)
        except:
            page.keyboard.type(outlook_password, delay=3)
        time.sleep(1)
        page.keyboard.press("Tab")
        page.keyboard.press("Tab")
        page.keyboard.press("Enter")
        time.sleep(6)
        page.screenshot(path="C:\\Users\\Jweng\\OneDrive\\Desktop\\protonMailGenerator-main\\mailgen\\Logger\\step_2_password.png")

        # === DOB (kept keyboard - reliable for selects) ===
        print("→ DOB...")
        page.keyboard.press("Tab")
        for _ in range(random.randint(1, 8)):
            page.keyboard.press("ArrowDown")
            time.sleep(0.35)
        page.keyboard.press("Tab")
        for _ in range(random.randint(1, 8)):
            page.keyboard.press("ArrowDown")
            time.sleep(0.35)
        page.keyboard.press("Tab")
        year = random.randint(1989, 2007)
        page.keyboard.type(str(year))
        time.sleep(1)
        page.keyboard.press("Tab")
        page.keyboard.press("Tab")
        page.keyboard.press("Enter")
        time.sleep(7)
        page.screenshot(path="C:\\Users\\Jweng\\OneDrive\\Desktop\\protonMailGenerator-main\\mailgen\\Logger\\step_3_dob.png")

        # === NAME ===
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        print(f"→ Name: {first_name} {last_name}")
        page.keyboard.type(first_name, delay=4)
        page.keyboard.press("Tab")
        page.keyboard.type(last_name, delay=3)
        page.keyboard.press("Enter")
        time.sleep(9)
        page.screenshot(path="C:\\Users\\Jweng\\OneDrive\\Desktop\\protonMailGenerator-main\\mailgen\\Logger\\step_4_created.png")

        # === OPTIONAL PHONE SKIP (new in 2025-2026) ===
        try:
            if page.get_by_text("Add phone number", timeout=3000).is_visible():
                print("📱 Phone verification appeared — skipping...")
                page.keyboard.press("Escape")
                time.sleep(2)
                page.keyboard.press("Enter")
        except:
            pass

        print(f"✅ OUTLOOK CREATED: {outlook_email} | {first_name} {last_name} ({year})")
        return outlook_email, outlook_password, browser

# === STEAM PART (unchanged - it's solid) ===
def create_steam_account(outlook_email, outlook_password, browser):
    steam_password = generate_strong_password(14)
    page = browser.new_page()
    page.goto("https://store.steampowered.com/join/")
    page.fill("#email", outlook_email)
    page.fill("#reenter_email", outlook_email)
    page.fill("#password", steam_password)
    page.fill("#reenter_password", steam_password)
    page.click("input[type=checkbox]")
    page.click("button.btn_green_white_innerfade")
    print("✅ Steam form submitted")

    # === AUTO VERIFY ===
    inbox = browser.new_page()
    inbox.goto("https://outlook.live.com/mail/0/")
    inbox.fill('input[type="email"]', outlook_email)
    inbox.click('button:has-text("Next")')
    time.sleep(4)
    inbox.fill('input[type="password"]', outlook_password)
    inbox.click('button:has-text("Sign in")')
    time.sleep(8)
    inbox.click('text=Steam')
    time.sleep(3)
    inbox.click('a:has-text("Verify"), button:has-text("Verify")')
    print("✅ Verification clicked!")
    
    page.goto("https://store.steampowered.com/login/")
    page.fill("#input_username", outlook_email)
    page.fill("#input_password", steam_password)
    page.click("button.btnv6_blue")
    page.wait_for_load_state("networkidle")
    print("🔥 SUCCESSFULLY LOGGED IN!")
    return {
        "outlook_email": outlook_email,
        "outlook_password": outlook_password,
        "steam_password": steam_password,
        "created_at": datetime.now().isoformat(),
        "status": "verified_and_logged_in"
    }

# ====================== MAIN ======================
accounts = []
for i in range(NUM_ACCOUNTS):
    print(f"\n🚀 Creating account {i+1}/{NUM_ACCOUNTS}...")
    try:
        email, pw, browser = create_outlook_account()
        acc = create_steam_account(email, pw, browser)
        accounts.append(acc)
        print(f"✅ Account ready: {acc['outlook_email']}")
    except Exception as e:
        print(f"❌ Account {i+1} failed: {e}")
        try:
            page.screenshot(path=f"error_{i}.png")
        except:
            pass

if accounts:
    with open("steam_accounts.json", "w", encoding="utf-8") as f:
        json.dump(accounts, f, indent=4)
    print(f"\n🎉 ALL DONE! {len(accounts)} accounts saved!")
else:
    print("\n📸 Check the step_*.png screenshots — the dynamic priming should have fixed it!")