import json
import os 


#recursively convert None to 'null'
def replace_null(obj):
    if isinstance(obj, dict):
        return {k: replace_null(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [replace_null(v) for v in obj]
    elif obj is None:
        return 'null'
    else:
        return obj






recipes_dir = r"C:\Users\ayhan\Desktop\ChefApp\artifacts\cusine"

categories = os.listdir(recipes_dir)

for category in categories:

    file_names = [name for name in  os.listdir(os.path.join(recipes_dir,category)) if name.endswith(".json")]
    print(category,"/////////////////////")
    for file in file_names:
        #print(file)
        json_file_path = os.path.join(recipes_dir,category,file)
        with open(json_file_path, 'r') as file:
            data = json.load(file)

        data = replace_null(data)
        with open(json_file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print("done")
