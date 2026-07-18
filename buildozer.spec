[app]
title = Calculator
package.name = calculator
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# ये बहुत ज़रूरी हैं
requirements = python3,kivy==2.2.1

orientation = portrait
fullscreen = 0
android.presplash_color = #FFFFFF
android.permissions = INTERNET

# ये वर्ज़न GitHub Actions के लिए बेस्ट हैं
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.ndk_api = 21

# आर्किटेक्चर (सिर्फ एक रखें ताकि बिल्ड जल्दी और सफल हो)
android.archs = arm64-v8a

# लाइसेंस ऑटो-एक्सेप्ट करने के लिए
android.accept_sdk_license = True

# सबसे ज़रूरी: एरर देखने के लिए लॉग लेवल 2 रखें
log_level = 2

[buildozer]
log_level = 2
warn_on_root = 1
