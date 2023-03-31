from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from xgboost import XGBRegressor, XGBRFRegressor
from lightgbm import LGBMRegressor


def construct_model(opt):
    if opt == "LR":
        model = LinearRegression()
        GSparameters = None
    elif opt == "DTR":
        model = DecisionTreeRegressor(random_state=420)
        GSparameters = None
    elif opt == "RFR":
        model = RandomForestRegressor(
            random_state=420, n_estimators=150, min_samples_split=15  # 300,  # 125
        )
        GSparameters = {
            "model__n_estimators": [100, 150, 200],
            "model__min_samples_split": [10, 15, 25],
        }
    elif opt == "GBR":
        model = GradientBoostingRegressor(
            loss="absolute_error", min_samples_split=50, n_estimators=20000, alpha=0.05
        )
        GSparameters = {
            #'model__min_samples_split': [50,100,150],
            "model__n_estimators": [10000, 15000, 20000],
            #'model__alpha':[0.03,0.05,0.07],
        }
    elif opt == "XGB":
        model = XGBRegressor(
            n_estimators=4000,
            max_depth=5,
            eta=0.03,
            subsample=0.75,
            colsample_bytree=0.75,
            colsample_bylevel=0.75,
            colsample_bynode=0.75,
            random_state=43,
        )
        GSparameters = {
            #'model__n_estimators': [2500, 3000, 4000],
            #'model__max_depth': [3,5,7],
            #'model__eta':[0.01,0.03,0.05],
        }
    elif opt == "XGBRF":
        model = XGBRFRegressor(
            n_estimators=20000,
            max_depth=18,
            eta=0.015,
            subsample=0.78,
            # colsample_bytree=0.75,
            # colsample_bylevel=0.75,
            # colsample_bynode=0.75,
            random_state=420,
        )
        GSparameters = {
            #'model__n_estimators': [1000, 2000, 3000],
            #'model__max_depth': [17,18,20],
            #'model__eta':[0.01, 0.015, 0.02],
            "model__subsample": [0.75, 0.78, 0.80]
        }
    elif opt == "LGBM":
        model = LGBMRegressor(
            n_estimators=1000,
            max_depth=20,
            # learning_rate=0.025,
            subsample=0.75,
            num_iterations=10000,
            num_leaves=100,
            # colsample_bytree=0.75,
            # colsample_bylevel=0.75,
            # colsample_bynode=0.75,
            random_state=777,
        )
        GSparameters = {
            # 'model__learning_rate': [0.01, 0.015, 0.025, 0.03],
            # 'model__num_leaves': [100, 200, 300, 500, 1000],
            # 'model__n_estimators': [1000, 2000, 3000],
            # 'model__max_depth': [17,18,20,22],
            #'model__eta':[0.01, 0.015, 0.02],
            #"model__subsample": [0.75, 0.78, 0.80]
        }
    else:
        raise ValueError(f"model:{opt} option not defined")

    return model, GSparameters
