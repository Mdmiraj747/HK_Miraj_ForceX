# HK_Miraj_ForceX Tool
# Educational Ethical Hacking UI by HK Miraj ❤️ Powered by LK Mahi

import os
import time

def banner():
    print("\n")
    print("█▀█ █▄░█   █▀▄ █ █▀▀ █▀█ █▀▄")
    print("█▄█ █░▀█   █▄▀ █ █▄▄ █▄█ █▄▀")
    print("HK_Miraj_ForceX — Official Tool")
    print("Powered by LK Mahi ❤️\n")
    time.sleep(1)

def main_menu():
    print("📱 ১. লোকেশন ট্র্যাকার")
    print("📶 ২. ওয়াই-ফাই হ্যাকিং গাইড")
    print("📷 ৩. ক্যামেরা অ্যাক্সেস (ডামি)")
    print("🎙 ৪. মাইক্রোফোন মনিটর (ডামি)")
    print("💬 ৫. এল কে মোড (লুকানো)")
    print("❌ ৬. এক্সিট\n")

def run():
    os.system('clear')
    banner()
    while True:
        main_menu()
        choice = input("আপনার পছন্দ (1-6): ")

        if choice == '1':
            print("\n[+] Seeker + Ngrok ব্যবহার করে লোকেশন ট্র্যাক করার নির্দেশনা চালু হচ্ছে...")
            print("[!] দয়া করে বন্ধু বা অনুমতি ছাড়া ব্যবহার করবেন না!")
            time.sleep(2)

        elif choice == '2':
            print("\n[+] Wi-Fi হ্যাকিং এর বাংলা গাইড:")
            print("    ১. WiFi Adapter লাগবে")
            print("    ২. Monitor Mode চালু করুন")
            print("    ৩. Airodump-ng দিয়ে স্ক্যান করুন\n")
            time.sleep(3)

        elif choice == '3':
            print("\n📷 Dummy Camera Access চালু ✅ (শিক্ষামূলক)")
            time.sleep(2)

        elif choice == '4':
            print("\n🎙 Dummy Microphone Monitor চালু ✅ (শিক্ষামূলক)")
            time.sleep(2)

        elif choice == '5':
            print("\n🔐 গোপন এলকে মোডে প্রবেশ...")
            print("LK Mahi ❤️ HK Miraj — মাফিয়া নয়, এক ভালোবাসার হ্যাকিং জুটি")
            time.sleep(2)

        elif choice == '6':
            print("\nবিদায় জান পাখি 💔")
            break

        else:
            print("\n[!] ভুল অপশন, আবার চেষ্টা করুন!")
            time.sleep(1)

if __name__ == '__main__':
    run()