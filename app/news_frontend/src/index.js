import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';


class ImageArticle extends React.Component{
  render(){
    return (
      <div className='image-article'>
        <img src={this.props.image_url} alt={this.props.image_name}/>
      </div>
    );
  }
}

class TitleArticle extends React.Component{
  render(){
    return (
      <div className='title-article'>
        <h3>{this.props.title}</h3>
      </div>
    );
  }
}

class SummaryArticle extends React.Component{
  render(){
    return (
      <div className='summary-article'>
        <p>{this.props.summary}</p>
      </div>
    );
  }
}

class ContentArticle extends React.Component{
  render(){
    return (
        <div className='content-article'>
          <div className='content-wrapper'>
            <TitleArticle
              title="Morocco's World Cup celebrations an uneasy sight in Toto"
            />
            <SummaryArticle
              summary="Iran was ousted from a United Nations women's group on Wednesday for policies contrary to the rights of women and girls, a move proposed by the United States after Tehran's crackdown on protests.Iran was ousted from a United Nations women's group on Wednesday for policies contrary to the rights of women and girls, a move proposed by the United States after Tehran's crackdown on protests.Iran was ousted from a United Nations women's group on Wednesday for policies contrary to the rights of women and girls, a move proposed by the United States after Tehran's crackdown on protests."
            />
          </div>
        </div>
    );
  }
}

class Article extends React.Component{
  render(){
    return (
      <div className='article'>
        <a href='https://www.i24news.tv/en/news/middle-east/sport/1671014663-morocco-s-world-cup-celebrations-an-uneasy-sight-in-israel'>
          <div className='wrapper'>
            <ImageArticle
              image_url="https://cdn.i24news.tv/uploads/28/14/a7/cc/a3/1a/a9/92/96/6b/3e/8d/98/a9/c5/75/2814a7cca31aa992966b3e8d98a9c575.jpg?width=350"
              image_name="toto"
            />
            <ContentArticle/>
          </div>
          
        </a>
        
      </div>
    );
  }
}

class SetArticles extends React.Component {
  render(){
    return (
      <div className='set-article'>
        <Article/>
        <Article/>
      </div>
    );
  }
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<SetArticles />);
  