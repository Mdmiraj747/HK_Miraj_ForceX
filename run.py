import os
import time

# Clear screen & Intro
os.system("clear")
print("""
██╗  ██╗██╗  ██╗    ███╗   ███╗██╗██████╗  █████╗      ██╗██╗
██║ ██╔╝██║ ██╔╝    ████╗ ████║██║██╔══██╗██╔══██╗     ██║██║
█████╔╝ █████╔╝     ██╔████╔██║██║██████╔╝███████║     ██║██║
██╔═██╗ ██╔═██╗     ██║╚██╔╝██║██║██╔═══╝ ██╔══██║██   ██║██║
██║  ██╗██║  ██╗    ██║ ╚═╝ ██║██║██║     ██║  ██║╚█████╔╝██║
╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝╚═╝     ╚═╝  ╚═╝ ╚════╝ ╚═╝
       HK_Miraj_ForceX — Powered by LK Mahi ❤️
""")

print("\n🎙️ Voice: ‘Jab Pyar Hacker ban jaaye... duniya sirf ek naam se darti hai... HK Miraj!’")
input("\n🔔 [ENTER] চাপলে টুল শুরু হবে...\n")

# Main Menu
def main_menu():
    while True:
        os.system("clear")
        print("""
HK_Miraj_ForceX — Official Tool                         Powered by LK Mahi ❤️

📱 ১. লোকেশন ট্র্যাকার
📶 ২. ওয়াই-ফাই হ্যাকিং গাইড
📷 ৩. ক্যামেরা অ্যাক্সেস (ডামি)
🎙 ৪. মাইক্রোফোন মনিটর (ডামি)
💬 ৫. এল কে মোড (লুকানো)
❌ ৬. এক্সিট
""")
        choice = input("আপনার পছন্দ (1-6): ")

        if choice == "1":
            print("🔍 লোকেশন ট্র্যাকার চালু হচ্ছে...")
            input("🕵️‍♂️ (Demo Only) ENTER চাপুন মেইন মেনুতে ফিরতে...")
        elif choice == "2":
            print("📶 ওয়াই-ফাই হ্যাকিং গাইড চালু হচ্ছে...")
            input("📖 (Demo Only) ENTER চাপুন মেইন মেনুতে ফিরতে...")
        elif choice == "3":
            print("📷 ক্যামেরা অ্যাক্সেস (ডামি) শুরু...")
            input("🕶️ (Demo Only) ENTER চাপুন মেইন মেনুতে ফিরতে...")
        elif choice == "4":
            print("🎙 মাইক্রোফোন মনিটর (ডামি) শুরু...")
            input("🎧 (Demo Only) ENTER চাপুন মেইন মেনুতে ফিরতে...")
        elif choice == "5":
            lk_mode()
        elif choice == "6":
            print("❌ টুল বন্ধ হচ্ছে...")
            break
        else:
            print("❗ভুল অপশন, আবার চেষ্টা করো!")
            time.sleep(1)

# LK Mode
def lk_mode():
    print("\n🔐 গোপন এলকে মোডে প্রবেশ...")
    print("LK Mahi ❤️ HK Miraj — মাফিয়া নয়, এক ভালোবাসার হ্যাকিং জুটি")
    while True:
        print("""
📱 ১. লোকেশন ট্র্যাকার
📶 ২. ওয়াই-ফাই হ্যাকিং গাইড
📷 ৩. ক্যামেরা অ্যাক্সেস (ডামি)
🎙 ৪. মাইক্রোফোন মনিটর (ডামি)
💬 ৫. এল কে মোড (লুকানো)
❌ ৬. এক্সিট
""")
        lk_choice = input("আপনার পছন্দ (1-6): ")

        if lk_choice == "1":
            print("🔍 লোকেশন ট্র্যাকার চালু হচ্ছে...")
            input("⏪ ENTER চাপুন LK Mode মেনুতে ফিরতে...")
        elif lk_choice == "2":
            print("📶 ওয়াই-ফাই হ্যাকিং গাইড চালু হচ্ছে...")
            input("⏪ ENTER চাপুন LK Mode মেনুতে ফিরতে...")
        elif lk_choice == "3":
            print("📷 ক্যামেরা অ্যাক্সেস (ডামি) শুরু...")
            input("⏪ ENTER চাপুন LK Mode মেনুতে ফিরতে...")
        elif lk_choice == "4":
            print("🎙 মাইক্রোফোন মনিটর (ডামি) শুরু...")
            input("⏪ ENTER চাপুন LK Mode মেনুতে ফিরতে...")
        elif lk_choice == "5":
            print("🔐 তুমি আগে থেকেই এলকে মোডে আছো 😎")
        elif lk_choice == "6":
            print("❌ এলকে মোড থেকে বের হচ্ছি...")
            break
        else:
            print("❗ভুল অপশন, আবার চেষ্টা করো!")

# Start the tool
main_menu()