# forwardbot.py
import asyncio
from telethon import TelegramClient, events
from telethon.tl.patched import MessageService

# ======== Personal Settings ========
api_id = 123456              # Replace with your own api_id from my.telegram.org
api_hash = "your_api_hash"   # Replace with your own api_hash

SOURCE_CHAT = -1001111111111  # Source chat/group ID or username
TARGET_CHAT = -1002222222222  # Target chat/group ID
# ================================

# Initialize the Telegram client
client = TelegramClient("session_session_name", api_id, api_hash)

# Event handler for new messages in the source chat
@client.on(events.NewMessage(chats=SOURCE_CHAT))
async def forward_handler(event):
    """
    Forward messages from SOURCE_CHAT to TARGET_CHAT.
    Skips service messages (like join/leave/pin events).
    """
    if isinstance(event.message, MessageService):
        return  # Skip service messages

    try:
        await client.forward_messages(TARGET_CHAT, event.message)
        print(f"Forwarded message ID {event.message.id}")
    except Exception as e:
        print(f"Error forwarding message ID {event.message.id}: {e}")

print("ForwardBot is running...")
with client:
    client.run_until_disconnected()