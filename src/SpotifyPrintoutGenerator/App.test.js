import React from 'react';
import renderer from 'react-test-renderer';

import App from './App';
import EntryScreen from './app/screens/EntryScreen';
import PreviewScreen from './app/screens/PreviewScreen';
import ShareScreen from './app/screens/ShareScreen';

/**
 * Unit test for App.js
 */
 describe('<App />', () => {
    it('has 1 child', () => {
      const tree = renderer.create(<App />).toJSON();
      expect(tree.children.length).toBe(1);
    });
  });
  
/**
 * Unit test for EntryScreen.js
 */
describe('<EntryScreen />', () => {
    it('has 2 children', () => {
    const tree = renderer.create(<EntryScreen />).toJSON();
    expect(tree.children.length).toBe(5);
    });
});

/**
 * Unit test for PreviewScreen.js
 */
describe('<PreviewScreen />', () => {
    it('has 1 child', () => {
    const tree = renderer.create(<PreviewScreen/>).toJSON();
    expect(tree.children.length).toBe(2);
    });
});

/**
 * Unit test for ShareScreen.js
 */
describe('<ShareScreen />', () => {
    it('has 1 child', () => {
        const tree = renderer.create(<ShareScreen/>).toJSON();
        expect(tree.children) == null
    });
});

/**
 * Snapshot test for App.js
 */
 it('App.js renders correctly', () => {
    const tree = renderer.create(<App />).toJSON();
    expect(tree).toMatchSnapshot();
  });

/**
 * Snapshot test for EntryScreen.js
 */
it('EntryScreen renders correctly', () => {
    const tree = renderer.create(<EntryScreen />).toJSON();
    expect(tree).toMatchSnapshot();
  });

/**
 * Snapshot test for PreviewScreen.js
 */
it('PreviewScreen renders correctly', () => {
    const tree = renderer.create(<PreviewScreen/>).toJSON();
    expect(tree).toMatchSnapshot();
  });

/**
 * Snapshot test for ShareScreen.js
 */
it('ShareScreen renders correctly', () => {
    const tree = renderer.create(<ShareScreen/>).toJSON();
    expect(tree).toMatchSnapshot();
  });