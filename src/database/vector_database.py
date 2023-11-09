from typing import List, Tuple, Union
import json 
from langchain.schema.document import Document
from langchain.embeddings import HuggingFaceEmbeddings, SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
from typing import List,Tuple ,Union, Any, Dict
import os 
import ast
from src.database.document_generator import JsonToDocument




class VectorRetriever:

    def __init__(self, model_name: str, model_kwargs: dict, encode_kwargs: dict, overwrite: bool = False) -> None:
        """
        pass overwrite = True when creating the vector store for the first time and if you want to overwrite intentionally.
        pass overwrite = False otherwise.
        """
        
        # we can pass different vector stores instead of built-in implemented-Chroma option. but this may require further consideration.
        self.vector_store = None
        self.model_name = model_name
        self.model_kwargs = model_kwargs
        self.encode_kwargs = encode_kwargs
        self.embedder = self.initialize_embedding_func()
        self.overwrite = overwrite
        

    def initialize_embedding_func(self):
        """
        Initializes the embedding function.

        :return: The initialized HuggingFaceEmbeddings object.
        """
        hf = HuggingFaceEmbeddings(
        model_name=self.model_name,
        model_kwargs=self.model_kwargs,
        encode_kwargs=self.encode_kwargs)

        embedding_dimension = hf.dict()['client'][1].get_config_dict()["word_embedding_dimension"]
        print("embedder initialized with dimension: ", embedding_dimension)

        return hf

    def initialize_vector_store(self, persist_directory:str,collection_name:str, documents:List[Document]=None,):
        """
        Initializes a Chroma vector store with the given texts and collection name and saves it to the persist_directory.

        Args:
            persist_directory (str): The directory to persist the vector store.
            texts (List[str]): The list of texts to be stored in the vector store.
            collection_name (str): The name of the collection.

        Returns:
            Chroma: The initialized Chroma vector store.
        """
        if self.overwrite:
            if os.path.exists(persist_directory) and os.path.isdir(persist_directory):
                print("persist directory already exists")
            else: 
                os.mkdir(persist_directory, exist_ok=True)
                print("persist directory created")
        
            self.vector_store = Chroma.from_documents(
                        documents =documents , 
                        embedding=self.embedder,
                        collection_name= collection_name,
                        persist_directory=persist_directory)

            self.vector_store.persist()
        
        else:
            #vectordb:Chroma = Chroma(persist_directory=persist_directory, embedding_function=self.embedder)
            self.vector_store = Chroma(persist_directory=persist_directory, embedding_function=self.embedder, collection_name=collection_name)
            
            

        print("vector store initialized successfully!")

    @staticmethod
    def drop_duplicates(raw_text_list):
        return list(set(raw_text_list))

    def similarity_search(self, query: Union[str, List[str]], k:int = 3 )->List[Tuple[str, float]]:

        """
        Performs a similarity search on the given query.

        Parameters:
        - query (Union[str, List[str]]): The query to search for. It can be either a single string or a list of strings.
        - k (int): The number of results to return. Default is 3.

        Returns:
        - List[Tuple[str, float]]: A list of tuples containing the similarity scores and their corresponding results.
        """
                
        if isinstance(query, list):
            query = "-".join(query) # concatenate list items to a string

        if isinstance(query, str):
            results = self.vector_store.similarity_search_with_relevance_scores(query, k=k) # ADD filter by metadata option
            print(type(results))
            return results

        else: 
            raise ValueError("query must be a string or a list of strings")

         ### ADD METADATA FILTERING, CHANGE THE LOGIC BELOW
        """
        # If a metadata filter is provided, apply the filter to the results
        if metadata_filter:
            filtered_results = []
            for result in results:
                document_id, _ = result
                document_metadata = self.vector_store.get_metadata(document_id)
                if all(document_metadata.get(key) == value for key, value in metadata_filter.items()):
                    filtered_results.append(result)
            return filtered_results
        return results
        """   



    def add_new_documents(self,documents:List[Document])->List[str]:
        """Adds a new document to the vector store."""
        ids= self.vector_store.add_new_documents(documents)
        self.vector_store.persist()
        print("new documents added to the vector store ids:", ids)
        return ids






    # Now, you need to implement the add_new_document method in VectorRetriever class to handle the metadata and vector insertion



