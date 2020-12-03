import {firebaseConfig} from "./init.js"
firebase.initializeApp(firebaseConfig);

const AUTH = firebase.auth();
const DB = firebase.database();

const inputs = document.getElementsByTagName('input');
document.getElementById("registerAcct").addEventListener("click", () => {
  if (inputs[3].value === inputs[4].value){
    AUTH.createUserWithEmailAndPassword(inputs[2].value, inputs[3].value).then(() => {
      DB.ref("users/"+AUTH.currentUser.uid).set({
        firstName: inputs[0].value,
        lastName: inputs[1].value,
      }).then(() => window.location.href = "../ticket.html");
    }).catch(e => alert(e));
  }else{
    alert("PASSWORDS DO NOT MATCH");
    inputs[3].value = inputs[4].value = "";
  }
});