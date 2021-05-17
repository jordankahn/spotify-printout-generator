import {StyleSheet} from 'react-native';
import colors from './colors';

const styles = StyleSheet.create({
    container: {
        backgroundColor: colors.background,
        flex: 1,
        justifyContent: "center",
        alignItems: "center"
    },
    grid: {
        justifyContent: 'center',
        flexDirection: 'row',
        flexWrap: 'wrap',
        flex: 1,
    },
    image: {
        width: 408,
        height: 529
    },
    rotatedImage: {
        width: 408,
        height: 529,
        transform: [{rotate: '180deg'}],
    },
    header: {
        fontSize: 30,
        fontWeight: "bold",
        color: colors.black,
        paddingRight: 40,
        paddingLeft: 40,
        textAlign: "center",
        flexWrap: "wrap"
    },
    secondaryText: {
        fontSize: 16,
        color: colors.black,
        paddingRight: 40,
        paddingLeft: 40,
        paddingTop: 10,
        textAlign: "center",
        flexWrap: "wrap"
    },
    warningText: {
        fontSize: 16,
        color: colors.red,
        paddingRight: 40,
        paddingLeft: 40,
        paddingTop: 10,
        textAlign: "center",
        flexWrap: "wrap"
    },
    input: {
        height: 40,
        width: 200,
        margin: 12,
        borderWidth: 1,
        color: "grey"
    },
    submitButton: {
        width: 120,
        height: 50,
        margin: 20,
        backgroundColor: colors.button,
        alignItems: "center",
        justifyContent: "center"
    },
    submitButtonText: {
        fontWeight: "bold",
        fontSize: 16,
        color: colors.white,
    }
})

export default styles;