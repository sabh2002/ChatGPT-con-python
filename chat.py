import openai

openai.api_key = "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"

while True:

    pregunta=input("\nPreguntame lo que quieras: ")

    if pregunta=="salir":
        break

    respuesta=openai.Completion.create(engine="text-davinci-003",
                                        prompt=pregunta,
                                        max_tokens=2048,
                                        temperature=0)
    print(respuesta.choices[0].text)
