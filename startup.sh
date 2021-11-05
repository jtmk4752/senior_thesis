#!/bin/sh

#http://www.neko.ne.jp/~freewing/raspberry_pi/nvidia_jetson_nano_cron_crontab_autoexec_script/

#jetson nano用。crontabに追加。setup.shでセットアップするのも良い
sleep 5
sudo nvpmodel -m 0
sleep 5
sudo jetson_clocks