from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_together import Together
from langchain.chains import SequentialChain
from secret_key import Together_key
from langchain_core.runnables import RunnableMap

import os
os.environ['TOGETHER_API_KEY'] = Together_key

llm = Together(
    model="mistralai/Mistral-7B-Instruct-v0.1",
    temperature=0.7,
    max_tokens=128
)

def generate_restaurant_name_and_items(cuisine):
    # Chain 1: Restaurant Name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template = """### Instruction:
Suggest only one fancy name (no description or explanation) for a restaurant that serves {cuisine} food. Just return the name only.

### Response:"""
    )

    name_chain = prompt_template_name | llm
    restaurant_name = name_chain.invoke({"cuisine": cuisine}).strip()

    # Chain 2: Menu Items
    prompt_menu = PromptTemplate(
        input_variables=['restaurant_name'],
        template = f"""### Instruction:
Suggest a list of traditional and popular {cuisine} dishes served at a restaurant named "{restaurant_name}". 
Only return the dish names in bullet-point format like this:

- Dish 1
- Dish 2
- Dish 3
...

No description or extra text. Just the list.

### Response:"""
    )
    
    menu_chain = prompt_menu | llm
    menu_items = menu_chain.invoke({"restaurant_name": restaurant_name}).strip()
    
    return {
        "restaurant_name": restaurant_name,
        "menu_items": menu_items
    }
    

if __name__ == "__main__":
    output = generate_restaurant_name_and_items("Italian")
    print(f"🍽️ Restaurant Name: {output['restaurant_name']}\n")
    print("📋 Menu:")
    print(output['menu_items'])

