# chef-app
this is the future of COOKING-COPILOT APPS

### TASK LIST:
- [] make ensure that the metadata in the vectorstore contains: cusine, mealtype, dietry type, cooking skill levels if exists.
    - we have to design the metadata structure in a proper filtering format for langchain filter.(gte, equals, lte , contains etc)
    - when scraping data, makesure the datastructure contains:
      - recipe_name, recipe_link , recipe_image_url, main_tag[cusine, mealtype, dietry type etc], sub_tags[cusine, mealtype, dietry type etc],
        total_calory, detailed_nutrition_info, [total_time, cook_time, prep_time, additional_time, servings]: may be we should scrape the table 
        as a single element than parse and convert them into numeric format to make ready for filtering later, via regex. 

<<<<<<< HEAD
- [X] data scraping :
=======
- [ ] data scraping :
    - recipe nutrition_details'i empty olan satırları dahil etme.
>>>>>>> 086789daf9015b49e808d2b17a56a7e6d56b3ce7
    - open 10 opera tabs, open webscraping import sitemap tabs
    - for each url and its type: main or single , generate individual sitemaps.
    - for each opened tab, just import these sitemaps and start the scraping asyncly: 20 (2window*10tabs)tabs -> 400 recipes/min -> 24k recipes/hr
												  
- [ ] create fastAPI endpoints:

	- user should post a json containing : preferences(for metadata filtering) and ingredients
	- we will initalize vectorstore and perform similarity search with these data passed.
	- return the top 3 recipe suggestions to the user as json.

### NOTES:
-  the following columns have some missing values in some datasets:
  -  [servings, prep_time, cook_time, total_time] 
-  in the final step, the we need to instruction prompt GPT to fill these missing parts with logical values.

