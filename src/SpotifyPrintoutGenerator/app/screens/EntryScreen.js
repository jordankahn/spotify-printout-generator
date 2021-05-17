import React, { useState } from 'react';
import { 
    View,  
    Text, 
    TextInput, 
    SafeAreaView, 
    TouchableOpacity} from 'react-native';
import colors from '../../config/colors';
import styles from '../../config/styles';
import fetchData from '../api/fetchData';

/**
 * The first screen of the app where you can enter a Spotify playlist or album
 */
function EntryScreen(props) {

    const [text, onChangeText] = useState("enter URL here");
    const [warningText, onChangeWarning] = useState("");
    
    const pressHandler = async () => {
        const data = await fetchData(text);
        console.log(data);
        if (data["error"] !== undefined) {
            console.log(data["error"]);
            onChangeWarning("The URL you entered is not for a Spotify playlist or album. Please try again.");
            return;
        }
        onChangeWarning("");
        props.navigation.navigate('previewScreen');
    }

    return (
        <SafeAreaView style={styles.container} forceInset={{top: 'always'}}>
            <Text style={styles.header}>Welcome to the Spotify Printout Generator!</Text>
            <Text style={styles.secondaryText}>Please enter a valid Spotify playlist or album link below</Text>
            <Text 
                onChangeWarning = {onChangeWarning}
                style= {styles.warningText}>
                {warningText}
            </Text>
            <TextInput
                style={styles.input}
                onChangeText={onChangeText}
                placeholder={text}
                backgroundColor={colors.white}
                autoCapitalize="none"
            />
            <TouchableOpacity onPress={pressHandler}>
                <View style={styles.submitButton}>
                    <Text style={styles.submitButtonText}>Submit</Text>
                </View>   
            </TouchableOpacity>
        </SafeAreaView>
    );
}

export default EntryScreen;