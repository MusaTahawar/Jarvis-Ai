#here i imported some modules

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time
import requests
from bs4 import BeautifulSoup
import smtplib
import python_weather
import asyncio
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
NEWS_API_KEY = 'YOUR_NEWS_API_KEY'


apps = ["youtube","facebook","twitter","aware international","musa tahawar","netflix","chrome","google"]

email_dict = {"USER_NAME":"YOUR_MAIL",
              "USER_NAME":"YOUR_MAIL",
              "USER_NAME":"YOUR_MAIL",
              "USER_NAME":"YOUR_MAIL"
              }

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty("voice", voices[0].id)

print("We are still working on this")


# Function to play a song on YouTube using Selenium

def playSongOnYouTube(query):
    # Initialize Chrome WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Maximize the Chrome window
    driver = webdriver.Chrome(options=options)

    # Open YouTube and search for the query
    driver.get("https://www.youtube.com")
    search_box = driver.find_element_by_name("search_query")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    # Wait for a moment to load search results
    time.sleep(2)

    # Click on the first video in the search results
    video_link = driver.find_element_by_id("video-title")
    video_link.click()

    # Close the WebDriver when the video starts playing
    time.sleep(5)  # Adjust this time based on your internet speed
    driver.quit()

    if "play a song" in query:
        speak("What song would you like to listen to on YouTube?")
        search_query = takeCommand()
        speak(f"Playing {search_query} on YouTube")
        playSongOnYouTube(search_query)

def speak(audio):
    '''this function is used for ai to speak'''
    engine.say(audio)
    engine.runAndWait()

def wishme():
    '''this function will greet you'''
    hour = int(datetime.datetime.now().hour)


    if hour >= 0 and hour<12:
        speak("good morning")

    elif hour>=12 and hour<18:
        speak("good afternoon")

    else:
        speak("good evening")
    speak("I am Jarvis Assistamt, Please tell me how may i help you")

def takeCommand():
    '''this function will take command from you'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query} \n")

    except Exception as e:
        print("Say that again please")
        return "None"

    return query
def sendEmail(to, content):
    server = smtplib.SMTP("smntp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("YOUR_EMAIL", "YOUR_PASSWORD")
    server.sendmail("YOUR_MAIL", to, content)
    server.close()

def search_google(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)

def get_google_answer(query):
    search_google(query)
    response = requests.get(f"https://www.google.com/search?q={query}")
    soup = BeautifulSoup(response.text, "html.parser")
    answer_div = soup.find("div", class_="BNeawe iBp4i AP7Wnd")

    if answer_div:
        answer = answer_div.get_text()
        return answer

    else:
        return "I couldn't find an answer for your query."
def open_website(query):
    search_google(query)
    response = requests.get(f"https://www.google.com/search?q={query}")

def get_weather_info(city):
    # Replace 'YOUR_API_KEY' with your actual API key
    weather = python_weather.Client(format=python_weather.Metric, apikey='YOUR_API_KEY')


    try:
        response = weather.find(city)
        current_weather = response.current
        temperature = current_weather.temperature
        description = current_weather.sky_text

        weather_info = f"The current weather in {city} is {description} with a temperature of {temperature} degrees Celsius."
        speak(weather_info)
    except Exception as e:
        speak("Sorry, I couldn't retrieve the weather information at the moment.")

def get_and_read_news():
    try:
        news_url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
        response = requests.get(news_url)
        news_data = response.json()

        if news_data['status'] == 'ok':
            articles = news_data['articles']
            for index, article in enumerate(articles):
                title = article['title']
                description = article['description']
                source = article['source']['name']
                news_info = f"News {index + 1}: {title}. {description}. Source: {source}."
                speak(news_info)

        else:
            speak("Sorry, I couldn't retrieve the news at the moment.")

    except Exception as e:
        speak("Sorry, I couldn't retrieve the news at the moment.")

if __name__ == "__main__":
    wishme()

    while True:
        query = takeCommand().lower()
        
        if "wikipedia" in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia, """)
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

            pass
        elif "hi" in query or "hello" in query:
            speak("Hello How may i assist you?")
            print("Hello How may i assist you?")
        elif "tell me the news" in query:
            speak("Sure, here are the latest news headlines.")
            get_and_read_news()
        elif "who are you" in query:
            speak("My name is kinzond i am a AI assistant i am here to help you")
            print("My name is Kinzond I am an AI assistant I am here to help you")

        elif "what is your name" in query:
            speak("My name is Kinzond")
            print("My name is Kinzond")

        elif "play cupid" in query:
            speak("Playing Cupid")
            print("Playing Cupid")
            webbrowser.open("https://youtu.be/Qc7_zRjH808?si=YIpH-D4vjS7ZaNBP")

        elif "Play a song" in query:
            speak("What song you want to listen?")
            search_query = takeCommand()
            search_url = f"https://www.youtube.com/results?search_query={search_query}"
            speak(f"Playing {search_query}")
            webbrowser.open(search_url)

        elif "open youtube" in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")

        elif "open facebook" in query:
            speak("Opening Facebook")
            webbrowser.open("facebook.com")

        elif "open aware international" in query:
            speak("Opening Aware international")
            webbrowser.open("awareinternational.net")

        elif "open instagram" in query:
            speak("Opening Instagram")
            webbrowser.open("instagram.com")

        elif "open twitter " in query:
            speak("Opening Twitter")
            webbrowser.open("twitter.com")

        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif "open bing" in query:
            speak("Opening Bing")
            webbrowser.open("bing.com")

        elif "open Musa Tahawar" in query:
            speak("Opening Musa Tahawar Website")
            webbrowser.open("musatahawar.epizy.com")

        elif "open sales Dash" in query:
            speak("Opening Salesdash")
            webbrowser.open("https://salesdashcrm.com/")

        elif "open netflix" in query:
            speak("Opening Netflix")
            webbrowser.open("netflix.com")

        elif "play a song" in query:
            speak("What song would you like to listen to on YouTube?")
            search_query = takeCommand()
            speak(f"Playing {search_query} on YouTube")
            playSongOnYouTube(search_query)

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Musa the time is {strTime}")

        elif "search on youtube" in query:
            speak("What would you like to search for on YouTube?")
            search_query = takeCommand()
            search_url = f"https://www.youtube.com/results?search_query={search_query}"
            webbrowser.open(search_url)
        elif "opem vscode" in query:
            code_path = "Local Disk (C) - Shortcut.lnk"
            os.startfile(code_path)
        elif "opem chrome" in query:
            code_path = "Local Disk (C) - Shortcut.lnk"
            speak("Opening Chrome")
            os.startfile(code_path)

        elif "search on google" in query:
            speak("What would you like to search for on Google?")
            search_query = takeCommand()
            answer = get_google_answer(search_query)
            speak(answer)

        elif "tell me the weather" in query:
            speak("Sure, in which city?")
            city = takeCommand()
            get_weather_info(city)

        elif "Email to Musa" in query:

            try:
                speak("What should i say?")
                content = takeCommand()
                to = "jjsa"
                sendEmail(to, content)
                speak("Email has been Sent!")

            except Exception as e:
                print(e)
                speak("Sorry my friend musa, i am not able to send the email")

