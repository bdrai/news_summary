// Importing modules
import React, { useState, useEffect } from "react";
import Article from "./components/article";
import './index.css';

function DayArticles(date) {
	// usestate for setting a javascript
	// object for storing and using data
	const [articles, setData] = useState();

	const getApiData = async () => {
		const response = await fetch(`/get_articles_by_date/${date}`).then((response) => response.json());
		setData(response);
	};

	useEffect(() => {getApiData()}, []);

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

function generateDateList() {
	const dateList = [];
	const today = new Date();
	const lastMonth = new Date(today.getFullYear(), today.getMonth() - 1, 1);
  
	while (lastMonth <= today) {
	  const year = lastMonth.getFullYear();
	  const month = String(lastMonth.getMonth() + 1).padStart(2, '0');
	  const day = String(lastMonth.getDate()).padStart(2, '0');
	  dateList.push(`${year}-${month}-${day}`);
	  lastMonth.setDate(lastMonth.getDate() + 1);
	}
	return dateList;
}

function App() {
	// usestate for setting a javascript
	// object for storing and using data
	const dateArray = generateDateList();

	return (
		<div className='app'>
			{dateArray &&
				dateArray.reverse().map((date) => (
					<div>
					<h1 className="date">{date}</h1>
					 {DayArticles(date)}
					</div>
				))
			}
		</div>
	);
}
export default App;
