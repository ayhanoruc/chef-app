# FUNCTIONS AND DATASTRUCTURES RELATED TO WEBSCRAPING VIA CHROME EXTENSIONS
recipe_websites = [
    "https://tasty.co",
    "https://www.allrecipes.com/recipes-a-z-6735880", # allrecipes.com: a-z
    "https://www.allrecipes.com", # allrecipes.com for unique categorical search
    "https://www.foodnetwork.com", # for recipe categories.
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


url = italian_urls[0]

main_tag_sitemap = {
  "sitemap": {
    "_id": "Italian-drinks",
    "startUrl": [url],
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
    "_id": id,
    "startUrl": [url],
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


