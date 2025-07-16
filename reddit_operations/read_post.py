import praw
from dotenv import load_dotenv
import os

load_dotenv()

class read_post :


    def __init__(self, post_id,comments_num):
        
        self.post_id = post_id
        self.comments_num = comments_num

        self.reddit = praw.Reddit(
            client_id=os.getenv('client_id'),
            client_secret=os.getenv('client_secret'),
            user_agent= os.getenv('user_agent')
        )

        self.post = self.reddit.submission(id=self.post_id)
        self.post.comments.replace_more(limit=0)

        # top level mean comments that dirctly reply to the post and not to another comment , post.comments return this by default
                                    # assign only comments under 700 char using this loop
        self.top_level_comments = [comment for comment in self.post.comments if len(comment.body) < 700]
        self.top_comments = sorted(self.top_level_comments,key=lambda comment:comment.score , reverse=True)




    def get_title(self):
        # selftext is the body of the post
        return self.post.title+ '\n\n'+ self.post.selftext


    # this method is needed for screenshoting
    def get_authors(self) :
        # authors are the commenters names
        authors_name = []

        for i in range(self.comments_num):
            comment = self.top_comments[i]


            if comment.author is not None and comment.author.name :
                 authors_name.append(comment.author.name)

        return authors_name


    # this method is needed for text to voice
    def get_comments(self) :
        comments = []

        for i in range(self.comments_num):
            comments.append(self.top_comments[i].body)

        return comments






