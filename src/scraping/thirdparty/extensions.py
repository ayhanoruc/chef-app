# FUNCTIONS AND DATASTRUCTURES RELATED TO WEBSCRAPING VIA CHROME EXTENSIONS
recipe_websites = [
    "https://tasty.co",
    "https://www.allrecipes.com/recipes-a-z-6735880", # allrecipes.com: a-z
    "https://www.allrecipes.com", # allrecipes.com for unique categorical search
    "https://www.foodnetwork.com", # for recipe categories.
    "https://www.bbcgoodfood.com/recipes" # huge!!!
]
italian_maintag_urls = [
    "https://www.allrecipes.com/recipes/16767/world-cuisine/european/italian/main-dishes/",

    "https://www.allrecipes.com/recipes/505/main-dish/pasta/spaghetti/",
    "https://www.allrecipes.com/recipes/250/main-dish/pizza/"
]

italian_single_urls = [
    "https://www.allrecipes.com/recipes/17551/world-cuisine/european/italian/drinks/",
    "https://www.allrecipes.com/recipes/1789/world-cuisine/european/italian/authentic/",
    "https://www.allrecipes.com/recipes/1790/world-cuisine/european/italian/soups-and-stews/",
    "https://www.allrecipes.com/recipes/1791/world-cuisine/european/italian/desserts/",
    "https://www.allrecipes.com/recipes/1793/world-cuisine/european/italian/appetizers/",
    "https://www.allrecipes.com/recipes/1800/world-cuisine/european/italian/salads/",
]

mexican_maintag_urls = [
  "https://www.allrecipes.com/recipes/1214/world-cuisine/latin-american/mexican/appetizers/",
  "https://www.allrecipes.com/recipes/1215/world-cuisine/latin-american/mexican/soups-and-stews/",
  "https://www.allrecipes.com/recipes/1217/world-cuisine/latin-american/mexican/desserts/",
  "https://www.allrecipes.com/recipes/17504/world-cuisine/latin-american/mexican/main-dishes/"

]
mexican_single_urls = [
  "https://www.allrecipes.com/recipes/1470/world-cuisine/latin-american/mexican/authentic/",
  "https://www.allrecipes.com/recipes/17513/world-cuisine/latin-american/mexican/salads/",
  "https://www.allrecipes.com/recipes/1216/world-cuisine/latin-american/mexican/main-dishes/burritos/"
]

chineese_maintag_urls = [
  "https://www.allrecipes.com/recipes/17135/world-cuisine/asian/chinese/main-dishes/",

]
chineese_single_urls = [
  "https://www.allrecipes.com/recipes/1899/world-cuisine/asian/chinese/appetizers/",
  "https://www.allrecipes.com/recipes/1900/world-cuisine/asian/chinese/soups-and-stews/",
  "https://www.allrecipes.com/recipes/22838/world-cuisine/asian/chinese/main-dishes/beef/",
  "https://www.allrecipes.com/recipes/1902/world-cuisine/asian/chinese/main-dishes/chicken/",
  "https://www.allrecipes.com/recipes/1901/world-cuisine/asian/chinese/main-dishes/pork/",
  "https://www.allrecipes.com/recipes/1903/world-cuisine/asian/chinese/main-dishes/seafood/"
]


middle_eastern_single_urls = [
  "https://www.allrecipes.com/recipes/15937/world-cuisine/middle-eastern/persian/",
  "https://www.allrecipes.com/recipes/1824/world-cuisine/middle-eastern/lebanese/",
  "https://www.allrecipes.com/recipes/1825/world-cuisine/middle-eastern/turkish/",
  "https://www.allrecipes.com/recipes/1826/world-cuisine/middle-eastern/israeli/",
  "https://www.allrecipes.com/recipes/16704/healthy-recipes/mediterranean-diet/"
]





url = italian_urls[0]

