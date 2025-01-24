## ASQA: Ambiguous Questions
PROMPT = """{few_shot_examples}\n\nGiven an ambiguous question, figure out its interpretations and answer them one by one.\nQuestion: {question}\nAnswer: """

# few shot examples

FEW_SHOT_EXAMPLES_ASQA = """Given an ambiguous question, figure out its interpretations and answer them one by one. 
Question: Who played bonnie in gone with the wind? 
Answer: This question is ambiguous in terms of which version or adaptation of Gone with the Wind is being referred to. In order to figure out its interpretations, we need to consider different versions or adaptations of Gone with the Wind. Gone with the Wind has two versions or adaptations: the 1939 film Gone with the Wind or the 2008 musical Gone with the Wind. Therefore, this question has 2 interpretations: (1) Who played Bonnie in the 1939 film Gone with the Wind? (2) Who played Bonnie in the 2008 musical Gone with the Wind? The answers to all interpretations are: (1) The 1939 film Gone with the Wind’s character Bonnie was played by Eleanore Cammack "Cammie" King. (2) The 2008 musical Gone with the Wind’s character Bonnie was played by Leilah de Meza. 

Given an ambiguous question, figure out its interpretations and answer them one by one. 
Question: What is the second largest city in the usa? 
Answer: This question is ambiguous in terms of the criteria being used to determine the second largest city in the USA. In order to figure out its interpretations, we need to consider different criteria to determine a city’s size. City size can be measured by two criteria: population or area. Therefore, this question has 2 interpretations: (1) What is the second largest city in the USA by population? (2) What is the second largest city in the USA by area? The answers to all interpretations are: (1) The second largest city in the USA by population is Los Angeles, California. (2) The second largest city in the USA by area is Juneau, Alaska. 
"""
