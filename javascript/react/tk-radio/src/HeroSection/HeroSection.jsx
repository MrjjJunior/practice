import styles from './HeroSection.module.css';

function HeroSection() {
    return(
        <section className={styles.hero}>
        <div className={styles.heroContainer}>
          {/* Logo & Text */}
          <div className={styles.heroText}>
            <h1 className={styles.heroTitle}>Tk Radio</h1>
            <p className={styles.heroDescription}>
              Welcome to TK Radio where artists are discovered and their stories are being told.
            </p>
            <p className={styles.heroDescription}>
              Come on and listen to the online radio station live on Zeno.
            </p>
            <button className="hero-button">Listen</button>
          </div>
  
          {/* Image */}
          <div className="hero-image">
            <img src="your-image-url-here" alt="Radio" />
          </div>
        </div>
      </section>       
    );
}

export default HeroSection