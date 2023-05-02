possible_commands = [
    {
        'command': "!stop",
        "definition": "Faz o bot parar de responder as suas mensagens"
    },
    {
        'command': "!start",
        "definition": "Faz o bot responder as suas mensagens"
    },
    {
        'command': "!help",
        "definition": "Mostra uma breve explicação sobre o bot"
    },
    {
        'command': "!kill",
        "definition": "Fecha o script rodando e as abas do Whatsapp e ChatGPT"
    },
    {
        'command': "!introduction",
        "definition": "Introduz o usuário a Lumma"
    },
    {
        'command': "!commands",
        "definition": "Mostra os comandos disponiveis"
    },
    {
        'command': "!ignore",
        "definition": "Mostra a lista de palavras que a Lumma irá ignorar"
    }
    ]

ignoring = ["blz", "a", "sim", "nao", "tbm", "ja é", "jaé", "jae", "ja", "vlw", "valeu"]

def execute_command(text: str):
    text = text.lower()
    for commands in possible_commands:   
        if text not in commands.get("command"):
            pass
        else:
            if text == "!stop":
                print("parei o bot")
            elif text == "!start":
                print("comecei o bot")
            elif text == "!help":
                print("Estou ajudando")
            elif text == "!kill":
                print("Fechando o bot")
            elif text == "!introduction":
                print("Bem vindo ao Lumma")
            elif text == "!commands":
                print("Comandos:")
                for i in range (len(possible_commands)):
                    print(f"\n\t{possible_commands[i].get('command')}: \n\t\t{possible_commands[i].get('definition')}")
            elif text == "!ignore":
                print("Palavras que irei ignorar:")
                for i in range (len(ignoring)):
                    print(f"\n\t{ignoring[i]}")
                print("\nTambem irei ignorar qualquer forma de audio, foto, stickers e videos")


execute_command("!texte")
# execute_command("!ignore")
execute_command("!commands")