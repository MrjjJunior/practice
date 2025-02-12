/* import outward from './assets/Fonts/outward-master/outward-master/fonts/webfonts/'
*/
function Header (){
    return(
        <header className="header">
            <h1 className="h1">My first React app</h1>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
        <hr></hr>
        </header>
    );
}

export default Header