# import datetime
# import nepali_datetime

# # Dictionary mapping important events to Nepali dates
# IMPORTANT_EVENTS = {
#     (1, 1): "नयाँ वर्ष",  # Nepali New Year (BS)
#     (1, 11): "लोकतन्त्र दिवस",  # Loktantra Diwas
#     (1, 18): "विश्व मजदुर दिवस",  # International Labor Day
#     (1, 30): "श्रीपञ्चमी",  # Shree Panchami
#     (2, 7): "ग्याल्पो लोसार",  # Gyalpo Losar
#     (3, 8): "महिला दिवस",  # International Women's Day
#     (5, 15): "कुशे औंशी",  # Kushe Aunshi
#     (6, 3): "संबिधान दिवस",  # Constitution Day
#     (6, 8): "विश्व वातावरण दिवस",  # World Environment Day
#     (6, 11): "गणेश चतुर्थी",  # Ganesh Chaturthi
#     (7, 1): "विश्व पर्यटन दिवस",  # World Tourism Day
#     (8, 25): "ग्याल्बो लोसार",  # Gyalpo Losar
#     (9, 1): "विश्व पर्यटन दिवस",  # World Tourism Day
#     (9, 7): "उधौली पर्व",  # Udhauli Parva
#     (9, 12): "मोहनी नख",  # Mohani Nakha (Newa)
#     (9, 15): "अन्नपूर्ण यात्रा",  # Annapurna Yatra
#     (9, 23): "यमरी पुन्ही",  # Yomari Punhi
#     (10, 1): "माघे संक्रान्ति",  # Maghe Sankranti
#     (11, 7): "प्रजातन्त्र दिवस",  # Democracy Day
#     (11, 8): "सोनाम ल्होसार",  # Sonam Lhosar

# }

# # Nepali tithi information
# TITHI_LIST = [
#     "प्रतिपदा", "द्वितीया", "तृतीया", "चतुर्थी", "पञ्चमी", "षष्ठी", "सप्तमी", "अष्टमी",
#     "नवमी", "दशमी", "एकादशी", "द्वादशी", "त्रयोदशी", "चतुर्दशी", "पूर्णिमा", "अमावस्या"
# ]

# class NepaliCalendar:
#     def __init__(self, english_date =None):
#         if english_date is None:
#             self.english_date= datetime.datetime.now()
#         else:
#             self.english_date= english_date
           
#         # COnvert to Nepali Date usign nepali_datetime library 
#         self.nepali_date= nepali_datetime.date.from_datetime_date(self.english_date.date())
#         self.day_of_week= self.get_nepali_day_of_week()
        
#     def get_nepali_day_of_week(self):
#         #  days of week in nepali
#         nepali_days = [
#          "सोमबार", "मंगलबार", "बुधबार", "बिहिबार", "शुक्रबार", "शनिबार","आइतबार"
#         ]
#         return nepali_days[self.english_date.weekday()]
#         #here .weekday return the days name starting from monday as in 0th index so we have to arrage the nepali days as sombar in the 0th index to return the same value.
        
#     def get_tithi(self):
#         day_of_month= self.nepali_date.day
#         tithi_index= (day_of_month-1)% len(TITHI_LIST) #here -1 is done as tithi list index start from 0 so to index to day 1 it will gives (1-1)=0 ---> प्रतिपदा
#         return TITHI_LIST[tithi_index]
    
#     def get_important_event(self):
#         #it will check if the nepali date has an important event
#         nepali_month_day=(self.nepali_date.month, self.nepali_date.day)
#         return IMPORTANT_EVENTS.get(nepali_month_day,"No special event today")
    
#     def get_time(self):
#         # current_time= self.english_date.time()
#         # return current_time.strftime("%H:%M:%S")
#         current_time=datetime.datetime.now()
#         print("Current time is: {}".format(current_time.strftime("%H:%M:%S")))
    
#     def show_nepali_date(self):
#         print(f'Nepali Date: {self.nepali_date}')
#         print(f'Day of the Week: {self.day_of_week}')
#         self.get_time()
#         # print(f'Time: {self.get_time()}')
#         print(f'Tithi: {self.get_tithi()}')
#         print(f'Important Event: {self.get_important_event()}')
        
