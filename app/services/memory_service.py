MAX_MEMORY_LENGTH = 10


conversation_memory = []


def add_message(role, content):

    conversation_memory.append({
        "role": role,
        "content": content
    })

    if len(conversation_memory) > MAX_MEMORY_LENGTH:
        conversation_memory.pop(0)


def get_conversation_history():

    return conversation_memory


def clear_memory():

    conversation_memory.clear()