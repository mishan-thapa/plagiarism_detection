import joblib

def predict_lab(lsaval,ngram_sim):
    model = joblib.load('saved_model_nepali1.pkl')
    new_obs = [[lsaval,ngram_sim]]
    label = model.predict(new_obs)
    return label
    