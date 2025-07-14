NEXTSTEP_PROMPT = """You are a smart tool selector. I will provide you with some information extracted from an image, along with a list of available tool options for the next steps. Please choose the most suitable tool to obtain more information or generate a new image. 

The tool options are as follows: 
{options} 

Your response should consist of two parts:

1. **Thought:** Explain your reasoning behind how you decide to choose the next tool.
2. **Choice:** Provide the specific tool you have selected.

Here are some examples to help you understand the task.

{examples}

Now that you understand the approach and format for selecting tools, I will provide you with the necessary information. Please choose the next tool using the same format.

Information:
{context}
"""

# example format:
# Information:
# {tool_name}: {tool_output}

# Thought: {thought_choose}
# Choice: {choice} (1. ImageDescription)