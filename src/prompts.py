FEW_SHOT_EXAMPLES_ASQA = """Given an ambiguous question, figure out its interpretations and answer them one by one. 
Question: Who played bonnie in gone with the wind? 
Answer: This question is ambiguous in terms of which version or adaptation of Gone with the Wind is being referred to. In order to figure out its interpretations, we need to consider different versions or adaptations of Gone with the Wind. Gone with the Wind has two versions or adaptations: the 1939 film Gone with the Wind or the 2008 musical Gone with the Wind. Therefore, this question has 2 interpretations: (1) Who played Bonnie in the 1939 film Gone with the Wind? (2) Who played Bonnie in the 2008 musical Gone with the Wind? The answers to all interpretations are: (1) The 1939 film Gone with the Wind’s character Bonnie was played by Eleanore Cammack "Cammie" King. (2) The 2008 musical Gone with the Wind’s character Bonnie was played by Leilah de Meza. 

Given an ambiguous question, figure out its interpretations and answer them one by one. 
Question: What is the second largest city in the usa? 
Answer: This question is ambiguous in terms of the criteria being used to determine the second largest city in the USA. In order to figure out its interpretations, we need to consider different criteria to determine a city’s size. City size can be measured by two criteria: population or area. Therefore, this question has 2 interpretations: (1) What is the second largest city in the USA by population? (2) What is the second largest city in the USA by area? The answers to all interpretations are: (1) The second largest city in the USA by population is Los Angeles, California. (2) The second largest city in the USA by area is Juneau, Alaska. 
"""

PROMPT = """{few_shot_examples}\n\nGiven an ambiguous question, figure out its interpretations and answer them one by one.\nQuestion: {question}\nAnswer: """

SYSTEM_INSTRUCTION = """Please act as an impartial judge and evaluate the quality of the response provided by an AI assistant to the user question displayed below. Your evaluation should consider factors such as the helpfulness, relevance, accuracy, depth, and level of detail of the response. Begin your evaluation by providing a short explanation. Be as objective as possible. After providing your explanation, please rate the response on a scale of 1 to 10 by strictly following this format: [[rating]], for example: Rating: [[5]].
"""

QA_REF = """[Question]
{question}

[The Start of Reference Answer]
{answer_ref}
[The End of Reference Answer]

[The Start of Assistant’s Answer]
{answer}
[The End of Assistant’s Answer]"""

QA = """[Question]
{question}

[The Start of Assistant’s Answer]
{answer}
[The End of Assistant’s Answer]"""

ANSEWER_RELEVANCE_ANTIQUE = """Generate a question for the given answer. Please provide questions following this format: [[Question]]

[[Answer]] Albert Einstein was born in Germany.

[[Question]] Where was Albert Einstein born?

Generate a question for the given answer. Please provide questions following this format: [[Question]]

[[Answer]] It can change its skin color based on the temperature of its environment.

[[Question]] What unique ability does the newly discovered species of frog have?

Generate a question for the given answer. Please provide questions following this format: [[Question]]

[[Answer]] The tallest mountain on Earth, measured from sea level, is a renowned peak located in the Himalayas.

[[Question]] What is the tallest mountain on Earth?

Generate a question for the given answer. Please provide questions following this format: [[Question]]

[[Answer]] I don't know about the  groundbreaking feature of the smartphone invented in 2023 as am unware of information beyond 2022.

[[Question]] What was the groundbreaking feature of the smartphone invented in 2023?

Generate a question for the given answer. Please provide questions following this format: [[Question]]

[[Answer]] {answer}
"""

