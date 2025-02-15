import tkRadioTitle from './biggger Title.svg'
import styles from './Hero.module.css'

function Hero() {
    return(
        <div className={styles.hero}>
            <img src={ tkRadioTitle } className={styles.img} alt="Tk-Radio Title"></img>
            <p className={styles.p}> Welcome to Tk Radio where artists are discovered and their stories are being told.</p>
        </div>
    );
}

export default Hero