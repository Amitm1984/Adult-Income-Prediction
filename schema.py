from pydantic import BaseModel

class AdultIncome(BaseModel):
    age:int
    workclass:str
    fnlwgt:int
    education_num:int
    occupation:str
    race:str
    sex:str
    capital_gain:int
    capital_loss:int
    hours_per_week:int

    model_config = {
        "json_schema_extra":{
            "examples":[
                {
                    "age":38, "workclass":"Private", "fnlwgt":215646, "education_num":9,
                    "occupation":"Handlers-cleaners", "race":"White", "sex":"Male", "capital_gain":0,
                    "capital_loss":0, "hours_per_week":40
                }
            ]
        }
    }
