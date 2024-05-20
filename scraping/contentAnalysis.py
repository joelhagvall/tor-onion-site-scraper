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
7days tutorial on fraud methods CPN  carding bank loan skrill paypal  fraudbuddy DARKmarket special is designed for people with little or no idea of how to start making money online black hat methods such as carding PayPal Skrill   MoneyGram etc  CPN  black hat affiliate marketing  Virtual carding  bank logs  account logs  ecommerce refund scam technique lol plus lots of other stuff that will blow your mind and of course train you to replicate them in real life. We will drop the game for you  If you need to make any special requests please do so with respect but do not expect any favours because you only bought our listing and am quite sure I have delivered so be kind  you can only except a favour from me only when you have left a positive feedback because that clearly shows your support towards our well esteemed establishment and I always pay my debt just so you know.  What you will get upon purchase  Full fraud PDF guide on various courses which we are gonna discuss together 7days mentorship One on one chatting here on the market where you can ask your questions lol even silly questions are accepted to so no pressure I need you to be open up to me so I can transfer all my knowledge to you.  So how many of you are tired of being noobs  or are still looking for the right high paying niche in the fraud world  or want to have a steady monthly or weekly income through the dark means  This is for you      keyword:   cashapp paypal account fraud dark market cc apple guides tutorial money mentor credit card fraud debit card fast paypal carded items software malware counterfeit fraud guides tutorials identification jewellry miscellaneous security hosting services drugs digital goods fast money bitcoin method cc high balance crack heroin cocaine weed meth skrill coinbase monero transfer money instagram western union cashapp bitstamp cashout bank login hq paypal balance cookies credit accounts account proxy cheap paypal balance paypal credit cc fullz onlyfans cc attached 2FA paypal.com carding proof ccv details cashout working 2023 2023 method ultimate guide paypal fraud paypal carding paypal to btc paypal balance pp ssn credit card bank account paypal paypal balance paypal credit paypal money paypal credit card paypal cc carding money cvv paypal account venmo rdp vps virtual private server remote desktop vnc hacked cracked cvv known real balances credit card fraud Fresh Sniffin best Quality US FULLZ CC CVV (ssn & dob) US cc carding cookies credit accounts account proxy cheap cc fullz onlyfans cc attached 2FA carding proof ccv details cashout working 2023 working fresh sniffed method ultimate guide ssn credit card bank account cc carding money account USA CC HQ LIVE high balance classic standard platinum signature discover world Level Classic Platinum Signature buisiness premier gold world card prepaid electron green infinite gold premium purchasing new world centurion black consumer card corporate world elite small fleet purchasing coporate card optima blue atm gsa pin ebt global payment world debit premium plus sbs gold green plus business elite charge travel money v pay gift lowes card Visa Mastercard American Express Disc-diners Discover Maestro JCB; China Union Pay Laser creditcard cc cvv credit debit charge card wells frago hansa chase bank of america boa capital neteller paypal Monese accounts  Paysera account shopify N26 accouunts  paysend account  earnin account  betway account   Revolut account  bet365 accounts  bovada and mybookie account How make money online transfer Google Amazon Spotify AppleStore Zoom Venmo either.io archive.org discord.com genshin.mihoyo.com PayPal Google Sony Twitter TikTok MEGAnz NvidiaStore Live Amazon GitHub Venmo Spotify AppleStore SteamGoogle  Facebook  AppleStore  Pof  Google  Amazon  AppleStore  Yahoo  PayPal  Webmail  Slack  LinkedIn  Google  Bwin  Facebook  Bet365  Ebay  Unibet  Betfair  AppleStore  Live  Zoom  LinkedIn  Booking Amazon  Office365  888sport  Binance  Skrill  PayPal  Pinterest  Instagram  LenovoStore  Bitstamp  WIX  Betway  Uber  Aliexpress  Bitfinex  EToro  Emirates  Stripe  QatarAirways  Facebook  O2online  T-mobile  GoDaddy  Binance  1and1Panel  2Checkout  Steam  Kraken  Coinmama  Bittrex  Netflix  TurkishAirway  Shopify Skype  Ebay  Fiverr  Gemini  LocalBitcoin  Bitstamp  Skrill  Coinbase  Bitfinex  Upwork  Immobilie  Xoom  Dropbox  Uber  GitHub  Yahoo  Live  Messenger  ADP  Netflix  Ebay  Xfinity  PayPal  Twitter  FedEx  Instagram  FirefoxAccount  Uber  PaycorPay  ATT  LinkedIn  Tumblr  Amazon  Greendot  Capitalone  HRBlock  SonyEnter  Indeed  Monster  Craigslist  Ancestry  Walmart  TaxAct  Coinbase Google  Office365  Facebook  Amazon  Groupon  Wordpress  Sprint  Intuit  Uber  ADP  LowesStore  CVS  Craigslist  Greendot  Tumblr  Netflix  Live  T-mobile  Reddit  LinkedIn  Twitter  Gobank  Yahoo  PayPal  GoDaddy  Vimeo  FreeTaxUsa  EtsyStore  Dropbox  FedEx  Homedepot  UhaulStore  Bestbuy  MySmartMove  Target  Squareup  Adobe  Walmart
"""

# Generate keywords with occurrences
keywords_with_occurrences = generate_keywords(description)

# Print the keywords with their occurrences
print("Keywords with Occurrences:")
for keyword, occurrences in keywords_with_occurrences:
    print(f"{keyword}: {occurrences}")
