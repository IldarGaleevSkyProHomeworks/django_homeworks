import re

from .models import WordFilter


def find_deprecated_subjects(text: str) -> list[str]:
    if not text:
        return []
    text = text.lower()
    filters = [(w_filter.name, w_filter.regular_expression) for w_filter in WordFilter.objects.filter(is_enable=True)]
    result = []
    for name, regex in filters:
        regexp = re.compile(regex.lower())
        if regexp.search(text):
            result.append(name)
    return result
