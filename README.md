# 🎬 Reddit2Reel: Automated Video & Reel Generator

> **Reddit2Reel** is a fully automated Python bot that converts Reddit posts into ready-to-publish vertical videos (TikTok, Instagram Reels, YouTube Shorts). The bot handles the entire pipeline—from scraping Reddit posts and synthesizing Text-to-Speech (TTS), to rendering the video with background gameplay and automatically uploading it to Instagram.

---

## 🌟 Features

* **Reddit Scraping:** Automatically fetches the top comments and post content using the PRAW (Python Reddit API Wrapper).
* **Automated Screenshots:** Captures high-quality screenshots of the Reddit thread using browser automation.
* **Text-to-Speech (TTS):** Converts post titles and comments into natural-sounding voiceovers.
* **Video Compositing:** Dynamically stitches together background gameplay footage (e.g., Minecraft Parkour), TTS audio, and screenshots to create engaging vertical videos.


---

## 📸 Demo

Check out the final product! This is a complete vertical video generated entirely by the bot, from scraping the text to overlaying TTS audio on gameplay footage:

<p align="center">
  <img src="assets/demo.gif" width="350" />
</p>

👉 **[Click here to watch the full HD Demo Video](assets/demo.mp4)**

---

## 🛠️ Tech Stack & Libraries

This project leverages a combination of web scraping, audio processing, and video editing libraries to fully automate content creation:

* **Python 3** - Core programming language.
* **PRAW** - For authenticated interaction with the Reddit API.
* **Playwright** - For headless browser automation (navigating Reddit and capturing high-quality UI screenshots of the threads).
* **MoviePy** - For video and audio compositing (stitching clips, overlaying audio, and rendering the final mp4).
* **python-dotenv** - For secure management of API credentials.

---

## 🤝 My Role

This was a **100% Solo Project**. I designed and implemented the entire pipeline from scratch, navigating the complexities of video rendering, programmatic audio-syncing, and browser automation to create a fully hands-off content generation machine.

---

## 🚀 How It Works

1. **Input:** The script prompts for a specific Reddit post ID and the number of comments to feature.
2. **Scraping:** It extracts the title, authors, and comment bodies directly from Reddit.
3. **Media Generation:** The bot automatically navigates to the post, captures screenshots of the thread, and generates corresponding TTS audio files.
4. **Rendering:** It overlays the screenshots and audio onto a background video, timing everything perfectly.

