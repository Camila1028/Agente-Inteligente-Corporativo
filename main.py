from src.loader import cargar_documentos
from src.splitter import dividir_documentos
from src.embeddings import crear_embeddings
from src.vectorstore import crear_vectorstore
from src.retriever import crear_retriever
from src.chat import crear_chat
from src.prompt import crear_prompt
from src.agent import crear_agente

# 1. Cargar documentos
documentos = cargar_documentos("documento_base.csv")

# 2. Dividir documentos
chunks = dividir_documentos(documentos)

# 3. Crear embeddings
embeddings = crear_embeddings()

# 4. Crear FAISS
vectorstore = crear_vectorstore(chunks, embeddings)

# 5. Crear retriever
retriever = crear_retriever(vectorstore)

# 6. Crear modelo de chat
chat = crear_chat()

# 7. Crear prompt
prompt = crear_prompt()

# 8. Crear cadena RAG
agente = crear_agente(chat, retriever, prompt)

print("=" * 60)
print("🤖 Lignum Atelier")
print("Asistente Inteligente Corporativo")
print("=" * 60)
print("Escribe 'salir' para finalizar la conversación.\n")

while True:

    pregunta = input("👤 Tú: ")

    if not pregunta.strip():
        print("\n⚠️ Por favor escribe una consulta.\n")
        continue


    if "salir" in pregunta.lower():
        print("\n🤖 Gracias por utilizar el Asistente Inteligente de Recursos Humanos de Lignum Atelier.")
        print("¡Hasta pronto!")
        break
    try:
        respuesta = agente.invoke(pregunta)

        print("\n🤖 Asistente:\n")
        print(respuesta)

    except Exception as e:
        print("\n⚠️ Ocurrió un error al procesar tu consulta.")
        print("Por favor, intenta nuevamente.")
        # Si quieres ver el error durante el desarrollo, descomenta la siguiente línea:
        # print(e)

    print("\n" + "-" * 60 + "\n")