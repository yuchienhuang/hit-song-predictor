from flask import request, render_template, redirect, url_for, flash,  jsonify
from mymix import app, db
from mymix.album import *
from mymix.spotify import *
import pandas as pd
import dill
import json
import sklearn
import seaborn as sns


p = os.path.join(app.root_path, 'public/ml_models/modelnew.pkd')
model = dill.load(open(p, 'rb'))


@app.route('/predictor')
def predictor():



    data = '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>id</th>\n      <th>track_number</th>\n      <th>popularity</th>\n      <th>name</th>\n      <th>duration_ms</th>\n      <th>tempo</th>\n      <th>time_signature</th>\n      <th>key</th>\n      <th>valence</th>\n      <th>mode</th>\n      <th>acousticness</th>\n      <th>danceability</th>\n      <th>energy</th>\n      <th>instrumentalness</th>\n      <th>liveness</th>\n      <th>loudness</th>\n      <th>speechiness</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>6od5hFv9IT5JHc7NEF9HRv</td>\n      <td>1</td>\n      <td>72</td>\n      <td>Victorious</td>\n      <td>178600</td>\n      <td>110.010</td>\n      <td>4</td>\n      <td>8</td>\n      <td>0.6910</td>\n      <td>1</td>\n      <td>0.002050</td>\n      <td>0.570</td>\n      <td>0.865</td>\n      <td>0.000000</td>\n      <td>0.4040</td>\n      <td>-4.518</td>\n      <td>0.0472</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>2fh3bZ8jZhMxOcfESE9nQY</td>\n      <td>2</td>\n      <td>74</td>\n      <td>Don\'t Threaten Me With A Good Time</td>\n      <td>213093</td>\n      <td>183.825</td>\n      <td>4</td>\n      <td>1</td>\n      <td>0.5900</td>\n      <td>0</td>\n      <td>0.015400</td>\n      <td>0.559</td>\n      <td>0.895</td>\n      <td>0.000000</td>\n      <td>0.1750</td>\n      <td>-4.476</td>\n      <td>0.0832</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>6TzJLISIitIzn1WtjDY0Op</td>\n      <td>3</td>\n      <td>70</td>\n      <td>Hallelujah</td>\n      <td>180627</td>\n      <td>80.008</td>\n      <td>4</td>\n      <td>11</td>\n      <td>0.6150</td>\n      <td>1</td>\n      <td>0.011000</td>\n      <td>0.578</td>\n      <td>0.886</td>\n      <td>0.000000</td>\n      <td>0.1430</td>\n      <td>-4.348</td>\n      <td>0.0633</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>3px2rAPu74ltbkf9eZsZ8h</td>\n      <td>4</td>\n      <td>74</td>\n      <td>Emperor\'s New Clothes</td>\n      <td>158667</td>\n      <td>94.481</td>\n      <td>4</td>\n      <td>1</td>\n      <td>0.6510</td>\n      <td>1</td>\n      <td>0.003020</td>\n      <td>0.562</td>\n      <td>0.904</td>\n      <td>0.000000</td>\n      <td>0.0433</td>\n      <td>-4.947</td>\n      <td>0.0807</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>1BECwm5qkaBwlbfo4kpYx8</td>\n      <td>5</td>\n      <td>78</td>\n      <td>Death Of A Bachelor</td>\n      <td>203507</td>\n      <td>139.256</td>\n      <td>4</td>\n      <td>0</td>\n      <td>0.4050</td>\n      <td>1</td>\n      <td>0.013700</td>\n      <td>0.462</td>\n      <td>0.538</td>\n      <td>0.000000</td>\n      <td>0.4290</td>\n      <td>-5.527</td>\n      <td>0.0590</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>6V68ItawQkQlZhYIf1S86C</td>\n      <td>6</td>\n      <td>69</td>\n      <td>Crazy=Genius</td>\n      <td>198040</td>\n      <td>114.109</td>\n      <td>4</td>\n      <td>2</td>\n      <td>0.4470</td>\n      <td>1</td>\n      <td>0.000247</td>\n      <td>0.455</td>\n      <td>0.910</td>\n      <td>0.000000</td>\n      <td>0.1070</td>\n      <td>-4.464</td>\n      <td>0.1660</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>2fmCA13dwQQOGBIbIOWRiJ</td>\n      <td>7</td>\n      <td>73</td>\n      <td>LA Devotee</td>\n      <td>196520</td>\n      <td>175.998</td>\n      <td>4</td>\n      <td>9</td>\n      <td>0.6980</td>\n      <td>1</td>\n      <td>0.000430</td>\n      <td>0.490</td>\n      <td>0.848</td>\n      <td>0.000008</td>\n      <td>0.0665</td>\n      <td>-5.050</td>\n      <td>0.0645</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>3fwKVZ73y7UUGMyR6rVCRa</td>\n      <td>8</td>\n      <td>68</td>\n      <td>Golden Days</td>\n      <td>254320</td>\n      <td>128.006</td>\n      <td>4</td>\n      <td>7</td>\n      <td>0.2060</td>\n      <td>1</td>\n      <td>0.003290</td>\n      <td>0.556</td>\n      <td>0.708</td>\n      <td>0.000000</td>\n      <td>0.3290</td>\n      <td>-5.708</td>\n      <td>0.0390</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>5eoZTdiq4C4aoEfUwAN0ha</td>\n      <td>9</td>\n      <td>68</td>\n      <td>The Good, The Bad And The Dirty</td>\n      <td>171520</td>\n      <td>156.071</td>\n      <td>4</td>\n      <td>7</td>\n      <td>0.8240</td>\n      <td>0</td>\n      <td>0.001910</td>\n      <td>0.531</td>\n      <td>0.825</td>\n      <td>0.000000</td>\n      <td>0.3290</td>\n      <td>-5.333</td>\n      <td>0.0545</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>2DgdHcjWmO3qd50RzuBLgZ</td>\n      <td>10</td>\n      <td>70</td>\n      <td>House Of Memories</td>\n      <td>208707</td>\n      <td>109.952</td>\n      <td>4</td>\n      <td>11</td>\n      <td>0.5060</td>\n      <td>0</td>\n      <td>0.002720</td>\n      <td>0.506</td>\n      <td>0.817</td>\n      <td>0.000000</td>\n      <td>0.0486</td>\n      <td>-5.051</td>\n      <td>0.0335</td>\n    </tr>\n    <tr>\n      <th>10</th>\n      <td>5j9yOfRB2s6OMS1YwwYiMw</td>\n      <td>11</td>\n      <td>65</td>\n      <td>Impossible Year</td>\n      <td>202547</td>\n      <td>85.574</td>\n      <td>3</td>\n      <td>10</td>\n      <td>0.0978</td>\n      <td>1</td>\n      <td>0.474000</td>\n      <td>0.174</td>\n      <td>0.337</td>\n      <td>0.000294</td>\n      <td>0.1100</td>\n      <td>-8.767</td>\n      <td>0.0313</td>\n    </tr>\n  </tbody>\n</table>'


    return render_template('predictor.html', data=data)



