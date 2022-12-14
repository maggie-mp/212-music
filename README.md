# 212-music

## virtual environment -- mac
python3 -m venv env
source env/bin/activate
pip install flask

## virtual environment -- windows
py -m venv env
env\Scripts\activate.bat
pip install flask

## running flask -- mac
/Users/maggienew/Documents/Github/212-music
source env/bin/activate
export FLASK_APP=run.py
export FLASK_DEBUG=1
flask run

## running flask -- windows
env\Scripts\activate.bat
set FLASK_APP=run.py
set FLASK_DEBUG=1
py -m flask run
 



 
<!-- I've (Maggie) added comments to sections that weren't in the orgional README doc before--> 

<!--added source where this database came from-->
Cleaned up Music Database Source: https://gist.github.com/rioto9858/ff72b72b3bf5754d29dd1ebf898fc893#file-top50musicfrom2010-2019-csv



This is a dataset of top 50 Spotify music from 2010 to 2019. 

Originally published at [Kaggle:Top Spotify songs from 2010-2019 - BY YEAR](https://www.kaggle.com/leonardopena/top-spotify-songs-from-20102019-by-year) which is scraped from [Spotify: Organize your music](http://organizeyourmusic.playlistmachinery.com/)

After cleaning the data, it contains 14 columns and 603 rows of data.


<!-- I've added the definitions that were in the table but moved them to the README doc to not clutter the dB data, this will also be somewhere on the website-->
The type of attributes:
  'title' is categorical. The name of the song.

  'artist' is categorical. The artist/s of the song

  'genre of the track' is categorical. The genre that the song fits in. Includes which geographical area the music is insipred by eg. "detroit hip hop"

  'year' is quantitative. The year the song was relased in.

  'Beats per minute' is quantitative. The tempo of the song.

  'energy' is quantitative. 
  The energy of a song - the higher the value, the more energtic

  'Danceability' is quantitative. 
  The higher the value, the easier it is to dance to this song

  'Loudness/dB' is quantitative. The higher the value, the louder the song

  'Liveness' is quantitative. The higher the value, the more likely the song is a live recording

  'Valence' is quantitative. The higher the value, the more positive mood for the song

  'Length' is quantitative. The duration of the song

  'Acousticness' is quantitative. The higher the value the more acoustic the song is

  'Speechiness' is quantitative. The higher the value the more spoken word the song contains

  'Popularity' is quantitative. The higher the value the more popular the song is
  


<!-- this was in the origional doc-->

Questions and tasks related to the dataset:
  1. Is there any important characteristics (eg:Beats per minute) that make them top 50 songs in the year?
  2. What is the most popular music genre in these years and is there any trend for the popularity?