# if __name__ =="__main__":
#     english_date= datetime.datetime(2024,12,25) 
#     nepali_calendar= NepaliCalendar(english_date) 
#     nepali_calendar.show_nepali_date()


# import datetime

# # Define a reference date for conversion: Nepali New Year 2080 BS starts on April 14, 2023 AD
# REFERENCE_AD_DATE = datetime.date(2023, 4, 14)
# REFERENCE_BS_DATE = (2080, 1, 1)  # Corresponding Nepali date: 1st Baisakh 2080

# # Define the lengths of months in the Nepali calendar for the year 2080
# BS_MONTH_LENGTHS = [30, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30]


# IMPORTANT_EVENTS = {
#     (1, 1): "नयाँ वर्ष",  # Nepali New Year (BS)
#     (1, 11): "लोकतन्त्र दिवस",  # Loktantra Diwas
#     (1, 18): "विश्व मजदुर दिवस",  # International Labor Day
#     (1, 30): "श्रीपञ्चमी",  # Shree Panchami
#     (2, 7): "ग्याल्पो लोसार",  # Gyalpo Losar
#     (3, 8): "महिला दिवस",  # International Women's Day
#     (5, 15): "कुशे औंशी",  # Kushe Aunshi
#     (6, 3): "संबिधान दिवस",  # Constitution Day
#     (6, 8): "विश्व वातावरण दिवस",  # World Environment Day
#     (6, 11): "गणेश चतुर्थी",  # Ganesh Chaturthi
#     (7, 1): "विश्व पर्यटन दिवस",  # World Tourism Day
#     (8, 25): "ग्याल्बो लोसार",  # Gyalpo Losar
#     (9, 1): "विश्व पर्यटन दिवस",  # World Tourism Day
#     (9, 7): "उधौली पर्व",  # Udhauli Parva
#     (9, 12): "मोहनी नख",  # Mohani Nakha (Newa)
#     (9, 15): "अन्नपूर्ण यात्रा",  # Annapurna Yatra
#     (9, 23): "यमरी पुन्ही",  # Yomari Punhi
#     (10, 1): "माघे संक्रान्ति",  # Maghe Sankranti
#     (11, 7): "प्रजातन्त्र दिवस",  # Democracy Day
#     (11, 8): "सोनाम ल्होसार",  # Sonam Lhosar
# }

# # Nepali tithi information
# TITHI_LIST = [
#     "प्रतिपदा", "द्वितीया", "तृतीया", "चतुर्थी", "पञ्चमी", "षष्ठी", "सप्तमी", "अष्टमी",
#     "नवमी", "दशमी", "एकादशी", "द्वादशी", "त्रयोदशी", "चतुर्दशी", "पूर्णिमा", "अमावस्या"
# ]

# # Days of the week in Nepali
# NEPALI_DAYS = [
#     "सोमबार", "मंगलबार", "बुधबार", "बिहिबार", "शुक्रबार", "शनिबार", "आइतबार"
# ]

# def get_nepali_day_of_week(english_data):
#     #return nepali name of the day for a given  english date.
#     return NEPALI_DAYS[english_data.weekday()]

# def get_tithi(nepali_day):
#     #return tithi based on the day of the month in nepali date
#     tithi_index= (nepali_day-1)% len(TITHI_LIST)
#     return TITHI_LIST[tithi_index]

# def get_important_event(nepali_month, nepali_day):
#     #return important event, if any, based on nepali month and day
#     return IMPORTANT_EVENTS.get((nepali_month,nepali_day),'No special event today')

# def get_time():
#     #return current time
#     current_time=datetime.datetime.now()
#     return current_time.strftime("%H:%M:%S")

# def days_between_dates(date1,date2):
#     #calculte the number of days between 2 dates
#     return(date2-date1).days

# def add_days_to_bs_date(bs_date, days_to_add):
#     #add a particular number of days in nepali(bs) date and return the new bs date
#     year,month,day= bs_date
#     while days_to_add>0:
#         days_in_current_month= BS_MONTH_LENGTHS[month-1]
#         if days_to_add+day<=days_in_current_month:
#             day+=days_to_add
#             days_to_add=0
#         else:
#             days_to_add-=(days_in_current_month-day+1)
#             day=1
#             month+=1
#             if month>12:
#                 month=1
#                 year+=1
    
