from django import template

register = template.Library()

@register.filter
def formatted_emotion(mood, emotion_name):
    value = getattr(mood, emotion_name)
    tag = getattr(mood, f"{emotion_name}_tag")
    if value is None:
        return "-"
    if tag:
        return f"{value} ({tag})"
    return str(value)