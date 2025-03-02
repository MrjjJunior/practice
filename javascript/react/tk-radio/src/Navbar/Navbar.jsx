import styles from './Navbar.module.css';
import home_img from './Home icon.svg';
import about_img from './info.svg';

function Navbar() {
    return (
        <div className={styles.navbar}>

            <div className={styles.home}>
                <a href="#home">
                    <img src={home_img} alt="home image"></img>
                </a>
            </div>

            <div className={styles.home}>
                <a href="#about">
                    <img src={about_img} alt="about img"></img>
                </a>            
            </div>

        </div>
    );
}

export default Navbar