import psutil
import time
from rich.console import Console, Group
from rich.table import Table
from rich.live import Live
from rich.progress import Progress, BarColumn, TextColumn


def make_table(cpu_usage, memory, disk, download_mib, upload_mib):
    table = Table(title="Linux Command Center")
    table.add_column("Metric")
    table.add_column("Usage", justify="right")
    
    disk_total_gb = disk.total / (1024 ** 3 ) #convert to gb.
    disk_used_gb = disk.used / (1024 ** 3 ) #convert to gb.
    
    table.add_row("CPU", f"{cpu_usage}%")
    table.add_row("RAM", f"{memory.percent}%")
    table.add_row("Disk", f"{disk_used_gb:.1f} / {disk_total_gb:.1f} GiB ({disk.percent}%)")
    table.add_row("Download", f"{download_mib:.4f} MiB/s")
    table.add_row("Upload", f"{upload_mib:.4f} MiB/s")

    return table


def get_usage_color(percentage):
    if percentage >= 80:
        return "red"
    elif percentage >= 60:
        return "yellow"
    else:
        return "green"


class ColoredBarColumn(BarColumn):
    """BarColumn that picks its color from the task's 'color' field."""
    def render(self, task):
        color = task.fields.get("color", "green")
        self.complete_style = color
        self.finished_style = color
        return super().render(task)


def make_progress(cpu_usage, memory, disk, swap, console):
    progress = Progress(
        TextColumn("{task.description}"),
        ColoredBarColumn(bar_width=40),
        TextColumn("[{task.fields[color]}]{task.percentage:>5.1f}%"),
        console=console,
    )

    progress.add_task(
        "CPU",
        total=100,
        completed=cpu_usage,
        color=get_usage_color(cpu_usage),
    )
    progress.add_task(
        "RAM",
        total=100,
        completed=memory.percent,
        color=get_usage_color(memory.percent),
    )
    progress.add_task(
        "Disk",
        total=100,
        completed=disk.percent,
        color=get_usage_color(disk.percent),
    )

    progress.add_task(
        "Swap",
        total=100,
        completed=swap.percent,
        color=get_usage_color(swap.percent),
    )  
    
    return progress

def get_network_speed(previous_net, current_net, elapsed):
    #To calculate speed -> (new_total - old_total) / elapsed seconds -> B/s
    download = (current_net.bytes_recv - previous_net.bytes_recv) / elapsed
    upload = (current_net.bytes_sent - previous_net.bytes_sent) / elapsed

    #convert B/s to MiB/s
    download_mib = download / (1024 ** 2)
    upload_mib = upload / (1024 ** 2)

    return download_mib, upload_mib


console = Console()
previous_net = psutil.net_io_counters()
previous_time = time.monotonic()
try:
    with Live(console=console, refresh_per_second=4) as live:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage("/")
            swap = psutil.swap_memory()

            current_net = psutil.net_io_counters()
            current_time = time.monotonic()

            elapsed = current_time - previous_time
            
            download_mib, upload_mib = get_network_speed(previous_net, current_net, elapsed)
            previous_net = current_net
            previous_time = current_time

            #show live table (CPU USAGE, RAM USAGE, SSD USAGE).
            table = make_table(cpu_usage, memory, disk, download_mib, upload_mib)
            

            #show live progress bars (CPU USAGE, RAM USAGE, SSD USAGE).
            progress = make_progress(cpu_usage, memory, disk, swap, console)
            live.update(Group(table, progress))

except KeyboardInterrupt:
    print("\nDashboard Stopped.")

