const functions = require('firebase-functions');

// // Create and Deploy Your First Cloud Functions
// // https://firebase.google.com/docs/functions/write-firebase-functions
//
// exports.helloWorld = functions.https.onRequest((request, response) => {
//   functions.logger.info("Hello logs!", {structuredData: true});
//   response.send("Hello from Firebase!");
// });
// this the firebase functions setup code
const functions = require('firebase-functions');
const admin = require('firebase-admin');
let Promise = require('promise');
const cors = require('cors')({ origin: true });
const auth = require('basic-auth');
const request = require('request');
const algoliasearch = require('algoliasearch');
admin.initializeApp(functions.config().firebase);
const db = admin.firestore();
// listen for creating a piece of equipment in Firestore
exports.addEquipmentToAlgolia = functions.firestore.document('equipment/{document}')
.onCreate(event => {
console.log('ADD EQUIP EVENT IS', event);
const active = event.data.data().active === true ? "true" : "false"
const data = {
  objectID: event.params.document,
  description: event.data.data().description, 
  category: event.data.data().category,
  category_id: event.data.data().category_id,
  flat_fee: event.data.data().flat_fee,
  group: event.data.data().group,
  hourly: event.data.data().hourly,
  active: active,
  daily: event.data.data().daily,
  weekly: event.data.data().weekly,
  monthly: event.data.data().monthly,
  bulkItem: event.data.data().bulkItem 
 };
return addToAlgolia(data, 'equipment')
 .then(res => console.log('SUCCESS ALGOLIA equipment ADD', res))
 .catch(err => console.log('ERROR ALGOLIA equipment ADD', err));
});
// listen for editing a piece of equipment in Firestore
exports.editEquipmentToAlgolia = functions.firestore.document('equipment/{document}')
.onUpdate(event => {
console.log('edit event', event.data.data())
const active = event.data.data().active === true ? "true" : "false"
const data = {
  objectID: event.params.document,
  description: event.data.data().description, 
  category: event.data.data().category,
  category_id: event.data.data().category_id,
  flat_fee: event.data.data().flat_fee,
  group: event.data.data().group,
  hourly: event.data.data().hourly,
  active: active,
  bundleItem: event.data.data().bundleItem,
  daily: event.data.data().daily,
  weekly: event.data.data().weekly,
  monthly: event.data.data().monthly,
  bulkItem: event.data.data().bulkItem 
 };
console.log('DATA in is', data)
return editToAlgolia(data, 'equipment')
 .then(res => console.log('SUCCESS ALGOLIA EQUIPMENT EDIT', res))
 .catch(err => console.log('ERROR ALGOLIA EQUIPMENT EDIT', err));
});
// listen for a delete of a piece of equipment in Firestore
exports.removeEquipmentFromAlgolia = functions.firestore.document('equipment/{document}')
.onDelete(event => {
 const objectID = event.params.document;
 return removeFromAlgolia(objectID, 'equipment')
 .then(res => console.log('SUCCESS ALGOLIA equipment ADD', res))
 .catch(err => console.log('ERROR ALGOLIA equipment ADD', err));
})
// helper functions for create, edit and delete in Firestore to replicate this in Algolia
function addToAlgolia(object, indexName) {
 console.log('GETS IN addToAlgolia')
 console.log('object', object)
 console.log('indexName', indexName)
 const ALGOLIA_ID = functions.config().algolia.app_id;
 const ALGOLIA_ADMIN_KEY = functions.config().algolia.api_key;
 const client = algoliasearch(ALGOLIA_ID, ALGOLIA_ADMIN_KEY);
 const index = client.initIndex(indexName);
return new Promise((resolve, reject) => {
  index.addObject(object)
  .then(res => { console.log('res GOOD', res); resolve(res) })
  .catch(err => { console.log('err BAD', err); reject(err) });
 });
}
function editToAlgolia(object, indexName) {
 const ALGOLIA_ID = functions.config().algolia.app_id;
 const ALGOLIA_ADMIN_KEY = functions.config().algolia.api_key;
 const client = algoliasearch(ALGOLIA_ID, ALGOLIA_ADMIN_KEY);
 const index = client.initIndex(indexName);
return new Promise((resolve, reject) => {
  index.saveObject(object)
  .then(res => { console.log('res GOOD', res); resolve(res) })
  .catch(err => { console.log('err BAD', err); reject(err) });
 });
}
function removeFromAlgolia(objectID, indexName) {
 const ALGOLIA_ID = functions.config().algolia.app_id;
 const ALGOLIA_ADMIN_KEY = functions.config().algolia.api_key;
 const client = algoliasearch(ALGOLIA_ID, ALGOLIA_ADMIN_KEY);
 const index = client.initIndex(indexName);
return new Promise((resolve, reject) => {
  index.deleteObject(objectID)
  .then(res => { console.log('res GOOD', res); resolve(res) })
  .catch(err => { console.log('err BAD', err); reject(err) });
 });
}
