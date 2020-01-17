# Input TXT file path as string
path = input("Enter Log TXT File Name (log.txt): ")


# path = "test.txt"
# Enter the file path
myfile = open(path, encoding="cp437")


# Creating a new file and closed it
newFileName = path[0:-4]+"_latlon.csv"
newFile = open(newFileName, "w")
newFile.writelines("slno, lat, lon, alt" + "\n")
newFile.close()
# Set the cursor to the 0 position
myfile.seek(0)
alt: float = 0
slno: int = 0

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
        if(data[2] != "" and data[4] != "" ):
            latDeg = float(data[2][0:2])
            latMin = float(data[2][2:])/60
            lat = latDeg + latMin

            lonDeg = float(data[4][0:3])
            lonMin = float(data[4][3:])/60
            lon = lonDeg + lonMin

            alt1 = float(data[9])
            alt2 = float(data[11])
            alt = alt1 + alt2 
            # print(lat, lon)
            # print(latDeg,latMin, lonDeg, lonMin, alt1, alt2)
            slno+=1

            # Write to a new file
            newFile = open(newFileName, "a")
            newFile.writelines(str(slno)+","+str(lat) + "," + str(lon) + "," + str(alt) + "\n")
            newFile.close()


print("Success")
print("Open "+newFileName+" file.")