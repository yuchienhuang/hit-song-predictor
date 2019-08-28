$(function() {
    $('form').submit(function(event) {
      event.preventDefault();

      let song = $('input[name="song"').val();
      let artist = $('input[name="artist"]').val();

      $.get('/feature_table?' + $.param({song: song, artist: artist}), function(data) {
        $('input[type="text"]').val('');
        $('input').focus();


        //let obj = jQuery.parseJSON( data );

        let table = data.trackdf;
        let link = data.link;
        let artists = data.artists;
        let hits = data.hit_list;
        let topthree = data.top_three;
        let album_popularity = data.popularity;

        const albumDiv = document.getElementById('albumlink');
        while (albumDiv.firstChild) {
          albumDiv.removeChild(albumDiv.firstChild);
        }

        const predictionDiv = document.getElementById('prediction');
        const scoreDiv = document.getElementById('score');
        const albumPopDiv = document.getElementById('album');
        const tableDiv = document.getElementById('print');


        console.log(album_popularity)

        if(album_popularity==''){


        albumDiv.innerHTML = '<div> Check spelling!  <em>' + song + '</em>' + ' by ' +  '<em>' + artist + "</em> is not in the Spotify database... </div>";
        predictionDiv.innerHTML = '';
        scoreDiv.innerHTML = '';
        albumPopDiv.innerHTML = '';
        tableDiv.innerHTML = '';



        }else{


        albumDiv.appendChild(StoryDOMObject(link,artists,newtab=true));





        if(hits == ''){
          predictionDiv.innerHTML = '<div> No song pass the hit song threshold, but the following two songs have the highest scores. </div>';
        }else{predictionDiv.innerHTML = hits;}



        scoreDiv.innerHTML =  topthree;



        albumPopDiv.innerHTML = '<div> (album popularity score: ' + album_popularity + ') </div>';



        tableDiv.innerHTML = table;



        }







        });
        return false;
      });
    });


    function StoryDOMObject(web_link,artist,newtab=false) {
      const card = document.createElement('div');
      // card.setAttribute('id', storyJSON._id);
      card.className = 'story card';

      const cardBody = document.createElement('div');
      cardBody.className = 'card-body';
      card.appendChild(cardBody);

      const creatorSpan = document.createElement('a');
      creatorSpan.className = 'story-creator card-title';
      creatorSpan.innerHTML = artist;
      creatorSpan.setAttribute('href', web_link);
      if(newtab == true){
        creatorSpan.target = "_blank"
      }
      cardBody.appendChild(creatorSpan);

      // const contentSpan = document.createElement('p');
      // contentSpan.className = 'story-content card-text';
      // console.log(storyJSON );
      // contentSpan.innerHTML = storyJSON.energy;
      // cardBody.appendChild(contentSpan);

      const cardFooter = document.createElement('div');
      cardFooter.className = 'card-footer';
      card.appendChild(cardFooter);


      return card;
    }
