import boto3
import os

polly = boto3.client('polly')

names = open("random_125_names.txt").read().lower().splitlines()
names[0] = names[0][3:]
print(names)


def play_sound(text):
    for text in names:
        file_name = 'Voices/2/' + text + '.mp3'
        if os.path.exists(file_name):
            print("File " + file_name + " already exists")
        else:
            response = polly.synthesize_speech(Text=text, VoiceId='Kimberly', OutputFormat='mp3')
            body = response['AudioStream'].read()

            with open(file_name, 'wb') as file:
                print(file_name)
                file.write(body)
                file.close()


if __name__ == '__main__':
    play_sound(names[4])
