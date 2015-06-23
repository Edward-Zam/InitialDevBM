This folder is for storing configuration files. Please append when inserting new files.

-hostapd.conf: The configuration file for hostapd. This setup is for the access point if no network is detected. Default SSID is
BlueMarbleIrr and the password is set to Testpass1. WPA-PSK is used. Location /etc/hostapd/hostapd.conf

-rc.local: This is the setup for checking the connectivity on boot and performing the appropriate action. Current version connnects to 
home SSID if in range and correct credientials. If not then it launches as an access point with the configuration of hostapd.conf.
Location /etc/rc.local

-udhcpd: Enables the uDHCPd server. Location /etc/default/udhcpd

-udhcpd.conf: Configures udhcpd, the bit that hands out IP addresses. Location /etc/udhcpd.conf

-RemoveOnBoot: This file shows the commands needed to prevent hostapd and udhcpd from running on boot and preventing the device
from connecting to other wireless networks automatically
