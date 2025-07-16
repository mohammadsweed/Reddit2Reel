from playwright.sync_api import sync_playwright



class screenshot_post:

    def __init__(self,post_id,authors):
         self.post_id = post_id
         self.authors = authors

    # this function uses javascript to hide replies , i used GPT
    def hide_replies(self,page):

         page.eval_on_selector_all(
    'shreddit-comment shreddit-comment',
    '''elements => elements.forEach(el => el.style.display = "none")'''
)




    def screenshot(self) :

         with sync_playwright() as playwright:
                self.user_data_dir = "C:/Users/moham/playwright_chrome_profile"
                self.browser = playwright.chromium.launch_persistent_context(
                    user_data_dir=self.user_data_dir,
                    headless=False,

                )


                for p in self.browser.pages:
                    p.close()


                page = self.browser.new_page()
                page.goto(f'https://www.reddit.com/r/AskReddit/comments/{self.post_id}/',wait_until="domcontentloaded")
                post_box=page.locator('shreddit-post')
                post_box.screenshot(path='assets/screenshots/post_title.png')




                for i in range(len(self.authors)):

                    author = self.authors[i]

                    # Click "More replies" buttons if needed
                    while page.locator('text="More Replies"').count() > 0:
                        page.locator('text="More Replies"').first.click()
                        page.wait_for_timeout(500)  # Let DOM update


                    self.hide_replies(page)



                    comment_box = page.locator(f'shreddit-comment[author="{author}"]')
                    comment_box.scroll_into_view_if_needed()

                    self.hide_replies(page)


                    # use this so the comment doesn't get hidden by the searchbar, i used GPT
                    comment_box.evaluate("""
                                    (element) => {
                                        const rect = element.getBoundingClientRect();
                                        window.scrollBy({ top: rect.top - 100, behavior: 'instant' });
                                    }
                                """, comment_box)

                    comment_box.screenshot(path=f'assets/screenshots/comment_{i+1}.png' , )
                    print(f'screenshot_{i+1} Saved ✅')


                self.browser.close()




