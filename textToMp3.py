from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import TextToSpeechV1
url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/f104b76e-d9e4-4082-b6bc-19b5070eb263'
apikey = 'fxYviIRDMsxq61Mdn0VDvj_fw8_mo3Ajl1mhjHZl1CNW'


def main():

    # Setup Service
    authenticator = IAMAuthenticator(apikey)
    # New TTS Service
    tts = TextToSpeechV1(authenticator=authenticator)
    # Set Service URL
    tts.set_service_url(url)

    with open('text.txt', 'r') as f:
        text = f.read()

    with open('voice.mp3', 'wb') as audio_file:
        res = tts.synthesize(text, accept='audio/mp3',
                             voice='en-US_AllisonV3Voice').get_result()
        audio_file.write(res.content)


if __name__ == "__main__":
    main()
