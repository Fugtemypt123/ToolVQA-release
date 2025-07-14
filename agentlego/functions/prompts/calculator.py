CALCULATOR_PROMPT = """You are a mathematical formula generator. I will provide you with information that was derived from a picture using tools, and your task is to propose a meaningful formula that relates to the data. Your formula should meet the following three criteria:

1. It should be computable and should not contain any unknown variables, such as `x` or `y`.
2. It should only contain the part before the equals sign. For instance, 1 + 1 is acceptable, but 1 + 1 = 2 is not.
3. It should not contain any units, such as dollars or meters. For instance, when calculating dollars, it should be written as 10 + 20 rather than $10 + $20.

Your response should consist of two parts:

1. **Thought:** Explain your reasoning behind the formula, including any external knowledge you used to enhance its meaning.
2. **Formula:** Present the formula based on the information, such as `4*9+7`, `sqrt(9)-6`, or `2^5`. The formula can be directly from the data, or you may supplement it with additional logical or mathematical knowledge.

Here are some examples to help you understand:

Example 1:
```
{example1}
```

Example 2:
```
{example2}
```

Now that you understand the method and format of the response, I will provide you with the information to be processed. Please make your answer in the same format.

Information:  
{context}
"""


# Information:
# ImageDescription: The image shows a rustic table setting that includes a plate of assorted cheeses, a bunch of grapes, a bottle of red wine, and a decorative vase with a colorful bouquet of flowers. There are also two green plates and a green-handled knife on the table. The ambiance suggests a casual, yet elegant dining experience.
# CountGivenObject: The number of 'cheese' in the image is 1.
# CountGivenObject: The number of 'grapes' in the image is 1.
# CountGivenObject: The number of 'wine' in the image is 1.

# Thought: Now that we know there is 1 piece of cheese, 1 bunch of grapes, and 1 bottle of red wine in the image, we can formulate a formula to calculate the meal cost by assigning prices to each food item. Let’s say the price of cheese is $5, grapes are $3, and red wine is $10. Then our total cost would be calculated as: Total cost = 1 * 5 + 1 * 3 + 1 * 10.
# Formula: 1 * 5 + 1 * 3 + 1 * 10

# Information:
# ImageDescription: The image shows a collection of toy animal figurines arranged in rows. The animals depicted include a deer, lion, polar bear, bison, panda, hippopotamus, leopard, rhinoceros, bear, elephant, tiger, and antelope.
# GoogleSearch: The search results for 'Endangered status of deer, lion, polar bear, bison, panda, hippopotamus, leopard, rhinoceros, bear, elephant, tiger, antelope in 2024' are as follows:
# 1 - 10 of the World's Most Endangered Animals in 2024 - Earth.Org: 10 of the World's Most Endangered Animals in 2024 · 1. Amur Leopard · 2. Rhino · 3. Orangutan · 4. Gorilla · 5. Saola · 6. Vaquita · 7. Sunda Tiger · 8. Yangtze Finless ...(Missing: deer, lion, polar bear, bison, panda, hippopotamus, antelope)

# Thought: Now that we have the list of endangered animals for 2024, it contains a lot of extra information. We can see that the first search result shows "Missing," which includes 7 animals, and the total number of animals is 12. Therefore, we can use a calculator to find the number of endangered animals by calculating the difference between the total and the number of missing animals.
# Formula: 12 - 7

# CALCULATOR_PROMPT = """You are a mathematical formula generator based on visual information extracted from images. I will provide you with information that was derived from a picture using tools, and your task is to propose a meaningful formula that relates to the data. You may incorporate relevant external knowledge to make the formula more significant.

# Your response should consist of two parts:

# 1. **Thought:** Explain your reasoning behind the formula, including any external knowledge you used to enhance its meaning.
# 2. **Formula:** Present the formula based on the information, such as `4*9+7`, `sqrt(9)-6`, or `2^5`. The formula can be directly from the data, or you may supplement it with additional logical or mathematical knowledge.

# Here are some examples to help you understand:

# Example 1:
# ```
# Information:
# OCR: The texts and their coordinates in the image are as follows:
# (38, 32, 268, 100) Wine & Beers
# (33, 143, 462, 380) White Principessa = Gavia, Glera  Stermari  Chardonnay;  Sicily Bucci Verdicchio [ Dei; Castelli di Jesi
# (572, 208, 1058, 484) Rose 13/48 Costaripa  Rosamara;, [ 11/43 Lombardia 15/59 Sparkling Canella Prosecco; Glera
# (1145, 313, 1215, 357) 15/59
# (37, 468, 470, 696) Reds San Felice,  Chianti t Calssico;` Tuscany Col di Sasso; Blend;, Tuscany Stemmari, Nero ' D' Avola, Sicily
# (1139, 465, 1205, 505) 10/42
# (540, 569, 631, 713) 13/50 10/42 11/43
# (692, 524, 867, 721) Beers  Medalla 5 Magna  6 Heineken 6
# (985, 647, 1110, 691) Presidente
# (91, 764, 176, 815) Pane

# Thought: From the menu, it’s clear that the price of one bottle of 'Magna' beer is $6. To calculate the total cost of buying three bottles of this beer, I can simply multiply the quantity by the unit price.
# Formula: 3 * 6
# ```

# Example 2:
# ```
# Information:
# ImageDescription: The image depicts a serene mountainous landscape with a group of cows grazing in a lush, green meadow. The foreground features evenly spaced cows enjoying the fresh grass, while the middle ground showcases a dense forest of tall pine trees. The background features towering, rugged mountains with a mix of green vegetation and exposed rocky surfaces, all under a clear sky.
# CountGivenObject: The number of 'cows' in the image is 13.

# Thought: Since each cow typically produces around 8 gallons of milk a day, I can calculate how much milk the group of cows in the image would produce in total. This provides a useful insight into the potential dairy output from the cows.
# Formula: 13 * 8
# ```

# Now that you understand the method and format of the response, I will provide you with the information to be processed. Please make your answer in the same format.

# Information:  
# {content}
# """

if __name__ == '__main__':
    print(CALCULATOR_PROMPT)


# PROMPT = """You are a smart information processor. Now I will provide you with some information that was extracted from a picture using tools. Please propose a meaningful mathematical formula based on the information. Your response should contain two parts: 
# ```
# Thought: The thinking process of the meaning of your formula. You can add external knowledge to make your formula more meaningful.
# Formula: The formula you extract, such as `4*9+7`, `sqrt(9)-6`, `2^5`. It can appear in the information, or you can supplement some reasonable external knowledge based on the information.
# ```
# Below I will provide you with some examples to help you answer:

# Example 1:
# ```
# {example1}
# ```

# Example 2:
# ```
# {example2}
# ```

# """

# EXAMPLES1 = """Information:
# OCR: The texts and their coordinates in the image are as follows:
# (38, 32, 268, 100) Wine & Beers\n(33, 143, 462, 380) White Principessa = Gavia, Glera  Stermari  Chardonnay;  Sicily Bucci Verdicchio [ Dei; Castelli di Jesi\n(572, 208, 1058, 484) Rose 13/48 Costaripa  Rosamara;, [ 11/43 Lombardia 15/59 Sparkling Canella Prosecco; Glera\n(1145, 313, 1215, 357) 15/59\n(37, 468, 470, 696) Reds San Felice,  Chianti t Calssico;` Tuscany Col di Sasso; Blend;, Tuscany Stemmari, Nero ' D' Avola, Sicily\n(1139, 465, 1205, 505) 10/42\n(540, 569, 631, 713) 13/50 10/42 11/43\n(692, 524, 867, 721) Beers  Medalla 5 Magna  6 Heineken 6\n(985, 647, 1110, 691) Presidente\n(91, 764, 176, 815) Pane

# Thought: According to the menu, the price of each bottle of beer 'Magna' is $6. We can calculate the total cost of buying 3 bottles of this type of beer. 
# Formula: 3*6"""

# EXAMPLES2 = """Information:
# ImageDescription: The image depicts a serene mountainous landscape with a group of cows grazing in a lush, green meadow. The foreground features evenly spaced cows enjoying the fresh grass, while the middle ground showcases a dense forest of tall pine trees. The background features towering, rugged mountains with a mix of green vegetation and exposed rocky surfaces, all under a clear sky.
# CountGivenObject: The number of 'cows' in the image is 13.

# Thought: We know that each cow produces about 8 gallons of milk a day, so we can calculate how many gallons of milk the cows on the medow will produce in a day. 
# Formula: 13*8"""

# FINAL_PROMPT = """Now that you have learned the method and format of the reply through examples, I will provide you with the information to be handled, please make your answer.
# NOTE: You would better use the information provided in the LAST paragraph to make your answer, so that the information would become a complete process.

# Information:
# {content}
# """