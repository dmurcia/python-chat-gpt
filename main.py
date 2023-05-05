import openai
import config
import typer
from rich import print
from rich.table import Table


def main():

    openai.api_key = config.api_key

    print("💬 [bold green]ChatGPT API en Python[/bold green]")

    table = Table("Comando", "Descripción")
    table.add_row("exit", "Salir de la aplicación")
    table.add_row("new", "Crear nueva conversación")

    print(table)

    # Contexto inicial
    context = {"role": "system",
               "content": "Eres un asistente de traducción de español a ingles"}

    messages = [context]

    while True:

        content = __prompt()

        if content == "new":
            print("🆕 Nueva conversación")
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                messages=messages)

        response_content = response.choices[0].message.content

        messages.append({"role": "assistant", "content": response_content})

        print(f"[bold green]> [/bold green] [green]{response_content}[/green]")


def __prompt() -> str:
    prompt = typer.prompt("\n¿Qué necesitas saber?")

    if prompt == "exit":
        exit = typer.confirm("✋ ¿Estás seguro?")
        if exit:
            print("👋 Adiós!")
            raise typer.Abort()

        return __prompt

    return prompt


if __name__ == "__main__":
    typer.run(main)
