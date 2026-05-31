from rich import print

print("[red]Hello[/red] [bold blue]World[/bold blue]")



from rich.table import Table
from rich.console import Console

console = Console()

table = Table(title="Students")

table.add_column("Name")
table.add_column("Marks")

table.add_row("Himanshu", "95")
table.add_row("Rahul", "88")

console.print(table)


from rich.progress import track
import time

for i in track(range(10), description="Loading..."):
    time.sleep(0.5)