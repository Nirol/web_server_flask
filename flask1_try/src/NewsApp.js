import React, { Component, useState, useEffect } from 'react';


const NewsApp = () => {

//state
const [news, setNews] = useState([])
const [searchQuery, setSearchQuery] = useState('react')
const [url, seturl] = useState('https://hn.algolia.com/api/v1/search?query=react')

//fetch news
const fetchNews = () => {
    // eslint-disable-next-line no-template-curly-in-string
    fetch(url).then(result => result.json())
    .then(data => setNews(data.hits))
    .catch(error => console.log(error));


};

useEffect(() => {

fetchNews();

});



const handleChange = e => {
setSearchQuery(e.target.value);


}


const handleSubmit = e => {
    e.preventDeafult();
    seturl()


}


return (
<div>
<h2>News</h2>
<form onSubmit={handleSubmit}>
<input type="text" value={searchQuery} onChange={handleChange} />
<button>Search</button>
</form>
{news.map((n,i) => (<p key={i}> {n.title} </p>) )}
</div>

)

}

export default NewsApp;