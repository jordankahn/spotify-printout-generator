import React, { useState } from 'react';
import { 
    View,
    Text, 
    SafeAreaView, 
    TouchableOpacity,
    Image} from 'react-native';
import printoutImage from '../../assets/generated-printout.png';
import styles from '../../config/styles';

function PreviewScreen(props) {
    console.log("preview")
    const [flipStyle, onFlip] = useState(styles.image);

    const flipHandler = () => {
        if (flipStyle === styles.image) {
            onFlip(styles.rotatedImage);
        } 
        else {
            onFlip(styles.image);
        }
    }

    const pressHandler = () => {
        props.navigation.navigate('shareScreen');
    }

    return (
        <SafeAreaView style={styles.container} forceInset={{top: 'always'}}>
            <Image source={printoutImage}
                    style={flipStyle}/>
            <TouchableOpacity onPress={flipHandler}>
                <View style={styles.submitButton}>
                    <Text style={styles.submitButtonText}>Flip Printout</Text>
                </View>   
            </TouchableOpacity>
            <TouchableOpacity onPress={pressHandler}>
                <View style={styles.submitButton}>
                    <Text style={styles.submitButtonText}>Share/Print</Text>
                </View>   
            </TouchableOpacity>

        </SafeAreaView>
    );
}

export default PreviewScreen;