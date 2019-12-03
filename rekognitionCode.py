import boto3

def detect_text(photo):

    client=boto3.client('rekognition')  # use rekognition

    response=client.detect_text(Image={'Bytes':photo})  #Call API for text_detection

    textDetections=response['TextDetections']   #extract detection text
    str = ''
    for text in textDetections:
        str = str + text['DetectedText'] + ' '      #combine the detected text into one long string.
    return (str)
