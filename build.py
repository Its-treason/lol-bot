import os
from time import time
from base64 import b64encode
from os import urandom

print('Building LOL-BOT and TFT-BOT...')
startTime = int(time())

# Create build.ini
checksum = str(b64encode(urandom(18)).decode('utf-8'))
version = 'v' + input('Enter version: ')
conf = """
[build]
buildNumber=%s
version=%s
""" % (checksum, version)
if not os.path.isdir('tft-bot/build'):
    os.mkdir('tft-bot/build')
f = open('tft-bot/build/build.ini', 'w')
f.write(conf)
f.close()
if not os.path.isdir('lol-bot/build'):
    os.mkdir('lol-bot/build')
f = open('lol-bot/build/build.ini', 'w')
f.write(conf)
f.close()


print("""
=====================================
    START OF TFT-BOT BUILD OUTPUT
=====================================
""")

os.chdir('./tft-bot')
os.system("""
pyinstaller
    --onefile ./main.py
    --target-architecture x86_64
    --console
    --clean
    --noconfirm
    --log-level DEBUG
    --collect-all cv2
    -i tft-bot.ico
    --add-data ./images/*;images
    --add-data ./images/champions/*.png;images/champions
    --add-data ./build/*.ini;build
    --hidden-import cv2
""".replace('\n', ' '))
os.chdir('..')

print("""
=====================================
    END OF TFT-BOT BUILD OUTPUT
=====================================
""")

print("""
=====================================
    START OF LOL-BOT BUILD OUTPUT
=====================================
""")

os.chdir('./lol-bot')
os.system("""
pyinstaller
    --onefile ./main.py
    --target-architecture x86_64
    --console
    --clean
    --noconfirm
    --log-level DEBUG
    --collect-all cv2
    -i lol-bot.ico
    --add-data ./images/*;images
    --add-data ./build/*.ini;build
    --hidden-import cv2
""".replace('\n', ' '))
os.chdir('..')

print("""
=====================================
    END OF LOL-BOT BUILD OUTPUT
=====================================
""")

# Copy Executables
if not os.path.isdir('./dist'):
    os.mkdir('./dist')

os.replace('./tft-bot/dist/main.exe', './dist/tft-bot__%s.exe' % version)
os.replace('./lol-bot/dist/main.exe', './dist/lol-bot__%s.exe' % version)

# CleanUp
# Do not delete build folder to make debugging the build easier
os.rmdir('tft-bot/dist')
os.remove('tft-bot/main.spec')
os.remove('tft-bot/build/build.ini')
os.rmdir('lol-bot/dist')
os.remove('lol-bot/main.spec')
os.remove('lol-bot/build/build.ini')

buildTime = str(int(time()) - startTime)
print("""
Finished build, took %s seconds!

== Build variables ==
Version        : %s
Build-Checksum : %s
== Build variables ==
""" % (buildTime, version, checksum))
