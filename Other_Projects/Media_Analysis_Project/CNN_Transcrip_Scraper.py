# Jared Sekellick
# Downloads all transcripts currently on CNN

import requests
from bs4 import BeautifulSoup
import os
import time
import datetime

# Define the URL of the CNN transcripts page
url = 'https://www.cnn.com/transcripts'

# Define the directory where the transcripts will be saved
transcript_dir = 'CNN Transcripts'

# Create the directory if it doesn't already exist
if not os.path.exists(transcript_dir):
    os.makedirs(transcript_dir)

# Define a function to download the transcripts for a given date
def download_transcripts(date):
    # Format the date as YYYY-MM-DD
    date_str = date.strftime('%Y-%m-%d')
    # Construct the URL for the transcripts for that date
    url_date = f'{url}/{date_str}.html'
    # Send a request to the URL and get the response
    response = requests.get(url_date)
    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all the transcript links on the page
    transcript_links = soup.find_all('a', {'class': 'cnnTransScriptLink'})
    # Download each transcript and save it in the transcript directory
    for link in transcript_links:
        transcript_url = link['href']
        transcript_response = requests.get(transcript_url)
        transcript_filename = os.path.join(transcript_dir, f'{date_str}_{link.text.strip()}.txt')
        with open(transcript_filename, 'w', encoding='utf-8') as f:
            f.write(transcript_response.text)
    # Wait for a few seconds to avoid overwhelming the server
    time.sleep(5)

# Send a request to the CNN transcripts index page and get the response
response = requests.get(url)

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the links to transcript pages on the index page
transcript_links = soup.find_all('a', {'class': 'cnnTransArchiveLink'})

# Loop through each transcript link and download transcripts for each date
for link in transcript_links:
    # Get the date from the link text
    date_str = link.text.strip()
    date = datetime.datetime.strptime(date_str, '%B %d, %Y').date()
    # Download transcripts for that date
    download_transcripts(date)
