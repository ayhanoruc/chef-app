import os
import re
import pandas as pd
from typing import List

class Preprocessor:
    def __init__(self) -> None:
        print("preprocessor initialized")
        self.df = pd.DataFrame([])  # initialize an empty dataframe
        self.file_path = None

    def read_xlsx(self, file_path: str, features: List, index_col=False) -> None:
        try:
            sub_category = file_path.split("\\")[-1].split(".")[0]
            self.file_path = file_path

            # Read the Excel file into a DataFrame
            df = pd.read_excel(file_path , header=0, index_col=None)
            #print("OK")
            # Check if the column "ingredients" exists in the DataFrame and rename it if necessary
            if "ingredients" in df.columns:
                df.rename(columns={"ingredients": "recipe_ingredients"}, inplace=True)

            # Filter the DataFrame based on the specified features
            df = df[features]
            #print(df.columns)

            # Remove duplicated rows, if any
            df.drop_duplicates(inplace=True)

            # Remove rows with null values in "recipe_directions" column
            df.dropna(subset=["recipe_directions"], inplace=True)

            # Add a "sub_category" column derived from the file name
            df["sub_category"] = sub_category

            # Assign the final processed DataFrame to self.df
            self.df = df

            #print(df.info())
            
        except Exception as e:
            print("Error occurred while reading xlsx file: ", e)



    def df_to_json(self, path: str = None) -> None:
        """
        Converts a given record file in .xlsx format to JSON format.
        """
        if path is None:
            path = os.path.splitext(self.file_path)[0] + ".json"

        if self.df.empty:
            raise ValueError("DataFrame is empty. Please use read_xlsx to populate the DataFrame first.")

        self.df.to_json(path, orient="records", indent=4)
        print(f"JSON saved to {path}")



    def image_url_parser(self, recipe_card: str) -> str:
        pattern = r'https[^"]+\.jpg'
        #print(recipe_card)
        match = re.findall(pattern, recipe_card)
        if match:
            return match[0]
        return None


    def df_img_url_parser(self, col_name: str = "card") -> None:
        self.df["image_url_formatted"] = self.df[col_name].apply(self.image_url_parser)
        

    def recipe_tag_formatter(self) -> None:
        if "recipe_tags" not in self.df.columns:
            raise ValueError("The dataframe does not contain the 'recipe_tags' column.")

        self.df.drop(self.df[self.df["recipe_tags"].isnull()].index, inplace=True)  # remove rows with no recipe_tags
        
        self.df["recipe_tags_formatted"] = self.df["recipe_tags"].apply(lambda tags: [kv["recipe_tags"] for kv in eval(tags)])
        # Get the common sub_category value
        common_sub_category = self.df["sub_category"].iloc[0]
        
        # Append the common_sub_category to each list in the "recipe_tags_formatted" column
        self.df["recipe_tags_formatted"] = self.df["recipe_tags_formatted"].apply(lambda element: element + [common_sub_category])


    def details_table_formatter(self, table: List) -> dict:
        #print(eval(table))
        try:
            table_str = eval(table)[0]["recipe_details_table"]
        except:
            print("ERROR OCCURED for", table)
            return "None"
        
        # Split the details string based on both newline and ":"
        details_list = re.split(r'\n|:', table_str)

        # Remove empty strings and strip any leading/trailing whitespace
        table_detail_list = [detail.strip() for detail in details_list if detail.strip()]

        #print(table_detail_list)
        # Initialize a dictionary with specific keys and default values
        table_details_dict = {
            "Prep Time": "None",
            "Cook Time": "None",
            "Additional Time": "None",
            "Total Time": "None",
            "Servings": "None",
            "Yield": "None"
        }
        
        
        for index , item in enumerate(table_detail_list):
            #print(item)
            if item in table_details_dict:
                table_details_dict[item] = table_detail_list[index+1]

        
        return table_details_dict


    def recipe_details_table_formatter(self) -> None:
        if "recipe_details_table" not in self.df.columns:
            raise ValueError("The dataframe does not contain the 'recipe_details_table' column.")

        #self.df.drop(self.df[~self.df["recipe_details_table"].str.contains("Time")].index, inplace=True)  # remove rows not containing any time detail.

        #print(eval(self.df["recipe_details_table"].iloc[0])) List[dict[str, str]]
        self.df["recipe_details_formatted"] = self.df["recipe_details_table"].apply(lambda tags: [kv["recipe_details_table"] for kv in eval(tags)])
        # Convert "recipe_details_table" into a dictionary of key-value pairs
        self.df["recipe_details_formatted"] = self.df["recipe_details_table"].apply(lambda tags: self.details_table_formatter(tags))




    def ingredient_list_formatter(self, ingredients: List) -> List:
        """Assumes the list has 1 element, if it contains multiple elements, then just ' '.join()  them """
        #print(ingredients)
        try:
            ingredient_str = ingredients[0]
        except:
            return "None"
        ingredients_list = ingredient_str.split('\n')

        # Remove empty strings and strip any leading/trailing whitespace
        ingredients_list = [ingredient.strip() for ingredient in ingredients_list if ingredient.strip()]
        return ingredients_list


    def recipe_ingredients_formatter(self) -> None:
        if "recipe_ingredients" not in self.df.columns:
            #print("COLUMNS:  ", self.df.columns)
            raise ValueError("The dataframe does not contain the 'recipe_ingredients' column.")
        
        # Drop rows with None or empty ingredient lists
        self.df = self.df.dropna(subset=["recipe_ingredients"])
        self.df = self.df[self.df["recipe_ingredients"].apply(lambda x: len(eval(x)) > 0 if isinstance(x, str) else False)]

        #print("COLUMNS:  ", self.df.columns)

        try:
            self.df["recipe_ingredients_formatted"] = self.df["recipe_ingredients"].apply(lambda tags: [kv["recipe_ingredients"] for kv in eval(tags)])
            
        except Exception as e:
            print("Error during column transformation:", e)
            return "None"
        
        self.df["recipe_ingredients_formatted"] = self.df["recipe_ingredients_formatted"].apply(lambda ingredient_list: self.ingredient_list_formatter(ingredient_list))



    def recipe_directions_formatter(self) -> None:
        if "recipe_directions" not in self.df.columns:
            raise ValueError("The dataframe does not contain the 'recipe_directions' column.")

        self.df.drop(self.df[self.df["recipe_directions"].apply(lambda element: len(element)) <= 2].index, inplace=True)
        self.df["recipe_directions_formatted"] = self.df["recipe_directions"].apply(lambda tags: [kv["recipe_directions"] for kv in eval(tags)])




    def recipe_nutrition_formatter(self, nutrition_details: List) -> dict:
        #print(nutrition_details)
        nutrition_str = nutrition_details[0]
        nutrition_list = nutrition_str.split('\n')

        # Remove empty strings and strip any leading/trailing whitespace

        nutrition_list = [nutrition.strip() for nutrition in nutrition_list if nutrition.strip()]
        nutrition_info = {
            "calories": 0,
            "fat": 0,
            "carbs": 0,
            "protein": 0
        }

        for index , item in enumerate(nutrition_list):
            if item.lower() in nutrition_info:
                nutrition_info[item.lower()] = nutrition_list[index - 1]
            

        return nutrition_info


    def recipe_nutrition_details_formatter(self) -> None:
        if "recipe_nutrition_details" not in self.df.columns:
            raise ValueError("The dataframe does not contain the 'recipe_nutrition_details' column.")

        self.df.drop(self.df[self.df["recipe_nutrition_details"].apply(lambda element: len(element)) <= 2].index, inplace=True)
        self.df["recipe_nutrition_details_formatted"] = self.df["recipe_nutrition_details"].apply(lambda tags: [kv["recipe_nutrition_details"] for kv in eval(tags)])

        self.df["recipe_nutrition_details_formatted"] = self.df["recipe_nutrition_details_formatted"].apply(lambda element: self.recipe_nutrition_formatter(element))


    def clean_df(self, cols: List) -> None:
        # Check if the specified columns exist in the DataFrame
        non_existing_cols = [col for col in cols if col not in self.df.columns]
        
        if non_existing_cols:
            raise ValueError(f"The following columns do not exist in the DataFrame: {non_existing_cols}")
        
        # Drop the specified columns
        self.df.drop(cols, axis=1, inplace=True)
        print("Unwanted columns dropped successfully!")
        

