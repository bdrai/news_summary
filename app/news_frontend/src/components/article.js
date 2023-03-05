import React from 'react';
import ImageArticle from './image_article';
import ContentArticle from './content_article';

class Article extends React.Component{
    render(){
      return (
        <div className='article'>
          <a href={this.props.url}>
            <div className='wrapper'>
              <ImageArticle
                image_url={this.props.image_url}
                image_name={this.props.title}
              />
              <ContentArticle
                title={this.props.title}
                summary={this.props.summary}
              />
            </div>
          </a>
        </div>
      );
    }
}
export default Article;