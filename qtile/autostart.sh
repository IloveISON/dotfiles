#!/bin/bash

# Set up dual monitors with xrandr
# xrandr --output HDMI1 --primary --brightness 0.56 --output eDP1 --auto --left-of HDMI1 
#

# xrandr --output HDMI1 --brightness 0.56

#Run single monitor
# xrandr --output eDP1 --brightness 0.8

# Terminate already running bar instances
killall -q polybar

### The Working Script for a single eDP1 display ### 
# polybar mybar 2>&1 | tee -a /tmp/polybar.log & disown


### The ChatGPT variant which doesn't work as expected ###
# while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done
#
# for m in $(polybar --list-monitors | cut -d":" -f1); do
# 	MONITOR=$m polybar --reload example &
# done

### The Arch Wiki variant ###
if type "xrandr"; then
	for m in $(xrandr --query | grep "connected" | cut -d" " -f1); do
		MONITOR=$m polybar --reload mybar &
	done
else
	polybar --reload mybar &
fi

echo "Polybar launched..."

### Start Dunst (notification manager)

dunst &
nitrogen --restore &
picom &
