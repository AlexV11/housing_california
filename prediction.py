import joblib

def predict(data, model):
    if model == 'Linear regression':
        model = joblib.load('linear_regression_model.pkl')
    elif model == 'Decision tree regression':
        model = joblib.load('tree_regression_model.pkl')
    elif model == 'Random forest regression':
        model = joblib.load('random_forest_model.pkl')
    elif model == 'Support vector regression':
        model = joblib.load('svr_regression_model.pkl')

    pipeline = joblib.load('full_pipeline.pkl')
    data = pipeline.transform(data)
    return model.predict(data)

