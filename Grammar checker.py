Grammar correction Model Using happytransformer

def grammar_check(happy_tt, settings, text):
  grammar_mistakes = []
  suggestions = []
  corrected_sentence = happy_tt.generate_text(text, args=settings)
  original_sentence_words = text.split()
  corrected_sentence_words = corrected_sentence.text.split()
  for word in original_sentence_words:
    if word not in corrected_sentence_words:
      grammar_mistakes.append(word)

  for word in corrected_sentence_words:
    if word not in original_sentence_words:
      suggestions.append(word)

  if len(grammar_mistakes) == 0:
    result = 'Passed'
    return result, ("No grammatical mistakes found")
  else:
    result = 'Failed'
    return result, corrected_sentence.text, grammar_mistakes, suggestions