main_tag_sitemap = {
  "sitemap": {
    "_id": "Chinese-main_dishes",
    "startUrl": ["https://www.allrecipes.com/recipes/17135/world-cuisine/asian/chinese/main-dishes/"],
    "selectors": [
      {
        "id": "sub_tag",
        "linkType": "linkFromHref",
        "multiple": true,
        "parentSelectors": ["_root"],
        "selector": "a.taxonomy-nodes__link",
        "type": "SelectorLink"
      },
      {
        "id": "recipe_card",
        "linkType": "linkFromHref",
        "multiple": true,
        "parentSelectors": ["sub_tag"],
        "selector": "a.card--image-top, .tax-sc__recirc-list a",
        "type": "SelectorLink"
      },
      {
        "extractAttribute": "",
        "id": "recipe_tags",
        "parentSelectors": ["recipe_card"],
        "selector": "li:nth-of-type(n+2) .mntl-breadcrumbs__link span",
        "type": "SelectorGroup"
      },
      {
        "id": "recipe_name",
        "multiple": false,
        "parentSelectors": ["recipe_card"],
        "regex": "",
        "selector": "h1",
        "type": "SelectorText"
      },
      {
        "id": "recipe_img",
        "multiple": false,
        "parentSelectors": ["recipe_card"],
        "selector": "img#mntl-sc-block-image_1-0-1",
        "type": "SelectorImage"
      },
      {
        "id": "recipe_servings",
        "multiple": false,
        "parentSelectors": ["recipe_card"],
        "regex": "",
        "selector": "div:nth-of-type(5) div.mntl-recipe-details__value",
        "type": "SelectorText"
      },
      {
        "id": "recipe_prep_time",
        "multiple": false,
        "parentSelectors": ["recipe_card"],
        "regex": "",
        "selector": "div.mntl-recipe-details__item:nth-of-type(1) div.mntl-recipe-details__value",
        "type": "SelectorText"
      },
      {
        "id": "recipe_cook_time",
        "multiple": false,
        "parentSelectors": ["recipe_card"],
        "regex": "",
        "selector": "div:nth-of-type(2) div.mntl-recipe-details__value",
        "type": "SelectorText"
      },
      {
        "id": "recipe_total_time",
        "multiple": false,
        "parentSelectors": ["recipe_card"],
        "regex": "",
        "selector": "div:nth-of-type(4) div.mntl-recipe-details__value",
        "type": "SelectorText"
      },
      {
        "extractAttribute": "",
        "id": "recipe_nutrition",
        "parentSelectors": ["recipe_card"],
        "selector": "td.type--dog-bold",
        "type": "SelectorGroup"
      },
      {
        "extractAttribute": "",
        "id": "recipe_ingredients",
        "parentSelectors": ["recipe_card"],
        "selector": ".mntl-structured-ingredients__list-item p",
        "type": "SelectorGroup"
      },
      {
        "extractAttribute": "",
        "id": "recipe_directions",
        "parentSelectors": ["recipe_card"],
        "selector": ".mntl-sc-block-group--LI p",
        "type": "SelectorGroup"
      }
    ]
  }
}
single_url_sitemap = {
"sitemap": {
    "_id": "chineese-appetizers",
    "startUrl": ["https://www.allrecipes.com/recipes/1899/world-cuisine/asian/chinese/appetizers/"],
    "selectors":[
      {"id":"main_tag",
        "multiple":false,
        "parentSelectors":["_root"],
        "regex":"",
        "selector":"h1",
        "type":"SelectorText"},

      {"id":"recipe_card",
      "linkType":"linkFromHref",
      "multiple":true,
      "parentSelectors":["_root"],
      "selector":".tax-sc__recirc-list a",
      "type":"SelectorLink"},
      {
        "extractAttribute": "",
        "id": "recipe_tags",
        "parentSelectors": ["recipe_card"],
        "selector": "li:nth-of-type(n+2) .mntl-breadcrumbs__link span",
        "type": "SelectorGroup"
      },
      {
        "id": "recipe_name",
        "multiple": false,
        "parentSelectors": ["recipe_card"],
        "regex": "",
        "selector": "h1",
        "type": "SelectorText"
      },
      {
        "id": "recipe_img",
        "multiple": false,
        "parentSelectors": ["recipe_card"],
        "selector": "img#mntl-sc-block-image_1-0-1",
        "type": "SelectorImage"
      },
      {
        "id": "recipe_servings",
        "multiple": false,
        "parentSelectors": ["recipe_card"],
        "regex": "",
        "selector": "div:nth-of-type(5) div.mntl-recipe-details__value",
        "type": "SelectorText"
      },
      {
        "id": "recipe_prep_time",
        "multiple": false,
        "parentSelectors": ["recipe_card"],
        "regex": "",
        "selector": "div.mntl-recipe-details__item:nth-of-type(1) div.mntl-recipe-details__value",
        "type": "SelectorText"
      },
      {
        "id": "recipe_cook_time",
        "multiple": false,
        "parentSelectors": ["recipe_card"],
        "regex": "",
        "selector": "div:nth-of-type(2) div.mntl-recipe-details__value",
        "type": "SelectorText"
      },
      {
        "id": "recipe_total_time",
        "multiple": false,
        "parentSelectors": ["recipe_card"],
        "regex": "",
        "selector": "div:nth-of-type(4) div.mntl-recipe-details__value",
        "type": "SelectorText"
      },
      {
        "extractAttribute": "",
        "id": "recipe_nutrition",
        "parentSelectors": ["recipe_card"],
        "selector": "td.type--dog-bold",
        "type": "SelectorGroup"
      },
      {
        "extractAttribute": "",
        "id": "recipe_ingredients",
        "parentSelectors": ["recipe_card"],
        "selector": ".mntl-structured-ingredients__list-item p",
        "type": "SelectorGroup"
      },
      {
        "extractAttribute": "",
        "id": "recipe_directions",
        "parentSelectors": ["recipe_card"],
        "selector": ".mntl-sc-block-group--LI p",
        "type": "SelectorGroup"
      }
    ]
  }
}


