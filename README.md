# PiTempMonitor - Run Python Applications On A Raspberry Pi 24/7

PiTempMonitor is a project that demonstrates how to run a Python application continuously on a Raspberry Pi using `systemd`. The python script runs the `vcgencmd measure_temp` terminal command every 10 seconds and measures the Raspberry Pi temperature.

Note that the following process I am explaining is done on Raspberry Pi 64-bit OS Lite, but I am assuming it would work in any other similar versions.

## Installation

Open terminal and SSH into your Raspberry Pi. Then you would want to install Git if you haven't already.

```bash
sudo apt update
sudo apt install git -y
```

## Cloning The Repo

Copy the HTTPS of the repository `https://github.com/kevinde3ngineer/PiTempMonitor.git` and use the following command to clone the repository into your Raspberry Pi.

```bash
git clone https://github.com/kevinde3ngineer/PiTempMonitor.git
```

The repository should be located in `/home/your_username/PiTempMonitor` and the script in the repository should be located in `/home/your_username/PiTempMonitor/temp_bot.py`

## Testing

Now that you have the repo, check whether the python script works or not.

Enter the repo folder:
```bash
cd ~/PiTempMonitor
```

Comfirm the script file exist by checking for `temp_bot.py`:
```bash
ls
```

Test the script:
```bash
python3 temp_bot.py
```

## Create The Systemd

```bash
sudo nano /etc/systemd/system/pitempmonitor.service
```
- `sudo` - run as administrator
- `nano` - open the terminal text editor
- `/etc/systemmd/system` - where the custom system services live
- `pitempmonitor.service` - name of our service

## Create The Service File

After you entered the terminal command above you will need to write the service file for it.

Remember to change the info to your own info (ex. `your_username`)

```bash
[Unit]
Description=PiTempMonitor Python Script
After=multi-user.target

[Service]
User=your_username
WorkingDirectory=/home/your_username/PiTempMonitor
ExecStart=/usr/bin/python3 /home/your_username/PiTempMonitor/temp_bot.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```
- `Description` is the label for the service
- `After=multi-user.target` tells systemd to wait until the PI is at the normal boot stage before starting the script
- `User=your_username` run the script under your account (remember to change "your_username" with your actual info)
- `WorkingDirectory=/home/your_username/PiTempMonitor` brings us in the Temp_Notifier section (basically auto running `cd ~/Temp_Notifier`)
- `ExecStart=/usr/bin/python3 /home/your_username/PiTempMonitor/temp_bot.py` is the actual command systemd runs
- `Restart=always` is for if the script crashes or exits, systemd should start it again
- `RestartSec=5` is my arbitrary number for waiting before restarting it
- `WantedBy=multi-user.target` allows the service to be enabled so it starts during normal boot

To Save and Exit Nano: `Ctrl+O` to save, `Enter` to save file, and `Ctrl+X` to exit.

## Reload Systemd

Now you have tell systemd to reload its service definitions.

```bash
sudo systemctl daemon-reload
```

## Start Service

 Enable the service for startup on boot:
 ```bash
sudo systemctl enable pitempmonitor.service
```

Start the service:
``` bash
sudo systemctl start pitempmonitor.service
```

## Commands

To check that the service is running:
```bash
sudo systemctl status pitempmonitor.service
```

Watch the live output/logs:
```bash
journalctl -u pitempmonitor.service -f
```

Disable the service: (stops it from auto-starting on boot)
```bash
sudo systemctl disable pitempmonitor.service
```

Stop the service: (stops the service right now)
```bash
sudo systemctl stop pitempmonitor.service
```

Restart the service:
```bash
sudo systemctl restart pitempmonitor.service
```

How to delete the service: (Warning)
```bash
sudo systemctl stop pitempmonitor.service
sudo systemctl disable pitempmonitor.service
sudo rm /etc/systemd/system/pitempmonitor.service
sudo systemctl daemon-reload
```

## Note From Dev

Special thanks to @stuffman0001 for verifying the process. Note that `README.md` may have typos, but I tried my best to check. This project demonstrates how to run python applications countinously on a Raspberry Pi. You can obviously now make your own iteration with your own python application.




















