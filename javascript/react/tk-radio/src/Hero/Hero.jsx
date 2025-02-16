import tkRadioTitle from './biggger Title.svg'
import radio from './radio.jpeg'
import styles from './Hero.module.css'


function Hero() {
    return(
        <div className={styles.hero}>
            <img src={ tkRadioTitle } className={styles.img} alt="Tk-Radio Title"></img>
            <p className={styles.p}> Welcome to Tk Radio where artists are discovered and their stories are being told</p>
            <p> Come on and listen to the online radio station live on zeno.<br>
            </br>
                <button className={styles.button}>
                    Listen
                </button> 
            </p>
            <img src={radio} className={styles.img2} alt="Radio"></img>
        </div>
        
    );
}

export default Hero