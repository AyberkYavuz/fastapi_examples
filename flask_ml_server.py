from flask import Flask
from flask import request
from flask.views import MethodView
import pandas as pd
import random
import string
import json
from utils.path_operations import get_working_directory
from utils.file_handler import PickleHandler


working_directory = get_working_directory()
pickle_handler = PickleHandler()


def create_random_aplhanumeric_string():
    token = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(18))
    return token


app = Flask(__name__)
app.secret_key = create_random_aplhanumeric_string()

# loading the trained ml model
ml_model_path = working_directory + '/models/randomforest_iris_model.pickle'
production_machine_learning_model = pickle_handler.load_object(ml_model_path)

# loading the encoder model
iris_target_label_encoder_path = working_directory + '/models/iris_target_label_encoder.pickle'
iris_target_label_encoder = pickle_handler.load_object(iris_target_label_encoder_path)


class MachineLearningModelAPI(MethodView):
    """API for '/predict_class' url.
    """
    def get(self):
        """Handles GET requests for '/predict_class' url.
        Returns:
            message: tuple. Welcome message.
        """
        message = "Welcome to Machine Learning Model API!", 200
        return message

    def __get_features_dataframe(self):
        """Converts client request parameters to features_dataframe
        Returns:
            features_dataframe: dataframe. It will be used for producing prediction.
        """
        sepal_length = float(request.form["sepal_length"])
        sepal_width = float(request.form["sepal_width"])
        petal_length = float(request.form["petal_length"])
        petal_width = float(request.form["petal_width"])

        features_values = [[sepal_length, sepal_width,
                            petal_length, petal_width]]

        feature_names = ["sepal_length", "sepal_width",
                         "petal_length", "petal_width"]
        features_dataframe = pd.DataFrame(features_values, columns=feature_names)
        return features_dataframe

    def post(self):
        """Handles POST requests for '/predict_class' url.
        Returns:
            message: tuple. Server response to clients.
        """
        print("MachineLearningModelAPI POST Method")
        message = None
        parameter_list = ["sepal_length", "sepal_width",
                          "petal_length", "petal_width"]
        result_list = []
        for parameter in parameter_list:
            result = parameter not in request.form
            result_list.append(result)
        condition = True in result_list
        print(condition)
        if condition:
            message = "422", 422
        else:
            try:
                print("Converting client request parameters to features_dataframe.")
                features_dataframe = self.__get_features_dataframe()
                features_dataframe = features_dataframe.astype(float)
                print("Making a prediction.")
                prediction = production_machine_learning_model.predict(features_dataframe)[0]
                prediction = iris_target_label_encoder.inverse_transform([int(prediction)])[0]
                print(prediction)
                message = json.dumps({"class": prediction})
            except Exception as ex:
                print("Exception : " + str(ex))
                message = "Something went wrong!", 500
        return message


machine_learning_model_view = MachineLearningModelAPI.as_view('machine_learning_model_api')
app.add_url_rule('/predict_class', view_func=machine_learning_model_view, methods=['POST', 'GET'])

if __name__ == "__main__":
    app.run(debug=True)