#     return(year,month,day)

# def convert_to_nepali_date(english_date):
#     #convert the neglish date to nepalo date
#     days_diff= days_between_dates(REFERENCE_AD_DATE,english_date)
#     nepali_date=add_days_to_bs_date(REFERENCE_BS_DATE,days_diff)
#     return nepali_date


# def show_nepali_date(english_date, nepali_date):
#     #display nepali date, day of the week, tithi and any important events
#     nepali_day_of_week= get_nepali_day_of_week(english_date)
#     nepali_day=nepali_date[2]   #assuming nepali_date=(year,month,day) format
#     nepali_month= nepali_date[1]
    
#     print(f'Nepali date: {nepali_date}')
#     print(f'Day of week: {nepali_day_of_week}')
#     print(f'Current time: {get_time()}')
#     print(f'Tithi: {get_tithi(nepali_day)}')
#     print(f'Important event: {get_important_event(nepali_month,nepali_day)}')
    
# if __name__=="__main__":
#     english_date=datetime.date(2002,4,4)
#     nepali_date= convert_to_nepali_date(english_date)
    
#     show_nepali_date(english_date,nepali_date)
    

# import datetime

# # Define a reference date for conversion: Nepali New Year 2080 BS starts on April 14, 2023 AD
# REFERENCE_AD_DATE = datetime.date(2023, 4, 14)
# REFERENCE_BS_DATE = (2080, 1, 1)  # Corresponding Nepali date: 1st Baisakh 2080

# # Define the lengths of months in the Nepali calendar for the year 2080
# BS_MONTH_LENGTHS = [30, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30]

# IMPORTANT_EVENTS = {
#     (1, 1): "नयाँ वर्ष",  # Nepali New Year (BS)
#     (1, 11): "लोकतन्त्र दिवस",  # Loktantra Diwas
#     (1, 18): "विश्व मजदुर दिवस",  # International Labor Day
#     (1, 30): "श्रीपञ्चमी",  # Shree Panchami
#     (2, 7): "ग्याल्पो लोसार",  # Gyalpo Losar
#     (3, 8): "महिला दिवस",  # International Women's Day
#     (5, 15): "कुशे औंशी",  # Kushe Aunshi
#     (6, 3): "संबिधान दिवस",  # Constitution Day
#     (6, 8): "विश्व वातावरण दिवस",  # World Environment Day
#     (6, 11): "गणेश चतुर्थी",  # Ganesh Chaturthi
#     (7, 1): "विश्व पर्यटन दिवस",  # World Tourism Day
#     (8, 25): "ग्याल्बो लोसार",  # Gyalpo Losar
#     (9, 1): "विश्व पर्यटन दिवस",  # World Tourism Day
#     (9, 7): "उधौली पर्व",  # Udhauli Parva
#     (9, 12): "मोहनी नख",  # Mohani Nakha (Newa)
#     (9, 15): "अन्नपूर्ण यात्रा",  # Annapurna Yatra
#     (9, 23): "यमरी पुन्ही",  # Yomari Punhi
#     (10, 1): "माघे संक्रान्ति",  # Maghe Sankranti
#     (11, 7): "प्रजातन्त्र दिवस",  # Democracy Day
#     (11, 8): "सोनाम ल्होसार",  # Sonam Lhosar
# }

# # Nepali tithi information
# TITHI_LIST = [
#     "प्रतिपदा", "द्वितीया", "तृतीया", "चतुर्थी", "पञ्चमी", "षष्ठी", "सप्तमी", "अष्टमी",
#     "नवमी", "दशमी", "एकादशी", "द्वादशी", "त्रयोदशी", "चतुर्दशी", "पूर्णिमा", "अमावस्या"
# ]

# # Days of the week in Nepali
# NEPALI_DAYS = [
#     "सोमबार", "मंगलबार", "बुधबार", "बिहिबार", "शुक्रबार", "शनिबार", "आइतबार"
# ]

# def get_nepali_day_of_week(english_date):
#     # Return Nepali name of the day for a given English date.
#     return NEPALI_DAYS[english_date.weekday()]

