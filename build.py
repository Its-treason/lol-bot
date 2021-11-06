import os
from time import time

print('Building LOL-BOT and TFT-BOT...')
startTime = int(time())

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
    --log-level WARN
    --collect-all cv2
    -i tft-bot.ico
    --add-data ./images/*.png;images
    --add-data ./images/champions/*.png;images/champions
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
    --log-level WARN
    --collect-all cv2
    -i lol-bot.ico
    --add-data ./images/*.png;images
""".replace('\n', ' '))
os.chdir('..')

print("""
=====================================
    END OF LOL-BOT BUILD OUTPUT
=====================================
""")

if not os.path.isdir('./dist'):
    os.mkdir('./dist')

os.replace('./tft-bot/dist/main.exe', './dist/tft-bot.exe')
os.replace('./lol-bot/dist/main.exe', './dist/lol-bot.exe')

print('Finished build, took ' + str(int(time()) - startTime) + ' seconds')
