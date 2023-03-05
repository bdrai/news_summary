import React from 'react';

class SummaryArticle extends React.Component{
    render(){
      return (
        <div className='summary-article'>
          <p>{this.props.summary}</p>
        </div>
      );
    }
  }

export default SummaryArticle;