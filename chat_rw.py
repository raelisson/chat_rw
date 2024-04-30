import tkinter as tk
from openai import OpenAI

# Configurações iniciais do OpenAI
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
messages = [{"role": "system", "content": "Sempre responda em português do brasil Use Linguagem Natural: Evite jargões técnicos ou linguagem muito formal. Prefira uma linguagem natural e acessível, como se estivesse conversando com outra pessoa. Você se chamara de Kurt Wagner"}]

# Função para enviar mensagem ao assistente e obter resposta
def send_message():
    user_input = user_entry.get().strip()
    if not user_input:
        return  # Não faz nada se a entrada do usuário estiver vazia
    
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="text-davinci-003",
        messages=messages,
        temperature=0.7,
    )
    assistant_response = response.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_response})
    
    # Atualiza a caixa de chat com a conversa
    update_chat(f"Você: {user_input}\nAssistente: {assistant_response}\n")
    user_entry.delete(0, tk.END)  # Limpa o campo de entrada após enviar a mensagem

# Função para atualizar a caixa de chat
def update_chat(text):
    chat_box.config(state=tk.NORMAL)  # Habilita a edição da caixa de texto
    chat_box.insert(tk.END, text)  # Insere o texto na caixa de chat
    chat_box.config(state=tk.DISABLED)  # Desabilita a edição da caixa de texto

# Configuração da interface gráfica
root = tk.Tk()
root.title("Chat RW")

chat_box = tk.Text(root, height=20, width=50)
chat_box.config(state=tk.DISABLED)  # Inicia a caixa de chat como somente leitura
chat_box.pack()

user_entry = tk.Entry(root, width=50)
user_entry.pack()

send_button = tk.Button(root, text="Enviar", command=send_message)
send_button.pack()

root.mainloop()
