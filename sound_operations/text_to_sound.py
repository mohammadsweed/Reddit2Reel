from gtts import gTTS
import random



class text_to_sound :

    def __init__(self,post_title,post_comments):

        self.post_title = post_title
        self.post_comments= post_comments
        self.accents = ['com.au', 'co.uk','us','ca','ie',] # com.au = Australlia , ca = canada , ie = ireland


    def convert_to_sound(self):
        accent = random.choice(self.accents)

        speech = gTTS( text=self.post_title,lang='en',tld=accent)
        speech.save(f'assets/sound/post_title.mp3')

        for i, comment in enumerate(self.post_comments,1):
            accent = random.choice(self.accents)
            speech = gTTS( text=comment,lang='en',tld=accent)
            speech.save(f'assets/sound/comment_{i}.mp3')
            print(f'comment_{i} sound saved ✅')





