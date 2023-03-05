import React from 'react';

class ImageArticle extends React.Component{
    render(){
      return (
        <div className='image-article'>
          <img src={this.props.image_url} alt={this.props.image_name}/>
        </div>
      );
    }
  }
export default ImageArticle;