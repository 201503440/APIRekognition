
from flask import Flask, request
from flask_cors import CORS
import json
import boto3
import base64

app = Flask(__name__)
CORS(app)

client = boto3.client('rekognition',
                    aws_access_key_id=base64.b64decode("QUtJQVpJVEsyVVo3RkdWM1dVS1c=").decode("utf-8"),
                    aws_secret_access_key=base64.b64decode("YVlBcHRvaGdNMUk5azBObWlEZW9zaXVmeXZuTlVwMDVJbm9jMXY3aA==").decode("utf-8"),
                    region_name='us-east-2')

@app.route('/getLabels', methods=['GET', 'POST'])
def getLabels():    
    data = request.json
    photo = data['photo']
    bucket = data['bucket']
    try:
        response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}},MaxLabels=10)
        labels = []
        for label in response['Labels']:
            labels.append(label['Name'])
        return {"labels": labels}
    except:
        return {"status":400,"information":"Bad information."}

if __name__ == '__main__':    
    app.run(host = '0.0.0.0')