@app.route('/')
def homepage():
    return render_template('index.html')





@app.route('/feature_table', methods = ['GET'])
def feature_table():
    album_name =  request.args['song']
    track_artist_names = request.args['artist']
    try:
        album_id = get_album_id_from_album(album_name, track_artist_names)



        abj = album_json(album_id)
        a = Album(abj)


        hit_list, top_three = hit_song_predictor(a, model)



        # print('album id: ', abj['popularity'], ' type: ', type(int(abj['popularity'])))

        # x_test = abj['popularity']
        # y_predict = modeltest.predict([[x_test]])
        # print('predict testing...', y_predict)


        album_info, tracks_info = get_data(abj)


        artist_names = print_artists(album_info['artists_list'])
        spotify_album_link = get_audio_link(album_id, 'album')





        # tracks_html = tracks_info[['name','popularity','acousticness','danceability','energy','liveness','loudness','speechiness']].set_index('name').sort_values(by='popularity',ascending=False).to_html()

        # print(artist_names,spotify_album_link)
        hit_str = print_tracks(hit_list)
        top_three_str = print_tracks(top_three)

        # hit_html = pd.DataFrame(hit_list).to_html(index=False, header=False)
        # top_three_html = pd.DataFrame(top_three).to_html(index=False, header=False)

        #print(hit_str, top_three_str)

        cm = sns.light_palette("pink", as_cmap=True)

        df = a.tracks_df[['track_number', 'name','popularity','acousticness', 'danceability', 'energy', 'liveness', 'speechiness','valence']].sort_values(by='popularity',ascending=False).set_index('track_number')
        del df.index.name
        tracks_html = df.style.background_gradient(cmap=cm)._repr_html_()




        return jsonify(trackdf=tracks_html, link=spotify_album_link, artists=artist_names, hit_list=hit_str, top_three=top_three_str, popularity=a.popularity)
    except:
        return jsonify(trackdf='', link='', artists='', hit_list='', top_three='', popularity='')

