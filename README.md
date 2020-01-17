# UBolx Neo M8N GPS Data Logger by Python
    To get data from Ublox Neom8n USB Module - 
**Step 1:**
You Need a OTG to Connect USB cable to mobile.

**Step 2:**
Download **SerialUSBTerminal** from Google Playstore.
Connect the module to mobile by OTG.
https://play.google.com/store/apps/details?id=de.kai_morich.serial_usb_terminal&hl=en

**Step 3:**
Open it. Go to **Option** (top-left) -> **USB Devices** -> refresh if not show. -> Click on **device**.

If it didn't work -> Long press it to open options -> Edit -> Select the Driver (Use CDC or CP210x)-> It will start logging.
If not Worked.
Try other option to get data.

**Step 4:**
To save logging data click -> : on the top right -> **Data** -> Click **Log** -> The data will start recording to a text file. -> Then Click log **again**


# UBolx Neo M8N GPS Data Logger by Python
This is a python code for extracting **GNGGA** and **GPGGA** NMEA data -- co-ordinate and alititude from log text file

**Step 1:**
Convert your gps nmea log data to text file (.txt).

**Step 2:**
Copy the file to the same directory the programme belong.

**Step 3:**
Check if you have python 3.7 install.
open cmd or any terminal in the directory.
type---------- py logUbloxm8n.py

**Step 4:**
Enter file name: log.txt

CHECK the directory and open **lat_lon.csv** for co-ordinate data.

After Runnig this file it will generate a lat_lon_alt.csv file. Which contain latitude, longitude and altitude.