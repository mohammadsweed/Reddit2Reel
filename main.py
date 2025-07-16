import glob
import subprocess
from reddit_operations.read_post import read_post
from reddit_operations.screenshot_post import screenshot_post
from sound_operations.text_to_sound import text_to_sound
from video_operations.video_maker import video_maker

background_video_path = r"C:\Users\moham\Downloads\13 Minutes Minecraft Parkour.mp4"

post_id = input('Enter the post id: ')
comments_num = int(input('Enter the comments num: '))


post = read_post(post_id , comments_num)
print('Reading post...')

post_title = post.get_title()
post_comments = post.get_comments()
comments_authors = post.get_authors()

screenshot_everything = screenshot_post(post_id,comments_authors)
screenshot_everything.screenshot()

sound_converter = text_to_sound(post_title, post_comments)
sound_converter.convert_to_sound()

# This gets all PNG and mp3 files in the folder and stores its path in a list
screenshots = glob.glob("assets/screenshots/*.png")
audio_files = glob.glob("assets/sound/*.mp3")

video = video_maker(background_video_path,screenshots,audio_files)
video.make_video()




#1mctlj7 559
#1mdhyil
#1mdto7d 2531


