// ! react native is used for app and webistes so the syntax is different 
// ! NOTE YOU CAN ALO USE TYPESCRIPT IN REACT NATIVE 
// insted of using something like a div thast just for websites you can use something like contanor that will become a div on a website  and a view on a mobile app etc
// NO HTML NO CSS

// * html elements 
// In React Native, you don't use HTML tags like <div>, <span>, or <h1>. 
//Instead, React Native provides its own components, such as <View>, <Text>, <Image>, and others.

import { View, Text } from 'react-native';

function App() {
  return (
    <View>
      <Text>Hello, world!</Text>
    </View>
  );
}

// Styling with React Native

import { StyleSheet, Text, View } from 'react-native';

function App() {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Hello, world!</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  text: {
    fontSize: 20,
    color: '#333',
  },
});

// * layout 
// React Native uses Flexbox for layout, similar to web development.
// However, everything is laid out in one direction (either vertically or horizontally), which makes Flexbox more central to the design.
<View style={{ flexDirection: 'row', justifyContent: 'space-between' }}>
  <Text>Left</Text>
  <Text>Right</Text>
</View>

// * compnents
/*
React Native provides a set of native components that map to native iOS and Android elements:
<View>: Like a div in web, it's a container for other components.
<Text>: Displays text.
<Image>: Displays images.
<ScrollView>: Provides a scrolling container.
<TextInput>: For user input. 
 */

import { View, Text, Image, TextInput } from 'react-native';

function App() {
  return (
    <View>
      <Text>Enter your name:</Text>
      <TextInput placeholder="Your name" />
      <Image source={{ uri: 'https://example.com/image.png' }} />
    </View>
  );
}

// * touchable components
/*
Since React Native doesn’t use HTML’s <button>, it has various Touchable components to handle user interactions (like tapping a button). Common ones are:
<TouchableOpacity>: Changes the opacity of the component when pressed.
<TouchableHighlight>: Highlights the component when pressed.
<TouchableWithoutFeedback>: Registers the touch event without visual feedback. 
 */
import { TouchableOpacity, Text } from 'react-native';

function App() {
  return (
    <TouchableOpacity onPress={() => alert('Button Pressed!')}>
      <Text>Press Me</Text>
    </TouchableOpacity>
  );
}

// * platform specific components
/*
React Native allows you to write platform-specific code (iOS or Android). 
You can use the Platform API to check if you're running on Android or iOS and then render specific code accordingly. 
 */
import { Platform, Text } from 'react-native';

function App() {
  return (
    <Text>
      {Platform.OS === 'ios' ? 'Running on iOS' : 'Running on Android'}
    </Text>
  );
}

// * navigation
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

const Stack = createStackNavigator();

function HomeScreen() {
  return <Text>Home Screen</Text>;
}

function DetailsScreen() {
  return <Text>Details Screen</Text>;
}

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="Details" component={DetailsScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

// * images
/*
React Native uses its own <Image> component to render images, 
and instead of importing image assets in a traditional way, they are referenced via require() or uri. 
 */
<Image
  source={{ uri: 'https://example.com/my-image.png' }}
  style={{ width: 100, height: 100 }}
/>

// * native api's and modules
/* React Native gives you access to device features like the camera, 
location, and sensors via native modules or libraries (e.g., react-native-camera for camera access). */
import { Camera } from 'react-native-camera';

function CameraScreen() {
  return <Camera style={{ flex: 1 }} />;
}

// * states and hook
/* React Native uses the same state and hooks system as React, so you can use useState, useEffect, and other hooks in React Native apps. */
import React, { useState } from 'react';
import { View, Text, Button } from 'react-native';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <View>
      <Text>You clicked {count} times</Text>
      <Button title="Click me" onPress={() => setCount(count + 1)} />
    </View>
  );
}
