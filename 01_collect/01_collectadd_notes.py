"""录入目标小红书账号基本信息"""
import sqlite3
import sys
sys.path.append("..")
from config import DB_PATH
from rich.console import Console
from rich.panel import Panel

console = Console()

def main():
    console.print(Panel("📝 录入小红书账号", style="bold cyan"))

    xhs_id = input("用户ID（主页URL里的那串）: ").strip()
    nickname = input("昵称: ").strip()
    bio = input("简介（可直接回车跳过）: ").strip() or None
    follower_count = input("粉丝数（数字，不确定填0）: ").strip()
    note_count = input("笔记数: ").strip()

    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute(
            "INSERT INTO accounts (xhs_id, nickname, bio, follower_count, note_count) VALUES (?, ?, ?, ?, ?)",
            (xhs_id, nickname, bio, int(follower_count or 0), int(note_count or 0))
        )
        conn.commit()
        console.print(f"\n✅ 已录入账号: [bold]{nickname}[/bold]", style="green")
    except sqlite3.IntegrityError:
        console.print(f"\n⚠️  账号 {xhs_id} 已存在", style="yellow")
    finally:
        conn.close()

if __name__ == "__main__":
    main()