# def get_tithi(nepali_day):
#     # Return tithi based on the day of the month in Nepali date
#     tithi_index = (nepali_day - 1) % len(TITHI_LIST)
#     return TITHI_LIST[tithi_index]

# def get_important_event(nepali_month, nepali_day):
#     # Return important event, if any, based on Nepali month and day
#     return IMPORTANT_EVENTS.get((nepali_month, nepali_day), 'No special event today')

# def get_time():
#     # Return current time
#     current_time = datetime.datetime.now()
#     return current_time.strftime("%H:%M:%S")

# def days_between_dates(date1, date2):
#     # Calculate the number of days between two dates
#     return (date2 - date1).days

# def add_days_to_bs_date(bs_date, days_to_add):
#     # Add a particular number of days in Nepali (BS) date and return the new BS date
#     year, month, day = bs_date
#     while days_to_add > 0:
#         days_in_current_month = BS_MONTH_LENGTHS[month - 1]
#         if days_to_add + day <= days_in_current_month:
#             day += days_to_add
#             days_to_add = 0
#         else:
#             days_to_add -= (days_in_current_month - day + 1)
#             day = 1
#             month += 1
#             if month > 12:
#                 month = 1
#                 year += 1
#     return year, month, day

# def convert_to_nepali_date(english_date):
#     # Convert the English date to Nepali date
#     days_diff = days_between_dates(REFERENCE_AD_DATE, english_date)
    
#     # Debugging: print the calculated days difference
#     print(f"Days difference between {REFERENCE_AD_DATE} and {english_date}: {days_diff} days")
    
#     nepali_date = add_days_to_bs_date(REFERENCE_BS_DATE, days_diff)
#     return nepali_date

# def show_nepali_date(english_date, nepali_date):
#     # Display Nepali date, day of the week, tithi, and any important events
#     nepali_day_of_week = get_nepali_day_of_week(english_date)
#     nepali_day = nepali_date[2]  # Assuming nepali_date = (year, month, day) format
#     nepali_month = nepali_date[1]
    
#     print(f'Nepali Date: {nepali_date}')
#     print(f'Day of the Week: {nepali_day_of_week}')
#     print(f'Current Time: {get_time()}')
#     print(f'Tithi: {get_tithi(nepali_day)}')
#     print(f'Important Event: {get_important_event(nepali_month, nepali_day)}')

# if __name__ == "__main__":
#     # Example: Convert April 4, 2002 to Nepali date
#     english_date = datetime.date(2002, 4, 4)
    
#     # Debugging: show the original English date
#     print(f"Converting English date: {english_date}")
    
#     nepali_date = convert_to_nepali_date(english_date)
    
#     show_nepali_date(english_date, nepali_date)

import datetime

# Define a reference date for conversion: Nepali New Year 2080 BS starts on April 14, 2023 AD
REFERENCE_AD_DATE = datetime.date(2023, 4, 14)
REFERENCE_BS_DATE = (2080, 1, 1)  # Corresponding Nepali date: 1st Baisakh 2080

# Define the lengths of months in the Nepali calendar for the year 2080
BS_MONTH_LENGTHS = [30, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30]

IMPORTANT_EVENTS = {
    (1, 1): "नयाँ वर्ष",  # Nepali New Year (BS)
    (1, 11): "लोकतन्त्र दिवस",  # Loktantra Diwas
    (1, 18): "विश्व मजदुर दिवस",  # International Labor Day
    (1, 30): "श्रीपञ्चमी",  # Shree Panchami
    (3, 8): "महिला दिवस",  # International Women's Day
    (5, 15): "कुशे औंशी",  # Kushe Aunshi
    (6, 3): "संबिधान दिवस",  # Constitution Day
    (6, 8): "विश्व वातावरण दिवस",  # World Environment Day
    (6, 11): "गणेश चतुर्थी",  # Ganesh Chaturthi
    (7, 1): "विश्व पर्यटन दिवस",  # World Tourism Day
    (9, 1): "विश्व पर्यटन दिवस",  # World Tourism Day
    (9, 7): "उधौली पर्व",  # Udhauli Parva
    (9, 12): "मोहनी नख",  # Mohani Nakha (Newa)
    (9, 15): "अन्नपूर्ण यात्रा",  # Annapurna Yatra
    (9, 23): "यमरी पुन्ही",  # Yomari Punhi
    (10, 1): "माघे संक्रान्ति",  # Maghe Sankranti
    (11, 7): "प्रजातन्त्र दिवस",  # Democracy Day

}

