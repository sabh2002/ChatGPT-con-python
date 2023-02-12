import openai

openai.api_key = "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"

def preguntas():
    while True:

        pregunta=input("\nPreguntame lo que quieras: ")

        if pregunta=="salir":
            break

        respuesta=openai.Completion.create(engine="text-davinci-003",
                                            prompt=pregunta,
                                            max_tokens=2048,
                                            temperature=0)
        return respuesta.choices[0].text

def imagenes():
    while True:

        imagen=input("\nQue imagen quieres crear: ")

        if imagen=="salir":
            break

        respuesta=openai.Image.create(prompt=imagen,
                                        n=2,
                                        size="1024x1024")
        print(respuesta.data[0].url)

while True:
    print("""
    1)Pregunta
    2)Imagen
    3)Salir""")
    op=int(input(">"))

    if op==1:
        preguntas()
    
    elif op==2:
        imagenes()
    
    elif op==3:
        break
