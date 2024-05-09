import matplotlib.pyplot as plt

# Data
categories = ['Access Crime', 'Data Crime', 'Network Crime']
access_crime_subcategories = ['Malware', 'Phishing', 'Hacking', 'Course']
data_crime_subcategories = ['Leaks', 'Database', 'Credit Card', 'Account']
network_crime_subcategories = ['DDoS']

access_crime_keywords = [
    'Malware', 'trojan', 'ransomware', 'RAT', 'keylogger', 'spyware', 'worm',
    'Phishing', 'social engineering', 'fraud',
    'Hacking', 'exploit', 'vulnerability', 'penetration testing',
    'Tutorial', 'guide', 'ebook'
]

data_crime_keywords = [
    'Leak', 'data leak', 'breach', 'dump',
    'Database', 'SQL injection', 'MySQL', 'Oracle',
    'Credit card', 'CVV', 'carding', 'carder', 'BIN',
    'Account', 'login', 'username', 'email', 'credential', 'password', 'hash', 'cracking', 'brute force'
]

network_crime_keywords = [
    'DDoS', 'botnet', 'stresser', 'denial of service', 'booter'
]

frequency = [353, 295, 352, 2086, 180, 234, 985, 1121, 39]

# Plotting
plt.figure(figsize=(10, 8))
plt.pie(frequency, labels=access_crime_subcategories + data_crime_subcategories + network_crime_subcategories, autopct='%1.1f%%', startangle=140)
plt.title('Crime Category Pie Chart')
plt.axis('equal')

# Add legend
plt.legend(categories, loc="upper right")

plt.show()
