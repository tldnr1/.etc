import React from "react";
import {
  StyleSheet,
  Text,
  View,
  Image,
  TouchableOpacity,
} from "react-native";

export default function App() {
  return (
    <View style={styles.container}>
      <Text>Hello React Native</Text>
      <TouchableOpacity onPress={() => console.log("Image pressed")}>
       <View style={{ width: 200, height: 70, backgroundColor: "dodgerblue" }} />
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#FFF",
    justifyContent: "center",
    alignItems: "center",
    marginVertical: 20,
    marginHorizontal: 10,
  },
});