# Nepali tithi information
TITHI_LIST = [
    "प्रतिपदा", "द्वितीया", "तृतीया", "चतुर्थी", "पञ्चमी", "षष्ठी", "सप्तमी", "अष्टमी",
    "नवमी", "दशमी", "एकादशी", "द्वादशी", "त्रयोदशी", "चतुर्दशी", "पूर्णिमा", "अमावस्या"
]

# Days of the week in Nepali
NEPALI_DAYS = [
    "सोमबार", "मंगलबार", "बुधबार", "बिहिबार", "शुक्रबार", "शनिबार", "आइतबार"
]

def get_nepali_day_of_week(english_date):
    # Return Nepali name of the day for a given English date.
    return NEPALI_DAYS[english_date.weekday()]

def get_tithi(nepali_day):
    # Return tithi based on the day of the month in Nepali date
    tithi_index = (nepali_day - 1) % len(TITHI_LIST)
    return TITHI_LIST[tithi_index]

def get_important_event(nepali_month, nepali_day):
    # Return important event, if any, based on Nepali month and day
    return IMPORTANT_EVENTS.get((nepali_month, nepali_day), 'No special event today')

def get_time():
    # Return current time
    current_time = datetime.datetime.now()
    return current_time.strftime("%H:%M:%S")

def days_between_dates(date1, date2):
    # Calculate the number of days between two dates
    return (date2 - date1).days

def add_days_to_bs_date(bs_date, days_to_add):
    # Add or subtract a particular number of days in Nepali (BS) date and return the new BS date
    year, month, day = bs_date
    
    if days_to_add >= 0:
        # Adding days
        while days_to_add > 0:
            days_in_current_month = BS_MONTH_LENGTHS[month - 1]
            if days_to_add + day <= days_in_current_month:
                day += days_to_add
                days_to_add = 0
            else:
                days_to_add -= (days_in_current_month - day + 1)
                day = 1
                month += 1
                if month > 12:
                    month = 1
                    year += 1
    else:
        # Subtracting days for negative days_to_add
        days_to_subtract = -days_to_add
        while days_to_subtract > 0:
            if days_to_subtract < day:
                day -= days_to_subtract
                days_to_subtract = 0
            else:
                days_to_subtract -= day
                month -= 1
                if month < 1:
                    month = 12
                    year -= 1
                day = BS_MONTH_LENGTHS[month - 1]
    
    return year, month, day

def convert_to_nepali_date(english_date):
    # Convert the English date to Nepali date
    days_diff = days_between_dates(REFERENCE_AD_DATE, english_date)
    
    # Debugging the calculated days difference
    print(f"Days difference between {REFERENCE_AD_DATE} and {english_date}: {days_diff} days")
    
    nepali_date = add_days_to_bs_date(REFERENCE_BS_DATE, days_diff)
    return nepali_date

def show_nepali_date(english_date, nepali_date):
    # Display Nepali date, day of the week, tithi, and any important events
    nepali_day_of_week = get_nepali_day_of_week(english_date)
    nepali_day = nepali_date[2]  # Assuming nepali_date = (year, month, day) format
    nepali_month = nepali_date[1]
    
    print(f'Nepali Date: {nepali_date}')
    print(f'Day of the Week: {nepali_day_of_week}')
    print(f'Current Time: {get_time()}')
    print(f'Tithi: {get_tithi(nepali_day)}')
    print(f'Important Event: {get_important_event(nepali_month, nepali_day)}')

if __name__ == "__main__":
    # Example: Convert April 4, 2002 to Nepali date
    english_date = datetime.date(2001,8,20)
    
    # Debugging: show the original English date
    print(f"Converting English date: {english_date}")
    
    nepali_date = convert_to_nepali_date(english_date)
    
    show_nepali_date(english_date, nepali_date)
