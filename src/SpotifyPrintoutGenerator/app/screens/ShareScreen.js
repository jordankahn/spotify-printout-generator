import React from 'react';
import { 
    View,
    Text, 
    SafeAreaView, 
    TouchableOpacity,
    Image,
    Alert,
    Share} from 'react-native';
import * as MediaLibrary from 'expo-media-library';
import { Asset } from 'expo-asset';
import printoutImage from '../../assets/generated-printout.png';
import * as MailComposer from 'expo-mail-composer';
import styles from '../../config/styles';

function ShareScreen(props) {

    //opens an email dialog for the user to send a PDF of the printout (iOS and Android only)
    const emailHandler = async () => {
        const [{ localUri }] = await Asset.loadAsync(require('../../assets/generated-printout.pdf'));
        console.log("Email")
        MailComposer.composeAsync({
            recipients: [],
            subject: "Your Spotify Printout is Ready!",
            body: "Attached is a PDF of your printout created by the Spotify Printout Generator!",
            attachments: [localUri]
        })
    }

    //downloads a png of the printout to the user's device (iOS and Android only)
    const downloadHandler = async () => {
        const printoutUri = Image.resolveAssetSource(printoutImage).uri.split('?')[0];
        MediaLibrary.requestPermissionsAsync();
        MediaLibrary.saveToLibraryAsync(printoutUri);
        Alert.alert(
            "Printout Downloaded!",
            "A PNG file of your printout has been saved to your camera roll.",
            [
                { text: "OK", onPress: () => console.log("OK Pressed") }
            ],
            { cancelable: false }
        );
    }

    //opens multiple sharing options for a PDF version of the printout (iOS only)
    const shareHandler = async () => {
        const [{ localUri }] = await Asset.loadAsync(require('../../assets/generated-printout.pdf'));
        const result = await Share.share({
            message: 'Check out this printout generated with Spotify Printout Generator!',
            url: localUri
        });
    }

    return (
        <SafeAreaView style={styles.container} forceInset={{top: 'always'}}>
            <Image source={printoutImage}
                    style={styles.image}/>
            <View style={styles.grid}>
                <TouchableOpacity onPress={downloadHandler}>
                    <View style={styles.submitButton}>
                        <Text style={styles.submitButtonText}>Download</Text>
                    </View>   
                </TouchableOpacity>
                <TouchableOpacity onPress={emailHandler}>
                    <View style={styles.submitButton}>
                        <Text style={styles.submitButtonText}>Email</Text>
                    </View>   
                </TouchableOpacity>
                <TouchableOpacity onPress={shareHandler}>
                    <View style={styles.submitButton}>
                        <Text style={styles.submitButtonText}>Share</Text>
                    </View>   
                </TouchableOpacity>
            </View>

        </SafeAreaView>
    );
}

export default ShareScreen;