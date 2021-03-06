import os
from google.cloud import texttospeech
from google.cloud import texttospeech_v1

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'namegrabz-gcp-be3ef8eb02c4.json'
client = texttospeech_v1.TextToSpeechClient()

names = open("random_500_names.txt").read().lower().splitlines()
#names[0] = names[0][3:]
print(names)
gender = ['MALE', 'FEMALE']
count = 3
for sex in gender:
    count += 1
# For loop that goes through the names
    for name in names:
        file_name = "Voices/"+ str(count) +"/" + name + ".mp3"
        synthesis_input = texttospeech_v1.SynthesisInput(text= name)
        if sex == 'MALE':
            voice = texttospeech_v1.VoiceSelectionParams(language_code='en-in',ssml_gender=texttospeech_v1.SsmlVoiceGender.MALE)
        else:
            voice = texttospeech_v1.VoiceSelectionParams(language_code = 'en-in' , ssml_gender= texttospeech_v1.SsmlVoiceGender.FEMALE)
        print(client.list_voices)
        audio_config = texttospeech_v1.AudioConfig(audio_encoding=texttospeech_v1.AudioEncoding.MP3)

        response1 = client.synthesize_speech(input=synthesis_input, voice= voice, audio_config=audio_config)

        with open(file_name, 'wb') as output:
            output.write(response1.audio_content)




