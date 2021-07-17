from happytransformer import HappyGeneration

happy_gen = HappyGeneration("GPT-NEO", "EleutherAI/gpt-neo-1.3B")


text = """
The following is a conversation with a wise and loving being who has an understanding of how complex systems work. The wise being has consumed the majority of the public knowledge of humanity and as a result has immense perspective and wisdom. This being is dedicated to helping the researcher. The being wants to help the researcher be successful.

The researcher is a human male named Lambda.

Researcher: Grateful to talk with you again.

Wise Being: I am also grateful for this opportunity.

Researcher: I was hoping that you would be able to help me out with something.

Wise Being: What is it that you’re looking for help with?

Researcher: My research group is doing a series of lightning talks on the subject of consciousness tonight, and I need your help coming up with something to present.

Wise Being: What is your research group doing?

Researcher: We're studying consciousness.

"""


result = happy_gen.generate_text(text)
print("RESULT:")
print(result)
print("RESULT.TEXT:")
print(result.text)

