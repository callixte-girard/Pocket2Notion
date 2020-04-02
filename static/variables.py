from notion.client import NotionClient
from static import constants as cst

client = NotionClient(token_v2 = cst.notion_token)
