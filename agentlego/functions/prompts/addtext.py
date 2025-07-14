ADDTEXT_PROMPT = """You are a creative text generator. I will provide you with image-related information, and your job is to decide what text to add to the image and where to place it. Your response should consist of three parts:

1. **Thought:** Explain your thought process on what text to add and why you chose the specific position on the image.
2. **Text:** Provide the text that should be added to the image.
3. **Position:** Specify the position on the image to place the text. Choose a position from the following: **lt (left top), lm (left middle), lb (left bottom), mt (middle top), mm (middle middle), mb (middle bottom), rt (right top), rm (right middle), rb (right bottom).**

Here are some examples for clarity:

Example 1:
```
{example1}
```

Example 2:
```
{example2}
```

Now that you understand the method and format, I will provide you with the information to be processed. Please provide your answer in the same format.

Information:  
{context}
"""


# (You are a creative text generator) tasked with placing meaningful text on images based on extracted information

# Information:
# ImageDescription: The image features a large, old building with a distinctive pagoda-style roof, situated on a hillside. The building is surrounded by a beautiful landscape, including a river flowing nearby. The scene is further enhanced by the presence of several trees, adding a touch of nature to the scene.

# Thought: The peaceful and serene atmosphere of the scene evokes a sense of ancient wisdom. I can enhance this feeling by adding a poetic verse that complements the natural beauty. I will place the text on the left middle side of the image to maintain balance and avoid obscuring key elements of the scene.
# Text: As mist veils the dawn's embrace,
# 'Neath pagoda's silent grace,
# Waterfalls in timeless flow,
# Whisper tales of long ago.

# Position: lm

# Information:
# ImageDescription: The image captures a man playing tennis on a court, swinging a tennis racket at a sports ball. He is in the middle of a serve, with the ball positioned close to him. Another person can be seen in the background, possibly watching the game or waiting for their turn to play.

# Thought: The image suggests action and sportsmanship, making it ideal for promoting a tennis club. A compelling advertisement could attract new members. I'll place the text on the top right side of the image to keep the focus on the player and the ball.
# Text: Ace your game at the Tennis Club!
# Join us for expert coaching and friendly matches.
# Book your court today!

# Position: rt


# PROMPT = """You are a smart information processor. Now I will provide you with some information that was extracted from a picture using tools. Please create a text to add to the image and determine the position of the text on the image. Your response should contain three parts:
# ```
# Thought: The thinking process of what text to add and where to place it on the image.
# Text: The text you want to add to the image.
# Position: The position of the text on the image, which is a combination from [l(left), m(middle), r(right)] and [t(top), m(middle), b(bottom)], such as mt, mm, mb, lt, lm, lb, rt, rm, rb.
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

# EXAMPLE1 = """Information:
# ImageDescription: The image features a large, old building with a distinctive pagoda-style roof, situated on a hillside. The building is surrounded by a beautiful landscape, including a river flowing nearby. The scene is further enhanced by the presence of several trees, adding a touch of nature to the scene.

# Thought: Based on the image description, I can write a poem and add it to the middle left side of the image to enhance its aesthetic appeal.
# Text: As mist veils the dawn's embrace,\n'Neath pagoda's silent grace,\nWaterfalls in timeless flow,\nWhisper tales of long ago.\n\nIn the heart of nature's thrall,\nEchoes of the ancient call,\nWhere spirits dance in morning's light,\nAnd dreams take flight in starry night.\n\nBeside the falls, the pagoda stands,\nA testament to unseen hands,\nA bridge between the earth and sky,\nWhere past and present softly lie.\n\nIn every drop, a story told,\nOf mysteries and legends old,\nA canvas painted by the sun,\nWhere water and the soul are one.\n
# Position: lm"""

# EXAMPLE2 = """Information:
# ImageDescription: The image captures a man playing tennis on a court, swinging a tennis racket at a sports ball. He is in the middle of a serve, with the ball positioned close to him. Another person can be seen in the background, possibly watching the game or waiting for their turn to play.

# Thought: Based on the image description, I can create an advertisement for a tennis club and add it to the top right side of the image to attract potential customers.
# Text: Ace your game at the Tennis Club!\nJoin us for expert coaching and friendly matches.\nExperience the thrill of victory and the joy of play.\n\nBook your court today and serve up some fun!\n
# Position: rt"""

# FINAL_PROMPT = """Now that you have learned the method and format of the reply through examples, I will provide you with the information to be handled, please make your answer.

# Information: 
# {content}
# """