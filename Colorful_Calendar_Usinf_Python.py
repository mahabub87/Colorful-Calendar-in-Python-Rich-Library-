import calendar
from rich.console import Console
from rich.table import Table


def colorful_calendar(year):
    console = Console()  # ✅ fixed missing '='
    months = [calendar.monthcalendar(year, m) for m in range(1, 13)]

    for month in range(12):
        month_name = calendar.month_name[month + 1]

        # ✅ fixed title syntax and commas
        table = Table(title=f"[bold cyan]{month_name} {year}[/bold cyan]", show_lines=True)

        # ✅ fixed missing '=' and typos
        table.add_column("Mon", justify="center", style="green")
        table.add_column("Tue", justify="center", style="green")
        table.add_column("Wed", justify="center", style="green")
        table.add_column("Thu", justify="center", style="green")
        table.add_column("Fri", justify="center", style="green")
        table.add_column("Sat", justify="center", style="red")
        table.add_column("Sun", justify="center", style="red")

        for week in months[month]:
            # ✅ fixed typo: 'l=' → '!=', also formatted correctly
            table.add_row(*[str(day) if day != 0 else "" for day in week])

        console.print(table)
        console.print("\n")  # spacing between months


# ✅ call the function
colorful_calendar(2025)
