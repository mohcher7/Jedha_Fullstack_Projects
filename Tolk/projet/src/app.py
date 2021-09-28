from flask import Flask, request, jsonify,render_template
import joblib
import numpy as np
import re
import ast
import unidecode
import spacy

from spacy.lang.fr.stop_words import STOP_WORDS
nlp = spacy.load("fr_core_news_sm")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('layout2.html')

@app.route("/predict", methods=["POST"])
def predict():
    texte =  request.form["phrase"]
    
    global STOP_WORDS
    #preprocessing
    nlp.Defaults.stop_words |= {"bonjour","bonsoir","bjr","bsr","b","c","d","e","f",'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',"w","x","y","z"}

    text_clean = str(texte)
    text_clean = text_clean.replace('\d+', '')
    text_clean= re.sub(r'http\S+', '', text_clean) #delete http adresses
    
    text_clean = unidecode.unidecode(text_clean)

    text_clean = text_clean.replace(r"[^A-Za-z0-9 ]+", " ")
    #df["text_clean"] = df["text_clean"].apply(lambda x:''.join(ch for ch in x if ch.isalnum() or ch in [" "]))
    text_clean = text_clean.lower().strip()
    STOP_WORDS = list(STOP_WORDS)

    for elem in range(0,len(STOP_WORDS)):
        STOP_WORDS[elem] = unidecode.unidecode(STOP_WORDS[elem])
    STOP_WORDS = set(STOP_WORDS)

    text_clean = " ".join([token.lemma_ for token in nlp(text_clean) if (token.lemma_ not in STOP_WORDS) and (token.text not in STOP_WORDS)])
    
    # Load model
    classifier = joblib.load("models/classifier.joblib")
    # Load vectorizer
    vectorizer = joblib.load("models/vectorizer.joblib")   
    # Load label encoder
    label_encoder = joblib.load('models/label_encoder.joblib')       

    # TF-IDF vector
    print(text_clean)
    vectorized_sentence = vectorizer.transform([text_clean])
    # Predict
    prob = classifier.predict_proba(vectorized_sentence)
    predictions = np.argmax(prob,axis=1)

    predictions_texte = label_encoder.inverse_transform(predictions)
    # Return the result as JSON but first we need to transform the
    # result so as to be serializable by jsonify()
    predictions_texte = predictions_texte[0]
    
        #return jsonify({"predict": predictions_texte}), 200
    return render_template('layout2.html', prediction_text=predictions_texte)
    


if __name__ == "__main__":
    app.run(debug=True)