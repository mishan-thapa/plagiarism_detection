import joblib

def predict_lab(lsaval,fingval):
    model = joblib.load('saved_model.pkl')
    new_obs = [[lsaval,fingval]]
    label = model.predict(new_obs)
    return label
    