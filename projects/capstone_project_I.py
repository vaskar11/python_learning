import datetime
import nepali_datetime

# Dictionary mapping important events to Nepali dates
IMPORTANT_EVENTS = {
    (1, 1): "नयाँ वर्ष",  # Nepali New Year (BS)
    (1, 11): "लोकतन्त्र दिवस",  # Loktantra Diwas
    (1, 18): "विश्व मजदुर दिवस",  # International Labor Day
    (1, 30): "श्रीपञ्चमी",  # Shree Panchami
    (2, 7): "ग्याल्पो लोसार",  # Gyalpo Losar
    (2, 17): "आमाको मुख हेर्ने दिन",  # Aama Ko Mukh Herne Din
    (3, 8): "महिला दिवस",  # International Women's Day
    (3, 9): "फागुपूर्णिमा",  # Fagu Purnima
    (5, 15): "कुशे औंशी",  # Kushe Aunshi
    (6, 3): "संबिधान दिवस",  # Constitution Day
    (6, 8): "विश्व वातावरण दिवस",  # World Environment Day
    (6, 11): "गणेश चतुर्थी",  # Ganesh Chaturthi
    (7, 1): "विश्व पर्यटन दिवस",  # World Tourism Day
    (8, 25): "ग्याल्बो लोसार",  # Gyalpo Losar
    (9, 1): "विश्व पर्यटन दिवस",  # World Tourism Day
    (9, 7): "उधौली पर्व",  # Udhauli Parva
    (9, 12): "मोहनी नख",  # Mohani Nakha (Newa)
    (9, 15): "अन्नपूर्ण यात्रा",  # Annapurna Yatra
    (9, 23): "यमरी पुन्ही",  # Yomari Punhi
    (10, 1): "माघे संक्रान्ति",  # Maghe Sankranti
    (11, 7): "प्रजातन्त्र दिवस",  # Democracy Day
    (11, 8): "सोनाम ल्होसार",  # Sonam Lhosar

}

# Nepali tithi information
TITHI_LIST = [
    "प्रतिपदा", "द्वितीया", "तृतीया", "चतुर्थी", "पञ्चमी", "षष्ठी", "सप्तमी", "अष्टमी",
    "नवमी", "दशमी", "एकादशी", "द्वादशी", "त्रयोदशी", "चतुर्दशी", "पूर्णिमा", "अमावस्या"
]

class NepaliCalendar:
    def __init__(self, english_date =None):
        if english_date is None:
            self.english_date= datetime.datetime.now()
        else:
            self.english_date= english_date
           
        # COnvert to Nepali Date usign nepali_datetime library 
        self.nepali_date= nepali_datetime.date.from_datetime_date(self.english_date.date())
        self.day_of_week= self.get_nepali_day_of_week()
        
    def get_nepali_day_of_week(self):
        #  days of week in nepali
        nepali_days = [
         "सोमबार", "मंगलबार", "बुधबार", "बिहिबार", "शुक्रबार", "शनिबार","आइतबार"
        ]
        return nepali_days[self.english_date.weekday()]
        #here .weekday return the days name starting from monday as in 0th index so we have to arrage the nepali days as sombar in the 0th index to return the same value.
        
    def get_tithi(self):
        day_of_month= self.nepali_date.day
        tithi_index= (day_of_month-1)% len(TITHI_LIST) #here -1 is done as tithi list index start from 0 so to index to day 1 it will gives (1-1)=0 ---> प्रतिपदा
        return TITHI_LIST[tithi_index]
    
    def get_important_event(self):
        #it will check if the nepali date has an important event
        nepali_month_day=(self.nepali_date.month, self.nepali_date.day)
        return IMPORTANT_EVENTS.get(nepali_month_day,"No special event today")
    
    def get_time(self):
        current_time= self.english_date.time()
        return current_time.strftime("%H:%M:%S")
    
    def show_nepali_date(self):
        print(f'Nepali Date: {self.nepali_date}')
        print(f'Day of the Week: {self.day_of_week}')
        print(f'Time: {self.get_time()}')
        print(f'Tithi: {self.get_tithi()}')
        print(f'Important Event: {self.get_important_event()}')
        
if __name__ =="__main__":
    english_date= datetime.datetime(2024,12,25) 
    nepali_calendar= NepaliCalendar(english_date) 
    nepali_calendar.show_nepali_date()

