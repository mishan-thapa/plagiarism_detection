import joblib

def predict_lab(lsaval,fingval,word_sim,ngram_sim):
    model = joblib.load('saved_model1.pkl')
    new_obs = [[lsaval,fingval,word_sim,ngram_sim]]
    label = model.predict(new_obs)
    return label
    