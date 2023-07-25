@echo off
cls
echo ::
echo [101;93m Open 192.168.1.35:5000 in a device with blutooth, and connected to this computer through wifi [0m
echo ::

flask --app server run --host=0.0.0.0

