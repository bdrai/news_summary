// Importing modules
import React, { useState, useEffect } from "react";
import Article from "./components/article";
import './index.css';

function App() {
	// usestate for setting a javascript
	// object for storing and using data
	const [articles, setData] = useState();

	const getApiData = async () => {
		const response = await fetch("/get_articles_limit/10").then((response) => response.json());
		setData(response);
	};

	useEffect(() => {
		getApiData();
	  }, []);

	return (
		<div className='set-article'>
			{articles &&
				articles.map((article) => (
					<Article 
						key={article.id}
						image_url={article.image}
						title={article.title}
						summary={article.subtitle}
						url={article.url}
					/>
			))}
		</div>
	);
}
export default App;
