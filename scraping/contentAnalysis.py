import re
from collections import Counter

def generate_keywords(description):
    # Convert the description to lowercase
    description_lower = description.lower()
    
    # Use regular expression to extract words (including hyphenated words)
    words = re.findall(r'\b\w+(?:-\w+)*\b', description_lower)
    
    # Filter out common words (stop words) and words with less than 3 characters
    stop_words = set(["and", "or", "for", "to", "in", "with", "on", "of", "is", "this", "are", "you", "your", "my"])
    filtered_words = [word for word in words if word not in stop_words and len(word) > 2]
    
    # Count the frequency of each word
    word_counter = Counter(filtered_words)
    
    # Get the top 10 most common words as keywords
    keywords_with_occurrences = word_counter.most_common(10)
    
    return keywords_with_occurrences

# Example description
description = """
What you get upon purchase: Login Password Email address and password IP Name Address pin Phone number Useragent Cash out guide cookie.
Ask me questions and make enquiry before you buy.
Our accounts are verified with ID, SSN, Phone Number, and Email.
All balances have 7k dollars or more in them guaranteed. Bitcoin purchased enabled. Debit card attached.
Due to recent influx in the amount of noob customers purchasing my listings without sufficient knowledge on how to use,
I strongly suggest you purchase my 2 days or 7 days tutorial for you to learn and stand confident when trying to access these accounts.
There is a possibility that you might encounter 2fa, but do not worry, there is a way to bypass this easily which I will send to you for free after purchase.
So how many of you are tired of being noobs or are still looking for the right high paying niche in the fraud world or want to have a steady monthly or weekly income through the dark means? This is for you.
To get the chance to discuss anything fraud with me, discover new methods and guides or if you need my professional advice on fraud then I suggest you buy my 7days tutorial listing below.
BE SURE TO CHECK MY SHOP FOR accounts, FRAUD GUIDES, HACKING FRAUD SOFTWARE, and other items - THE VERY BEST YOU CAN FIND ON THE MARKET. IN ADDITION, LOYAL CUSTOMERS WILL PERIODICALLY RECEIVE GIFT VISA/MASTERCARD CC - SO DO NOT MISS OUT. MOVO, VERIFIED, ACCOUNT, EMAIL, LOGIN, payoneer, credit card, fraud, debit card, fast, paypal, carded items, software, malware, counterfeit, fraud guides, tutorials, identification, jewelry, miscellaneous, security, hosting, services, drugs, digital goods, fast money, bitcoin, method, cc, high balance, crack, heroin, cocaine, weed, meth, skrill, coinbase, monero, transfer, money, instagram, western union, cashapp, cashout, bank, login, hq, paypal balance, cookies, credit accounts, account, proxy, cheap, paypal balance, paypal credit, cc, fullz, onlyfans, cc attached, 2FA, paypal.com, carding, proof, ccv, details, cashout, working, 2023, 2023, method, ultimate, guide, paypal fraud, paypal carding, paypal to btc, paypal balance, pp, ssn, credit card, bank account, paypal, paypal balance, paypal credit, paypal money, paypal credit card, paypal cc, carding, money, cvv, paypal account, venmo, rdp, vps, virtual private server, remote desktop, vnc, hacked, cracked, cvv, known, real balances, credit card fraud, Fresh Sniffin, best Quality, US FULLZ CC, CVV (ssn & dob), US cc, carding, cookies, credit accounts, account, proxy, cheap cc, fullz, onlyfans, cc attached, 2FA, carding, proof, ccv, details, cashout, working 2023, working, fresh sniffed, method, ultimate guide, ssn, credit card, bank account, cc, carding, money, account, USA CC HQ LIVE, high balance, classic, standard, platinum, signature, discover, world, Level, Classic, Platinum, Signature, business, premier, gold world card, prepaid, electron, green, infinite, gold premium, purchasing, new world, centurion, black, consumer card, corporate, world elite, small, fleet, purchasing, corporate card, optima, blue, atm, gsa, pin, ebt, global payment, world debit, premium plus, sbs gold green, plus, business elite, charge, travel, money, v pay gift, lowes card, Visa, Mastercard, American Express, Disc-diners, Discover, Maestro, JCB, China Union Pay, Laser, creditcard, cc, cvv, credit debit charge card, wells fargo, hansa, chase, bank of america, boa, capital, binance.
"""

# Generate keywords with occurrences
keywords_with_occurrences = generate_keywords(description)

# Print the keywords with their occurrences
print("Keywords with Occurrences:")
for keyword, occurrences in keywords_with_occurrences:
    print(f"{keyword}: {occurrences}")
