#!/usr/bin/python3
import requests
from requests.exceptions import HTTPError
from zipfile import ZipFile
from datetime import timedelta, date
import pdb

#----------------------------#
# Define timeframe
#----------------------------#
start_date = date(2020, 7, 12)
end_date = date(2020, 7, 18)
delta = timedelta(days=1)

#----------------------------#
# Method to download data
#----------------------------#
def zipfile_download(date):
    print(date.strftime("%Y-%m-%d"))
    # URL of remote zipped file
    zipurl = "https://archives.nseindia.com/content/historical/EQUITIES/" \
             + date.strftime("%Y") + "/" + date.strftime("%b").upper() \
             + "/cm" + date.strftime("%d") + date.strftime("%b").upper() \
             + date.strftime("%Y") + "bhav.csv.zip"
    #zipurl = "https://www.bseindia.com/download/BhavCopy/Equity/EQ_ISINCODE_" \
    #         + date.strftime("%d%m%y") + ".zip"
    print(zipurl)

    # Download the file from the URL
    print("Start Get")
    resp = requests.get(zipurl)
    pdb.set_trace()
    print("End Get")

    print(resp.raise_for_status())

    try:
        print("Request status code:", resp.status_code)
        #print(resp.raise_for_status())
    except requests.ConnectionError:
        print('No connection, retrying')
    except HTTPError as http_err:
        # Return code error (e.g. 404, 501, ...)
        # ...
        print('HTTP error occurred: {http_err}')
        print('HTTPError: Could not download', resp.url)
    except Exception as err:
        print('Other error occurred: {err}')
        print('Exception: Could not download', resp.url)
    else:
        # 200
        # ...
        print (resp.url, 'downloaded successfully')
        #print ('downloaded successfully')

        # Create a new file on the hard drive
        tempzip = open("/Users/admin/workspace/qtapps/pythondownloader/tmp/tempfile.zip", "wb")

        # Write the contents of the downloaded file into the new file
        tempzip.write(resp.content)

        # Close the newly-created file
        tempzip.close()

        # Re-open the newly-created file with ZipFile()
        zf = ZipFile("/Users/admin/workspace/qtapps/pythondownloader/tmp/tempfile.zip")

        # Extract its contents into <extraction_path>
        # note that extractall will automatically create the path
        zf.extractall(path = '/Users/admin/workspace/qtapps/pythondownloader/tmp')

        # close the ZipFile instance
        zf.close()


#----------------------------#
# Start loop
#----------------------------#
while start_date <= end_date:
    print("Go inside func")
    zipfile_download (start_date)
    print("Came back from func")
    start_date += delta
