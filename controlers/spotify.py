# Python module to diseno
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
import webbrowser
import pyautogui
import time



class spotify:
    scopes = ["user-follow-read", 'ugc-image-upload', 'user-read-playback-state',
              'user-modify-playback-state', 'user-read-currently-playing', 'user-read-private',
              'user-read-email', 'user-follow-modify', 'user-follow-read', 'user-library-modify',
              'user-library-read', 'streaming', 'app-remote-control', 'user-read-playback-position',
              'user-top-read', 'user-read-recently-played', 'playlist-modify-private', 'playlist-read-collaborative',
              'playlist-read-private', 'playlist-modify-public']
    sp = None

    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="5cf8b2af777741c5b38ee5f309994131",
                                                            client_secret="004388617b734122a2a5a630b2f8d2f3",
                                                            redirect_uri='http://127.0.0.1:9090',
                                                            scope=self.scopes))
        user_data = self.sp.current_user()

    def info(self):
        user_data = self.sp.current_user()
        data = f"usuario:{user_data['display_name']}\n"
        data += f"Account:{user_data['product']}\n"
        data += f"Followers: {user_data['followers']['total']}\n"
        data += f"Link:' {user_data['external_urls']['spotify']}\n"
        return data

    def followed(self):
        print('\n\nFollowed Artists')
        artists = self.sp.current_user_followed_artists()['artists']
        artistas = ""
        try:
            if ('items' in artists):
                for i, artist in enumerate(artists['items']):
                    artistas += f'{i} - {artist["name"]} \n'

                if artists['next']:
                    artists = self.sp.next(artists)
                else:
                    artists = None

        except Exception as e:
            print('Error', e)

        return artistas

    def buscar(self,value):
        src=value["search"]
        if(src!=""):
            pyautogui.moveTo(x=1888, y=0)
            pyautogui.doubleClick()
            result = self.sp.search(src)
            pprint.pprint(result["tracks"]["items"][0]['id'])
            webbrowser.open("https://open.spotify.com/track/" +
                            result["tracks"]["items"][0]['id'])
            time.sleep(10)
            pyautogui.moveTo(x=366, y=586)
            pyautogui.doubleClick()
            return f'reproduciendo {result["tracks"]["items"][0]["name"]}'
        return "no se encontro una  cancion"

    def lista(self, a):
        
        playlist_id = ''
        if (type(a) == dict):
            if a["lista"] == "default":
                playlist_id = '37i9dQZF1E35yx2VFmcHZn'
               
            else:
                if (a['lista'].isnumeric()):
                    lista = self.listas(tipo=1)[int(a['lista'])-1]
                    if (lista['id'] == int(a['lista'])):
                       playlist_id = lista['playId']
                else:
                    return "debes escribir el numero de la lista"
            playlist = self.sp.playlist(playlist_id=playlist_id)
            playlist_tracks = playlist['tracks']
            webbrowser.open(playlist['uri'])
            webbrowser.open( playlist['external_urls']['spotify'])
            reprod=playlist_tracks['items'][0]['track']['name']
            time.sleep(5)
            pyautogui.moveTo(x=366, y=502)
            pyautogui.click()
            return 'reproduciendo playlist '+ playlist['name'] +" cancion "+ reprod  
        
                

    def listas(self, tipo=None):

        listas = ""
        listaArray = []
        playlists = self.sp.current_user_playlists()
        while playlists:
            for i, playlist in enumerate(playlists['items']):
                listas += f'\n\n{i+1} - {playlist["name"]}\n'
                listaArray.append(
                    {'id': i+1, 'name': playlist["name"], 'playId': playlist["id"]})
            if playlists['next']:
                playlists = self.sp.next(playlists)
            else:
                playlists = None

        if tipo == None:
            return listas
        else:
            return listaArray

    def recently(self):

        recents = self.sp.current_user_recently_played()
        while recents:

            for i, track in enumerate(recents['items']):
                return f'{i} - {track["track"]["name"]}\n{track["track"]["uri"]}'
            if recents['next']:
                recents = self.sp.next(recents)
            else:
                recents = None

    def validateLista(self, text):
        if (len(text.split(' ')) == 2):
            return None
        else:
            if ('por defecto' in text):
                return {'lista': "default"}
            
    def validateBuscar(self,text):
        if("busca"in text.lower()):
            buscar=""
            if("de" in text):
                indice=text.split(" ").index("de")
                buscar= " ".join(text.split(" ")[indice+1::])
            else:
                indice=text.lower().split(" ").index("busca")
                buscar= " ".join(text.split(" ")[indice+1::]) 
        if(buscar!=""):
            return {"search":buscar}
        return {}
                   
           
