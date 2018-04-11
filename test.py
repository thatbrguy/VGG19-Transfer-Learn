import requests
import json
import os
import glob
from requests.auth import HTTPBasicAuth

word2idx = {'cat': 0, 'lion': 1, 'tiger': 2, 'leopard': 3}
dirs = ['cat', 'lion', 'tiger', 'leopard']

correct = 0

for i, dir_ in enumerate(dirs):

    files = glob.glob(os.path.join('data','test',dir_,'*.jpg'))
    for j, file in enumerate(files):

        print('Dir:', dir_, 'File:', j, end = '\r')
        data = {
            "file":open(file, "rb"), \
            "modelId":("", "29c6b06e-7799-4654-a89a-111b00babfb9") #REPLACE WITH YOUR MODEL ID
        }

        headers = {
            'accept': 'multipart/form-data'
        }


        url = "https://app.nanonets.com/api/v2/ImageCategorization/LabelFile/"
        r = requests.post(url, headers=headers, files=data, auth=HTTPBasicAuth('_ftBUD6YTZoLDGjiyxI18p21F3fRvkr7UI_9y-ERQNV', ''))

        output = json.loads(r.content.decode())
        predictions = output['result'][0]['prediction']

        high = 0
        argmax_label = ''
        for label in predictions:
            if label['probability'] > high :
                argmax_label = label['label']

        if(word2idx[argmax_label] == i):
            correct+=1

print('Test Accuracy = ', correct/200)