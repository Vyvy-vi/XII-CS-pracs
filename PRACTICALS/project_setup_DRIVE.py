# SHORT NOTE: DRIVE OR LOCAL ENVIRONMENT FILES
"""
THE FILE HANDLING PRATICALS ARE MADE SUCH THAT THEY CONECT TO DRIVE AND FETCH FILES TO EDIT THERE.
OPEN THIS LINK TO PUT FILES IN YOUR DRIVE AND THEN PRESS 'RUN': <https://drive.google.com/drive/folders/1nzMxxm6CLGGUvpH2NSKIDoJnl1zbBlUe?usp=sharing>
FOR FULLY EXECUTING THESE, IT WILL BE SUGGESTED TO MOUNT YOUR DRIVE ONTO HERE.
*if you are not comfortable doing this, you may alternatively do the following:

ALTERNATIVELY, YOU CAN RUN THE NEXT SCRIPT BELOW INSTEAD OF THIS ONE TO GENERATE ALL REQUSITE FILES RIGHT HERE.
<Check next script titled FILE GENERATOR>

#TODO: get it to sync with a global drive account
"""
from google.colab import drive
import requests
drive.mount('/content/drive', force_remount=True)

file_url = ""
r = requests.get(file_url, stream=True)
drive.unmount()
with open("/content/drive/My Drive/python.pdf", "wb") as file:
    for block in r.iter_content(chunk_size=1024):
        if block:
            file.write(block)
