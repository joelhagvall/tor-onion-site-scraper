import re
from collections import Counter

def generate_keywords(description):
    # Convert the description to lowercase
    description_lower = description.lower()
    
    # Use regular expression to extract words (including hyphenated words)
    words = re.findall(r'\b\w+(?:-\w+)*\b', description_lower)
    
    # Filter out common words (stop words) and words with less than 3 characters
    stop_words = set(["and", "or", "for", "to", "in", "with", "on", "of", "is", "this", "are", "you", "your", "my", "the"])
    filtered_words = [word for word in words if word not in stop_words and len(word) > 2]
    
    # Count the frequency of each word
    word_counter = Counter(filtered_words)
    
    # Get the top 20 most common words as keywords
    keywords_with_occurrences = word_counter.most_common(25)
    
    return keywords_with_occurrences

# Example description
description = """
7days tutorial on fraud methods CPN  carding bank loan skrill paypal  fraudbuddy DARKmarket special is designed for people with little or no idea of how to start making money online black hat methods such as carding PayPal Skrill   MoneyGram etc  CPN  black hat affiliate marketing  Virtual carding  bank logs  account logs  ecommerce refund scam technique lol plus lots of other stuff that will blow your mind and of course train you to replicate them in real life. We will drop the game for you  If you need to make any special requests please do so with respect but do not expect any favours because you only bought our listing and am quite sure I have delivered so be kind  you can only except a favour from me only when you have left a positive feedback because that clearly shows your support towards our well esteemed establishment and I always pay my debt just so you know.  What you will get upon purchase  Full fraud PDF guide on various courses which we are gonna discuss together 7days mentorship One on one chatting here on the market where you can ask your questions lol even silly questions are accepted to so no pressure I need you to be open up to me so I can transfer all my knowledge to you.  So how many of you are tired of being noobs  or are still looking for the right high paying niche in the fraud world  or want to have a steady monthly or weekly income through the dark means  This is for you      
"""

# Generate keywords with occurrences
keywords_with_occurrences = generate_keywords(description)

# Print the keywords with their occurrences
print("Keywords with Occurrences:")
for keyword, occurrences in keywords_with_occurrences:
    print(f"{keyword}: {occurrences}")
