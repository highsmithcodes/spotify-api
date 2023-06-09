from flask import Flask, jsonify, request
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

# Set up Spotify credentials
client_id = '043908d5e3844f769aecaad844623854'
client_secret = '6f4b6912c23e404bb1625c28445ef3fb'
redirect_uri = 'https://powerful-thicket-30866-4deb00c4126c.herokuapp.com/current-song'  # Update the redirect URI to match your local development setup

# Create the Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='user-read-playback-state'))

app = Flask(__name__)

@app.route('/current-song')
def current_song():
    code = request.args.get('code')  # Get the authorization code from the request URL parameters
    
    # Check if the code parameter is present
    if code:
        # Exchange the authorization code for an access token
        sp.auth_manager.get_access_token(code, as_dict=False)  # Use as_dict=False to avoid the invalid_request error
        
    # Get the current user's playback information
    current_playback = sp.current_playback()

    if current_playback is not None and current_playback['is_playing']:
        track = current_playback['item']
        track_name = track['name']
        artists = ', '.join([artist['name'] for artist in track['artists']])
        return jsonify({'track_name': track_name, 'artists': artists})
    else:
        return jsonify({'track_name': 'No song is currently playing.', 'artists': ''})

if __name__ == '__main__':
    app.run()