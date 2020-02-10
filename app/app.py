# Dependencies
from sklearn.externals import joblib
from flask import Flask, request, jsonify, render_template
import pandas as pd


# Your API definition
app = Flask(__name__)

lr = joblib.load("model.pkl")  # Load "model.pkl"
print('Model loaded')

model_columns = joblib.load("model_columns.pkl")  # Load "model_columns.pkl"
print('Model columns loaded')


# kelly criterion
def kelly(odds, p):
    """ Kelly criterion formula outputs the fraction of your bankroll to bet depending on the odds predicted:
    f = fraction of the bankroll to bet
    b = decimal odds -1
    p = implied probability of our model
    q = probability of losing (1-p) """
    b = odds - 1
    f = (b * p - (1 - p)) / b
    return f


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # json_
    json_ = request.form.items()
    json_ = pd.DataFrame({x[0]: [x[1]] for x in json_})
    print(type(json_))
    print(json_)

    # dummy columns
    dummy_cols = ['home_team', 'away_team']

    # query
    query = pd.get_dummies(json_, columns=dummy_cols)
    query = query.reindex(columns=model_columns, fill_value=0)
    print(query)
    print(query.loc[0, :])

    # prediction
    prediction = lr.predict(query)
    output = round((prediction[0] * 100), 2)
    print(type(prediction))
    print(prediction)

    # implied home odds
    home_odds = float(json_['home_odds'][0])
    implied_home_odds = round(1 / home_odds * 100, 2)
    home_team = json_['home_team'][0]

    # kelly criterion
    kelly_stake = round((kelly(home_odds, prediction)*100/2)[0], 2)
    if kelly_stake >= 0:
        kelly_stake = kelly_stake
    else:
        kelly_stake = 0

    return render_template('index.html',
                           prediction_text='Probability of {} winning: {}% vs. House Odds of {}%'
                           .format(home_team, output, implied_home_odds),
                           kelly_text='Recommended Betting Stake: {}%'.format(kelly_stake))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
