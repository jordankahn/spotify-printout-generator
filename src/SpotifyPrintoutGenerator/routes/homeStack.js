import { createStackNavigator } from 'react-navigation-stack';
import { createAppContainer } from 'react-navigation';
import EntryScreen from '../app/screens/EntryScreen';
import PreviewScreen from '../app/screens/PreviewScreen';
import ShareScreen from '../app/screens/ShareScreen';

const screens = {
    entryScreen: {
        screen: EntryScreen,
        navigationOptions: {
            title: "Home",
        },
    },
    previewScreen: {
        screen: PreviewScreen,
        navigationOptions: {
            title: "Printout Preview",
        },
    },
    shareScreen: {
        screen: ShareScreen,
        navigationOptions: {
            title: "Share Your Printout",
        },
    }
}


const HomeStack = createStackNavigator(screens);

export default createAppContainer(HomeStack);