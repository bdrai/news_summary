import React from 'react';

class TitleArticle extends React.Component{
    render(){
      return (
        <div className='title-article'>
          <h3>{this.props.title}</h3>
        </div>
      );
    }
  }

export default TitleArticle;