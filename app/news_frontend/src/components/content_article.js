import React from 'react';
import SummaryArticle from './summary_article';
import TitleArticle from './title_article';

class ContentArticle extends React.Component{
    render(){
      return (
          <div className='content-article'>
            <div className='content-wrapper'>
              <TitleArticle
                title={this.props.title}
              />
              <SummaryArticle
                summary={this.props.summary}
              />
            </div>
          </div>
      );
    }
  }

export default ContentArticle;