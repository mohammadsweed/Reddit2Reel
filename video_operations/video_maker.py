import random
from moviepy.editor import (
    VideoFileClip,    # if you want to use a background video
    ImageClip,        # to use comment screenshots as video clips
    AudioFileClip,    # to add  audio to the video
    CompositeVideoClip,  # to layer images and video together
    concatenate_videoclips,  # to join multiple clips sequentially
)

class video_maker:


    def __init__(self,background_clip,screenshots,audio_clips):
        self.background_clip=background_clip
        self.screenshots = screenshots
        self.audio_clips = audio_clips




    def random_background_video_start(self,background_video):
      background_duration =background_video.duration
      reddit_video_length = sum(AudioFileClip(self.audio_clips[i]).duration for i in range(len(self.audio_clips)))
      # background_duration = max_start + reddit_video_length
      max_start = background_duration - reddit_video_length
      bg_start = random.uniform(0,max_start)
      return bg_start




    def make_video(self) :
      background_video =  VideoFileClip(self.background_clip).without_audio()

      bg_start = self.random_background_video_start(background_video)
      # data = sound and screenshot
      comment_data = []

      for i in range(len(self.screenshots)):

            comment_data.append({
                "Img": self.screenshots[i],
                "Audio": self.audio_clips[i]
            })
      #comment_data[-1:] → gets the last item as a list , comment_data[:-1] → gets everything except the last item:,I did this to make post_screenshot be first,used GPT
      comment_data = comment_data[-1:] + comment_data[:-1]
      clips = []

      # making this lists so to clean all of audio and image files later
      audio_objects = []
      img_objects = []


      for data in comment_data:
          audio = AudioFileClip(data['Audio'])

          audio_objects.append(audio)

          duration = audio.duration
                                                                                   # tiktok video size
          bg_clip = background_video.subclip(bg_start, bg_start + duration).resize(newsize=(1080,1920))

          # to make the backgorund video countinue and not be the same for all comments
          bg_start = bg_start + duration

          img_clip = ImageClip(data["Img"])\
                .set_duration(duration)\
                .set_position(("center", "center"))\
                .resize(width=1000)
          
          img_objects.append(img_clip)

          final_clip = CompositeVideoClip([bg_clip, img_clip]).set_audio(audio)
         # audio.close()

          clips.append(final_clip)


        # Concatenate all comment clips
      final_video = concatenate_videoclips(clips)

        # Export
      final_video.write_videofile("final_video/reddit_video.mp4", fps=30)


      # clean up everything

      final_video.close()
      del final_video

      background_video.close()
      del background_video

      for clip in clips:
        clip.close()
      del clips

      for audio in audio_objects:
        audio.close()
      del audio_objects

      for img in img_objects:
         img.close()
      del img_objects