def pipeline_preprocessor(file_path:str, features_to_use:List, unwanted_cols:List[str])->pd.DataFrame:
    preprocessor = Preprocessor()
    df = preprocessor.read_xlsx(file_path, features_to_use) # try to cover edgecases early, here
    preprocessor.df_img_url_parser() # add a early breaker if the column with embedded img_url (card) is not present additionally; if a row has no card, it will be skipped!
    preprocessor.recipe_tag_formatter() # add a early breaker if the column with embedded tags (recipe_tags) is not present + if a row has no tags, it will be skipped!
    preprocessor.recipe_details_table_formatter() # add a early breaker if the column with embedded details (recipe_details_table) is not present + if a row has no details, it will be skipped!
    preprocessor.recipe_ingredients_formatter() # first ensure the naming , then check data availability for each row  
    preprocessor.recipe_directions_formatter() # same procedures applies
    preprocessor.recipe_nutrition_details_formatter() # same procedures applies, check data availability for each row
    preprocessor.clean_df(unwanted_cols) 
    preprocessor.df_to_json() # turn each row-recipe into a json object
    return preprocessor.df

if __name__ == "__main__":
    features_to_use = ["card", "card-href", "sub_category", "recipe_name", "recipe_details_table","recipe_ingredients", "recipe_directions", "recipe_tags", "recipe_nutrition_details"]
    unwanted_cols = ["card","recipe_tags", "recipe_details_table", "recipe_ingredients", "recipe_directions", "recipe_nutrition_details","sub_category"]

    recipes_dir = r"C:\Users\ayhan\Desktop\ChefApp\artifacts\recipes\new_data\chineese"
    categories = os.listdir(recipes_dir)

    for category in [category for category in categories if category.endswith(".xlsx")]:
        path = os.path.join(recipes_dir, category) # ../breakfast/breakfast_breakfast-casseroles.xlsx
        print(path)
        pipeline_preprocessor(path, features_to_use, unwanted_cols)

    # OR ITERATE THRU CATEGORIES
    #recipes_dir = r"C:\Users\ayhan\Desktop\ChefApp\artifacts\recipes\new_data"

    """
    categories = os.listdir(recipes_dir)


    for category in categories:
        files = os.listdir(os.path.join(recipes_dir, category))

        for file in [file for file in files if file.endswith(".xlsx")]:
            path = os.path.join(recipes_dir, category, file)
            print(path)
            pipeline_preprocessor(path, features_to_use, unwanted_cols)
    """