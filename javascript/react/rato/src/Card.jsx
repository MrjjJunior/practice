import picture from './assets/TshepisoHeadshot.jpg'

function Card(props){
    return(
        <div className="card">
            <img className="card-img" src={picture} alt="profile picture of Tshepiso"></img>
            <h2 className="card-h2"> {props.name}</h2>
            <p className="card-p"> {props.position}</p>
        </div>
    );
}

export default Card