from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich import print as rprint
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    nationality = Prompt.ask("Choose nationality")
    table = Table(title=f"[italic]Season 2024-25 players from {nationality}[/italic]")
    table.add_column("Name", style="cyan")
    table.add_column("Teams", style="purple")
    table.add_column("Goals", style="green")
    table.add_column("Assists", style="green")
    table.add_column("Points", style="green")

    players = stats.top_scorers_by_nationality(nationality)

    for player in players:
        data = player[1]
        table.add_row(f"{data[0]}", f"{data[2]}", f"{data[3]}", f"{data[4]}", f"{data[5]}")

    console = Console()
    console.print(table)

if __name__ == "__main__":
    main()
