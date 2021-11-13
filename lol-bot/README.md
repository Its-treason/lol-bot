# LoL-Bot

Autoplay Coop-Vs-Ai games to level an account

## Setup

### Creating the binary from source

> These steps are only if you want to build the binary from source. If you already have a binary you can skip this step

Install all required packages

````bash
pip install -r requirements.txt
````

Start the build

````
python ./build.py
````

When asked, enter a version for the build. You may leave the version emtpy

The binary will be placed in the dist folder, with the naming scheme `lol-bot__v[Version Name].exe`

### Game settings

Make sure to set the following settings. The bot will not work without them

> The default settings are used for base settings, for best result you might want to reset all settings to default

> You can set the settings easily in the practice tool

- Set your clients and games language to english
- `Hotkeys` > `Player Movement` > `Player Attack Move Click`: Must be set to `A`
- `Video` > `Resolution`: Should be set to `1280x800`, other values may also work
- `Video` > `Window Mode`: Must be set to `Windowed` or `Borderless`
- `Interface` > `HUD Scale`: Must be set to `100`
- `Interface` > `Minimap Scale`: Must be set to `50`
- `Game` > `Auto attack`: Should be activated

### Starting the bot

Before starting the bot u must enter a Coop-Vs-Ai lobby with Intro difficulty. 
The bot will take over the mouse and focus the Client / Game aggressively.
After starting the bot you can exit by pressing `Ctrl` + `C` while the bots window is in focus.
