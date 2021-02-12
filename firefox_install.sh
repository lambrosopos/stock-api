wget https://ftp.mozilla.org/pub/firefox/releases/51.0/linux-x86_64/en-US/firefox-51.0.tar.bz2
tar -xjf firefox-51.0.tar.bz2
rm -rf /opt/firefox50
mv firefox /opt/firefox51
mv /usr/bin/firefox /usr/bin/firefoxold
ln -s /opt/firefox51/firefox /usr/bin/firefox
