import json


class Readfile:

    @staticmethod
    def read_object(filepath):
        with open(filepath) as file:
            json_obj = json.load(file)
            dict_obj = {}
            for key,value in json_obj.items():
                dict_obj[key] = (value['loc_type'], value['loc_value'])
            return(dict_obj, dict_obj.keys())