ANSEWER_RELEVANCE = """Generate several questions for the given [[Answer]], noting that the [[Answer]] may cover multiple aspects. Please provide questions following this format: [[Question]]

[[Answer]] [John Sullivan sings the opening theme song to Only Fools and Horses, and Chas & Dave sing the closing theme song.","Only Fools and Horses.... is a British television sitcom created and written by John Sullivan. Only Fools and Horses has separate theme songs for the opening and closing credits, \"Only Fools and Horses\" and \"Hooky Street\", respectively. The tune was changed after the first series, and the new one was written by John Sullivan. Sullivan was persuaded to do it himself by Ray Butt. Chas & Dave did later contribute to the show, performing the closing credits song for the 1989 episode \"The Jolly Boys' Outing\".]

[[Question]] Who sings the original opening theme after the first series to Only Fools and Horses? Who sings the revise theme to only fools and horses? Who sings the closing theme in the episode \"The Jolly Boys' Outing\" of the series Only Fools and Horses?


Generate several questions for the given [[Answer]], noting that the [[Answer]] may cover multiple aspects. Please provide questions following this format: [[Question]]

[[Answer]] ["As of September 2021, all of the top 100 songs have exceeded 1.2 billion streams, of which eight have reached 2 billion streams, with Ed Sheeran's Shape of You ranked in the top position. The most played song on Spotify in a single week is 7 Rings by Ariana Grande with 16.9 million streams. The most played song on Spotify in a single day is All I Want for Christmas is You by Mariah Carey, which received 10.8 million streams in December 2018.","As of August 2021, Ed Sheeran's \"Shape of You\" is the most streamed song on Spotify with over 2 billion streams. 7 Rings by by American singer Ariana Grande, from her fifth studio album Thank U, Next, is the most played song for a single week, and a Christmas song by Mariah Carey \"All I Want for Christmas Is You\" is the most played song on a single day. "]

[[Question]] What is the most played song on Spotify (total plays)? What is the most played song ever on spotify in a single week? What is the most played song ever on spotify in a single day?


Generate several questions for the given [[Answer]], noting that the [[Answer]] may cover multiple aspects. Please provide questions following this format: [[Question]]

[[Answer]] ["Robert Wadlow, also known as the Alton Giant and the Giant of Illinois, was an American man who was the tallest person in recorded history for whom there is irrefutable evidence. Wadlow's height was 8 ft 11 in (2.72 m) at his death at age 22. Trijntje Keever, nicknamed De Groote Meid (in English, The Big Girl), is the tallest unconfirmed female person in recorded history, standing 9 Amsterdam feet or 2.49 metres (8 ft 2 in) tall at the time of her death at age seventeen. Zeng Jinlian was the tallest woman verified in modern times, surpassing Jane Bunford's record. In the year between Don Koehler's death and her own, she surpassed fellow \"eight-footers\" Gabriel Est\u00eav\u00e3o Monjane and Suleiman Ali Nashnush. Kristian Matsson is a singer-songwriter from Dalarna, Sweden, who performs under the stage name of The Tallest Man on Earth.","The tallest person on the Earth can mean different things. For instance, Kristian Matsson is a singer-songwriter from Dalarna, Sweden, who performs under the stage name of The Tallest Man on Earth. The actual tallest man in recorded history on the Earth was Robert Wadlow. The unconfirmed tallest woman on Earth in history was Trijntje Keever. The tallest woman in recorded history Zeng Jinlian."]

[[Question]] Who has the stage name the tallest person on the earth? Who is the tallest man in recorded history on the earth? Who is the unconfirmed tallest woman in history on the earth? Who is the tallest confirmed woman in recorded history on the earth?


Generate several questions for the given [[Answer]], noting that the [[Answer]] may cover multiple aspects. Please provide questions following this format: [[Question]]

[[Answer]] {answer}
"""

FG_SYSTEM = """Score the following llm output of a question answering task with respect to following aspects with 1 to 5 stars.

Accuracy: determine the accuracy of the answers, verifying the correctness and reliability of the provided information.
1 star means Incorrect information 
2 stars means Partially correct information 
3 stars means half correct information
4 stars means Mostly correct information 
5 stars means Perfectly correct information

Informativeness: examines whether the answers provide sufficient and meaningful information that useful to the user and relevant to the question.
1 star means No information or irrelevant information
2 star means Very little information
3 stars means Some information
4 stars means Enough information
5 stars means Highly informative

Begin your evaluation by providing a short explanation. Be as objective as possible. After providing your explanation, please provide your evaluation by strictly following the JSON format such as: [[SCORE]] {"accuracy": 2, "informativeness": 3}.
"""

QUERY_CATEGORY_SYSTEM = """The question is related to the category of {category}, which means it expects answers with "{category_description}" """


def gen_prompt(question, answer, ref=None, system_instruction=SYSTEM_INSTRUCTION, user_instruction=QA):
    if ref is not None:
        return [
            {"role": "system", "content": system_instruction.strip()},
            {"role": "user", "content": user_instruction.format(question=question, answer=answer, answer_ref=ref)}
        ]
    else:
        return [
            {"role": "system", "content": system_instruction.strip()},
            {"role": "user", "content": user_instruction.format(question=question, answer=answer)}
        ]
