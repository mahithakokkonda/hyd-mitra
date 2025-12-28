conversation = []

def remember(user, bot):
    conversation.append({"u": user, "b": bot})
    if len(conversation) > 5:
        conversation.pop(0)

def get_context():
    text = ""
    for c in conversation:
        text += f"వాడుకరి: {c['u']}\nసహాయకుడు: {c['b']}\n"
    return text
