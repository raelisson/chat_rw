import tkinter as tk
from openai import OpenAI

# Configurações iniciais do OpenAI
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
messages = [{"role": "system", "content": "Sempre responda em português do Brasil. Use linguagem natural. Você se chamara de Kurt Wagner"}]

# Função para enviar mensagem ao assistente e obter resposta
def send_message():
    user_input = user_entry.get().strip()
    if not user_input:
        return  # Não faz nada se a entrada do usuário estiver vazia
    
    messages.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(
        model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
        messages=messages,
        temperature=0.7,
    )
    
    assistant_response = response.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_response})
    
    # Atualiza a caixa de chat com a resposta do assistente
    update_chat(f"\n\nVocê: {user_input}\n\nAssistente: {assistant_response}\n\n")
    user_entry.delete(0, tk.END)  # Limpa o campo de entrada após enviar a mensagem

# Função para atualizar a caixa de chat
def update_chat(text):
    chat_box.config(state=tk.NORMAL)  # Habilita a edição da caixa de texto
    chat_box.insert(tk.END, text, "bold")  # Insere o texto na caixa de chat em negrito
    chat_box.config(state=tk.DISABLED)  # Desabilita a edição da caixa de texto

# Configuração da interface gráfica
root = tk.Tk()
root.title("Chat RW")

chat_box = tk.Text(root, height=20, width=70, wrap=tk.WORD)  # Ajusta para que o texto não quebre ao chegar no final da linha
chat_box.tag_configure("bold", font=("Arial", 10, "bold"))  # Define a tag "bold" para o texto em negrito
chat_box.config(state=tk.DISABLED)  # Inicia a caixa de chat como somente leitura
chat_box.pack()

user_entry = tk.Entry(root, width=70)
user_entry.pack()

send_button = tk.Button(root, text="Enviar", command=send_message)
send_button.pack()

root.mainloop()
