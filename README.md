# chef-app
this is the future of COOKING-COPILOT APPS

### TASK LIST:
- [ ] Check whether the new_data & foodnet_data json files match. Then rewrite all the documents to a new vectorstore
- [ ] create fastAPI endpoints:

	- user should post a json containing : preferences(for metadata filtering) and ingredients
	- we will initalize vectorstore and perform similarity search with these data passed.
	- return the top 3 recipe suggestions to the user as json.

### NOTES:
-  the following columns have some missing values in some datasets:
  -  [servings, prep_time, cook_time, total_time] 
-  in the final step, the we need to instruction prompt GPT to fill these missing parts with logical values.

