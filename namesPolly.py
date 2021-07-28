import boto3

polly = boto3.client('polly')

names = open("random_125_names.txt").read().lower().splitlines()
names[0] = names[0][3:]
print(names)


def play_sound(text):
    for text in names:
        response = polly.synthesize_speech(Text= text, VoiceId= 'Matthew', OutputFormat='mp3')
        body = response['AudioStream'].read()
        file_name= text + '-1.mp3'

        with open(file_name,'wb') as file:
            file.write(body)
            file.close()

if __name__ == '__main__':
    play_sound(names[4])



