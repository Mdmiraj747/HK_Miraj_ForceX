import os

def main_menu():
    while True:
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
        print("""
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
        elif choice == "2":
            print("📶 ওয়াই-ফাই হ্যাকিং গাইড চালু হচ্ছে...")
        elif choice == "3":
            print("📷 ক্যামেরা অ্যাক্সেস (ডামি)...")
        elif choice == "4":
            print("🎙 মাইক্রোফোন মনিটর (ডামি)...")
        elif choice == "5":
            lk_mode()
        elif choice == "6":
            print("❌ টুল বন্ধ হচ্ছে...")
            break
        else:
            print("❗ ভুল অপশন, আবার দিন!")

        input("\n🔁 [Enter] চাপুন মেনুতে ফেরার জন্য...")

def lk_mode():
    while True:
        os.system("clear")
        print("\n🔐 গোপন এলকে মোডে প্রবেশ...")
        print("LK Mahi ❤️ HK Miraj — মাফিয়া নয়, এক ভালোবাসার হ্যাকিং জুটি\n")
        print("""
📱 ১. লোকেশন ট্র্যাকার
📶 ২. ওয়াই-ফাই হ্যাকিং গাইড
📷 ৩. ক্যামেরা অ্যাক্সেস (ডামি)
🎙 ৪. মাইক্রোফোন মনিটর (ডামি)
🔙 ৫. মূল মেনুতে ফিরুন
""")
        lk_choice = input("আপনার পছন্দ (1-5): ")

        if lk_choice == "1":
            print("🔍 লোকেশন ট্র্যাকার (LK Mode)...")
        elif lk_choice == "2":
            print("📶 WiFi Hack Guide (LK Mode)...")
        elif lk_choice == "3":
            print("📷 Dummy Camera Access...")
        elif lk_choice == "4":
            print("🎙 Dummy Microphone Monitor...")
        elif lk_choice == "5":
            break
        else:
            print("❗ ভুল অপশন!")

        input("\n🔁 [Enter] চাপুন LK মেনুতে ফেরার জন্য...")

if __name__ == "__main__":
    input("🔔 [ENTER] চাপলে টুল শুরু হবে...")
    main_menu()