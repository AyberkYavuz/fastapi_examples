from fastapi import FastAPI, APIRouter
from fastapi import Request
from pydantic import BaseModel
import pandas as pd
from utils.file_handler import PickleHandler
from utils.path_operations import get_working_directory

# loading the trained ml model
working_directory = get_working_directory()
pickle_handler = PickleHandler()

ml_model_path = working_directory + '/models/randomforest_iris_model.pickle'
production_machine_learning_model = pickle_handler.load_object(ml_model_path)

# loading the encoder model
iris_target_label_encoder_path = working_directory + '/models/iris_target_label_encoder.pickle'
iris_target_label_encoder = pickle_handler.load_object(iris_target_label_encoder_path)


class Flower(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class MyRouter(APIRouter):
    def __init__(self):
        super().__init__()

        self.add_api_route('/', self.get, methods=['GET'])
        self.add_api_route('/predict_class', self.get, methods=['GET'])
        self.add_api_route('/predict_class', self.post, methods=['POST'])

    async def __get_features_dataframe(self, flower: Flower):
        """
        Converts client request parameters to a pandas DataFrame object.

        Args:
            flower (Flower): A Pydantic model representing the flower attributes.

        Returns:
            features_dataframe (pandas.DataFrame): A pandas DataFrame object containing the input flower attributes.
        """
        sepal_length = flower.sepal_length
        sepal_width = flower.sepal_width
        petal_length = flower.petal_length
        petal_width = flower.petal_width

        features_values = [[sepal_length, sepal_width,
                            petal_length, petal_width]]

        feature_names = ["sepal_length", "sepal_width",
                         "petal_length", "petal_width"]
        features_dataframe = pd.DataFrame(features_values, columns=feature_names)
        return features_dataframe

    async def __get_prediction(self, features_dataframe: pd.DataFrame):
        """
        Generates a prediction for the given flower attributes.

        Args:
            features_dataframe (pandas.DataFrame): A pandas DataFrame object containing the input flower attributes.

        Returns:
            prediction (str): A string representing the predicted flower class.
        """
        prediction = production_machine_learning_model.predict(features_dataframe)[0]
        prediction = iris_target_label_encoder.inverse_transform([int(prediction)])[0]
        return prediction

    async def get(self, request: Request):
        return {"message": "Welcome to Machine Learning Model API!"}

    async def post(self, flower: Flower):
        features_dataframe = await self.__get_features_dataframe(flower)
        prediction = await self.__get_prediction(features_dataframe)
        return {"class": prediction}


app = FastAPI()

my_router = MyRouter()
app.include_router(my_router)
