from firebase_admin import credentials, initialize_app, storage, db, delete_app


def keys_app_2():
        
    cred1 = {

    }
    credt1 = credentials.Certificate(cred1)
    app2 = initialize_app(credt1, {

    }, name='app2')

    return app2



def keys_app_1():
        

    cred1 = {

    }
    credt1 = credentials.Certificate(cred1)
    app1 = initialize_app(credt1, {

    }, name='app1')


    return app1