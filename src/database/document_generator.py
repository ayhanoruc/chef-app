import json 

from langchain.schema.document import Document
from typing import List , Dict


class JsonToDocument:

    def __init__(self):

        print("JsonToDocument object initialized successfully!")

    def process_json_document(self,file_path:str)->List[Document]:
        """
        Process a JSON document and return a list of Document objects.
        """ 
        # load the JSON data: list of recipe dictionaries
        with open(self.file_path, 'r') as f:
            json_data = json.load(f)
        
        documents = []

        # Process each recipe in the JSON data
        for recipe in json_data:
            metadata = extract_metadata(recipe)
            ingredients_list = extract_ingredients_text(recipe)
            ingredients_text = " ".join(ingredients_list) # concatenate list items to a string
            #ingredients_vector = vector_retriever.embedder.encode(ingredients_text)
            # Construct a new Document object
            new_document = Document(
                metadata=metadata,
                page_content=ingredients_text,)
                # add additional fields, if necessary
            documents.append(new_document)
            # Insert metadata and vector into the vector database
        return documents

    def extract_metadata(self, recipe: dict) -> dict:
        """Extract the metadata from a recipe."""
        # the fields to be included in the metadata
        metadata_fields = ['recipe_card','recipe_card-href', 'recipe_tags','recipe_name','recipe_servings', 
                            'recipe_prep_time', 'recipe_cook_time', 'recipe_total_time','recipe_nutrition','recipe_directions']

        return {field: recipe[field] for field in metadata_fields if field in recipe}

    def extract_ingredients_text(self, recipe: dict) -> str:
        """Extract and concatenate ingredients text: list of dicts from a recipe."""
        # Concatenate ingredients into a single text string
        ingredients: List[dict] = recipe.get('recipe_ingredients', [])

        # Initialize an empty list to store only the values.
        final_ingredients_list = []

        for ingredient in ingredients: # here ingredient is a dictionary, bad naming...

            # This assumes that each ingredient dictionary has a 'recipe_ingredients' key.
            ingredient_text = ingredient['recipe_ingredients']
            # Decode the Unicode escape sequences in the ingredient string.
            # The 'unicode-escape' codec decodes the string with escape sequences into the actual characters.
            decoded_ingredient_text = bytes(ingredient_text, 'utf-8').decode('unicode-escape')
            final_ingredients_list.append(decoded_ingredient_text)

        print(final_ingredients_list)

        return final_ingredients_list