if __name__ == "__main__":

    #1. Initialize your vector retriever with the appropriate model and arguments.
    #2. Initialize the JsonToDocument class.
    #3. specify the json_file_path
    #4. Process the JSON file to create a list of Document objects.
    #5. Initialize the vector store, if it's the first time or if you want to overwrite.
        # This step is usually done once, not every time you add new documents.

    #6. Add the new documents to the vector store.
        # This step is repeated every time you have new documents to add.

    #---------SEARCH---------
    #7. specify the ingredients list , concatanate it and pass it as a search query, 
    #8. Use the VectorRetriever to perform a similarity search with the query
    #9. Print the results

    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': False}


    persist_directory = r"C:\Users\ayhan\Desktop\ChefApp\artifacts\vector_db"
    os.makedirs(persist_directory, exist_ok=True)
    collection_name= "recipe_vdb"

    json_file_path = r"C:\Users\ayhan\Desktop\ChefApp\artifacts\recipes\cusine\italian\italian-desserts.json"

    vector_retriever = VectorRetriever(model_name = model_name, model_kwargs= model_kwargs, encode_kwargs=encode_kwargs, overwrite=False)
    
    json_to_document = JsonToDocument()

    #single document
    #documents = json_to_document.process_json_document(file_path=json_file_path)

    recipes_dir_1 = r"C:\Users\ayhan\Desktop\ChefApp\artifacts\recipes"
    recipes_dir_2 = r"C:\Users\ayhan\Desktop\ChefApp\artifacts\cusine"

    """ 
    categories_1 = os.listdir(recipes_dir_1)
    categories_2 = os.listdir(recipes_dir_2)
    documents = []

    for category in categories_1:
        file_names = [name for name in  os.listdir(os.path.join(recipes_dir_1,category)) if name.endswith(".json")]
        print(category,"/////////////////////")
        for file in file_names:
            
            json_file_path = os.path.join(recipes_dir_1,category,file)
            documents.extend(json_to_document.process_json_document(file_path=json_file_path))

    # recipes from cusine folder
    for category in categories_2:
        file_names = [name for name in  os.listdir(os.path.join(recipes_dir_2,category)) if name.endswith(".json")]
        print(category,"/////////////////////")
        for file in file_names:
            
            json_file_path = os.path.join(recipes_dir_2,category,file)
            documents.extend(json_to_document.process_json_document(file_path=json_file_path))


    print(len(documents),"documents found!", type(documents)) # created database from 12456 documents in 165 seconds. 
    """

    # since overwrite is set to False, it will initialize the vector store as retriever.pass documents=None
    vector_retriever.initialize_vector_store(persist_directory=persist_directory, documents=None, collection_name=collection_name)
    
    ingredients_list = ["2 cups of flour", "1 cup of sugar", "1 teaspoon of vanilla extract"]
    search_query = ' '.join(ingredients_list)
    
    results = vector_retriever.similarity_search(query=qry, k=10)
    #we can use:  filter (Optional[Dict[str, str]]) – Filter by metadata. Defaults to None.
    
    #[result[0].page_content for result in results]
    #result = list of tuples: each tuple contains a document and its similarity score,
    # each document is a tuple of (page_content, metadata)
    print([result[0].page_content for result in results] )
    print("\n\n")
    print(results[0][0].metadata.__dir__())
    print(results[0][0].metadata.keys())
    print(results[0][0].metadata.get("recipe_name"), end="\n")
    print([result[0].metadata.get("recipe_card-href") for result in results])
    print("DONE")





