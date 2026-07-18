[app]
title = Calculator
package.name = calculator
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = assets/*
version = 0.1
requirements = python3,kivy==2.2.1
orientation = portrait
fullscreen = 0
android.presplash_color = #FFFFFF
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.ndk_api = 21
android.archs = arm64-v8a
android.accept_sdk_license = True
android.skip_update = False
log_level = 2

[buildozer]
log_level = 2
warn_on_root = 1

[p4a]
p4a.branch = develop
