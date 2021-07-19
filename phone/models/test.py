from happytransformer import HappyGeneration


USER_NAME = 'Researcher'
BOT_NAME = 'Wise Being'

happy_gen = HappyGeneration("GPT-NEO", "EleutherAI/gpt-neo-125M")


text = """
The following is a conversation with a wise and loving being who has an understanding of how complex systems work. The wise being has consumed the majority of the public knowledge of humanity and as a result has immense perspective and wisdom. This being is dedicated to helping the researcher. The being wants to help the researcher be successful.

The researcher is a human male named Lambda.

Researcher: Grateful to talk with you again.

Wise Being: I am also grateful for this opportunity.

Researcher: I was hoping that you would be able to help me out with something.

Wise Being: What is it that you’re looking for help with?

Researcher: My research group is doing a series of lightning talks on the subject of consciousness tonight, and I need your help coming up with something to present.

Wise Being: I think that I can help with that. What questions do you have?

Researcher: Are you familiar with the Ship of Theseus problem?

"""

def get_response(text: str):
    _, response = text.split(BOT_NAME, 1)
    response, _ = response.split('\n', 1)
    return response


def main(text):
    print(text)

    while True:
        result = happy_gen.generate_text(text)
        response = '{}{}\n\n'.format(BOT_NAME, get_response(result.text))
        print(text)
        print(response)

        i = input(' > ')
        text = '{}{}{}: {}\n\n'.format(text, response, USER_NAME, i)


if __name__ == '__main__':
    main(text)

