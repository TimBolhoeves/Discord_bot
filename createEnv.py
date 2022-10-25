colors = {
        "default": "\033[0m",
        "green": "\033[92m\033[40m"
}

with open('.env', 'w') as f:
    f.write(f"DISCORD_TOKEN=SuperSecretTokenHere\n")
    print(f"{colors['green']} .env file has been created. {colors['default']}")