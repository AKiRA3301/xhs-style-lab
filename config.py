import os
from dotenv import load_dotenv

load_dotenv()

# API
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = "https://api.deepseek.com"

# Models
ANALYSIS_MODEL = "claude-sonnet-4-20250514"
GENERATION_MODEL = "deepseek-chat"

# Paths
import pathlib
BASE_DIR = pathlib.Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "xhs_notes.db"
RAW_DIR = DATA_DIR / "raw"
ANALYZED_DIR = DATA_DIR / "analyzed"
OUTPUT_DIR = BASE_DIR / "output"
PROMPTS_DIR = BASE_DIR / "02_analyze" / "prompts"