function renderStories(stories) {

    const data_json  = JSON.parse(stories);
    const storiesDiv = document.getElementById('results');


    spotify_data = data_json[0]
    azlyrics_data = data_json[1]


    for (let i = 0; i < spotify_data.length; i++){
        storiesDiv.appendChild(StoryDOMObject('/features/' + spotify_data[i]['id'],spotify_data[i]['artist_names']));

    }

    const otherStoriesDiv = document.getElementById('no results');

    for (let i = 0; i < azlyrics_data.length; i++){
        otherStoriesDiv.appendChild(StoryDOMObject(azlyrics_data[i]['web'],azlyrics_data[i]['artist_names'],true));

    }

}


function StoryDOMObject(web_link,artist,newtab=false) {
  const card = document.createElement('div');

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

  const cardFooter = document.createElement('div');
  cardFooter.className = 'card-footer';
  card.appendChild(cardFooter);


  return card;
}

function newNavbarItem(text, url) {

  const itemLink = document.createElement('a');
  itemLink.innerHTML = text;
  itemLink.href = url;

  const itemNav = document.createElement('li');
  itemNav.className = 'nav';
  itemNav.appendChild(itemLink);


  return itemNav
}

function renderNavbar() {
  // const navbarDiv = document.getElementById('nav-item-container');
  const navbarDiv = document.getElementById('nav-item-container');

  navbarDiv.appendChild(newNavbarItem('&#127897 &#127925 &#127927', '/'));
  navbarDiv.appendChild(newNavbarItem('&#191Hit the Hit?', '/predictor'));


}

