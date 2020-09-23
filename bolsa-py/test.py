import os
import config
import time 

import firebase_admin
from firebase_admin import credentials, firestore

def delete_full_collection(config):
    print(config.credentialsFirebase)
    cred = credentials.Certificate( config.credentialsFirebase )
    defaultApp = firebase_admin.initialize_app(cred)
    db = firestore.Client()

    # [START delete_full_collection]
    def delete_collection(coll_ref, batch_size):
        docs = coll_ref.limit(batch_size).get()
        deleted = 0

        for doc in docs:
            print(u'Deleting doc {} => {}'.format(doc.id, doc.to_dict()))
            doc.reference.delete()
            deleted = deleted + 1

        if deleted >= batch_size:
            return delete_collection(coll_ref, batch_size)
    # [END delete_full_collection]

    delete_collection(db.collection(u'panel_cedears'), 10)

delete_full_collection(config)
