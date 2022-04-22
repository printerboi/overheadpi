import styles from '../../styles/CardButton.module.css'


export default function CardButton(props){
    return(
        <button className={styles.cardButton} onClick={props.onClick}>
            <div className={`${styles.carbuttonContainer}`}>
                <div className="card-body">
                <div className={styles.CardIcon}>
                    <i className={`bx ${props.icon}`}></i>
                </div>
                <h4 className="card-text">{props.text}</h4>
                </div>
            </div>
        </button>
    );
}