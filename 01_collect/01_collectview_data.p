"""查看已录入的数据概况"""
import sqlite3
import json
import sys
sys.path.append("..")
from config import DB_PATH
from rich.console import Console
from rich.table import Table

console = Console()

def main():
    conn = sqlite3.connect(DB_PATH)

    # 账号概况
    accounts = conn.execute("SELECT id, nickname, xhs_id FROM accounts").fetchall()
    console.print(f"\n📊 已录入 [bold]{len(accounts)}[/bold] 个账号\n")

    for acc in accounts:
        acc_id, nickname, xhs_id = acc
        notes = conn.execute(
            "SELECT title, tags, liked_count, publish_date FROM notes WHERE account_id = ? ORDER BY publish_date DESC",
            (acc_id,)
        ).fetchall()

        table = Table(title=f"{nickname} ({xhs_id}) — {len(notes)} 篇笔记")
        table.add_column("#", style="cyan", width=4)
        table.add_column("标题", max_width=35)
        table.add_column("标签", max_width=30)
        table.add_column("点赞", justify="right")
        table.add_column("日期")

        for i, n in enumerate(notes, 1):
            tags = json.loads(n[1]) if n[1] else []
            tags_str = " ".join(f"#{t}" for t in tags[:3])
            if len(tags) > 3:
                tags_str += f" +{len(tags)-3}"
            table.add_row(str(i), n[0][:35], tags_str, str(n[2]), n[3] or "-")

        console.print(table)
        console.print()

    conn.close()

if __name__ == "__main__":
    main()