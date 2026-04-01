"""运行一次，初始化数据库表结构"""
import sqlite3
import sys
sys.path.append("..")
from config import DB_PATH

DB_PATH.parent.mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    xhs_id TEXT UNIQUE,           -- 小红书用户ID
    nickname TEXT,
    bio TEXT,
    follower_count INTEGER,
    note_count INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id INTEGER,
    xhs_note_id TEXT UNIQUE,      -- 笔记ID
    title TEXT,
    content TEXT,                  -- 正文
    tags TEXT,                     -- JSON array
    image_count INTEGER,
    liked_count TEXT,              -- "1w+" 这种格式先存文本
    collected_count TEXT,
    comment_count TEXT,
    publish_date TEXT,
    note_type TEXT DEFAULT 'image', -- image / video
    source_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES accounts(id)
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS analysis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id INTEGER,
    dimension TEXT,               -- title_style / text_structure / tone / tags 等
    result TEXT,                  -- JSON格式的分析结果
    model_used TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES accounts(id)
)
""")

conn.commit()
conn.close()
print(f"数据库已初始化: {DB_PATH}")