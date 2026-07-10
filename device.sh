#!/bin/bash

echo "Disconnecting old connections..."
adb disconnect

echo "Setting up connected device..."
adb tcpip 5555

echo "Waiting for device to initialize..."
sleep 3

# Get the IP address of the device
ipfull=$(adb shell ip -f inet addr show wlan0 | grep "inet " | awk '{print $2}')
ip=${ipfull%%/*}

echo "Connecting to device with IP $ip..."
adb connect "$ip"

# Optional: Force connect to a specific IP
DEVICE_IP="192.0.0.4"
ADB_PORT=5555

echo "Restarting ADB server..."
adb kill-server
adb start-server

echo "Connecting to $DEVICE_IP:$ADB_PORT..."
adb connect "$DEVICE_IP:$ADB_PORT"
