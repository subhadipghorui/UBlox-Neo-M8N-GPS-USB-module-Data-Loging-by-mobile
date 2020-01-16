# Input TXT file path as string
path = input("Enter Log TXT File Name (log.txt): ")


# path = "test.txt"
# Enter the file path
myfile = open(path, encoding="cp437")

# Creating a new file and closed it
newFile = open("lat_lon_alt.csv", "w")
newFile.writelines("lat, lon, alt" + "\n")
newFile.close()
# Set the cursor to the 0 position
myfile.seek(0)
alt: float = 0
# Read line by line of the data
for db_set in myfile:
    # print(db_set)
     # fine the GNGGA data only
    # Check the string position and store in a variable
    gpgga = db_set.find("$GPGGA")
    gngga = db_set.find("$GNGGA")

    if (gpgga > -1 or gngga > -1):
        # print(db_set)
        # print(val1)
        data = db_set.split(',')
        lat = data[2]
        lon = data[4]
        alt1 = float(data[9])
        alt2 = float(data[11])
        alt = alt1 + alt2
        # print(lat, lon, alt1, alt2)
        # print(lat, lon, alt)

        # # Write to a new file
        newFile = open("lat_lon_alt.csv", "a")
        newFile.writelines(str(lat) + "," + str(lon) + "," + str(alt) + "\n")
        newFile.close()


print("Success")
print("Open lat_lon_alt.csv file.")